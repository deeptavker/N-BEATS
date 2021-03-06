
import logging
import os
from typing import Dict

import gin
import numpy as np
import pandas as pd
import torch as t
from fire import Fire

from common.experiment import Experiment
from common.sampler import TimeseriesSampler
from common.torch.ops import to_tensor
from common.torch.snapshots import SnapshotManager
from datasets.m3 import M3Dataset, M3Meta
from experiments.trainer import trainer
from experiments.model import generic, interpretable
from summary.utils import group_values


class M3Experiment(Experiment):
    @gin.configurable()
    def instance(self,
                 repeat: int,
                 lookback: int,
                 loss: str,
                 history_size: Dict[str, int],
                 iterations: Dict[str, int],
                 model_type: str):
        dataset = M3Dataset.load(training=True)

        forecasts = []
        for seasonal_pattern in M3Meta.seasonal_patterns:
            sp_history_size = history_size[seasonal_pattern]
            horizon = M3Meta.horizons_map[seasonal_pattern]
            input_size = lookback * horizon

            # Training Set
            training_values = group_values(dataset.values, dataset.groups, seasonal_pattern)

            training_set = TimeseriesSampler(timeseries=training_values,
                                             insample_size=input_size,
                                             outsample_size=horizon,
                                             window_sampling_limit=int(sp_history_size * horizon))
            if model_type == 'interpretable':
                model = interpretable(input_size=input_size, output_size=horizon)
            elif model_type == 'generic':
                model = generic(input_size=input_size, output_size=horizon)
            else:
                raise Exception(f'Unknown model type {model_type}')

            # Train model
            snapshot_manager = SnapshotManager(snapshot_dir=os.path.join(self.root, 'snapshots', seasonal_pattern),
                                               total_iterations=iterations[seasonal_pattern])
            model = trainer(snapshot_manager=snapshot_manager,
                            model=model,
                            training_set=iter(training_set),
                            timeseries_frequency=M3Meta.frequency_map[seasonal_pattern],
                            loss_name=loss,
                            iterations=iterations[seasonal_pattern])

            # Build forecasts
            x, x_mask = map(to_tensor, training_set.last_insample_window())
            model.eval()
            with t.no_grad():
                forecasts.extend(model(x, x_mask).cpu().detach().numpy())

        forecasts_df = pd.DataFrame(forecasts, columns=[f'V{i + 1}' for i in range(np.max(M3Meta.horizons))])
        forecasts_df.index = dataset.ids
        forecasts_df.index.name = 'id'
        forecasts_df.to_csv(os.path.join(self.root, 'forecast.csv'))


if __name__ == '__main__':
    logging.root.setLevel(logging.INFO)
    Fire(M3Experiment)
