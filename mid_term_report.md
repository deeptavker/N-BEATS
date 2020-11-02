### Mid Term Review 

#### Overview

1. Literature Review
2. Main Paper
3. Three papers which build up on NBEATS
4. Three papers which inspired NBEATS
5. N-BEATS Code review
6. Direction for future work

------------------

#### 1. Literature Review

------------------

#### 2. Main Paper

------------------

#### 3. Three papers which build up on NBEATS

------------------

#### 4. Three papers which inspired NBEATS

------------------

#### 5. N-BEATS Code review for m3 dataset

##### 5.1 Setting up and running N-BEATS model

The `MAKEFILE` in the repository targets a docker-based environment for building and testing N-BEATS. However, we decided to do it without Docker as it has it's own time and memory related issues. We built N-BEATS from the source code using basic environment variables and figured out how to run various experiments on Google Colab and on a Unix console. 

Demo for running an experiment on a bash terminal using N-BEATS for the 1.3Mb M3 dataset which is manually downloaded and placed in `storage/datasets/m3/`. 

```sh
git clone https://github.com/deeptavker/N-BEATS
cd N-BEATS
pip install -r requirements.txt
export PYTHONPATH=$PWD
export STORAGE=$PWD/storage
python datasets/m3.py M3Dataset download
python experiments/m3/main.py --config_path=$PWD/experiments/m3/generic.gin build_ensemble
python experiments/m3/main.py --config_path=$PWD/experiments/m3/interpretable.gin build_ensemble
python experiments/m3/main.py --config_path=storage/experiments/m3_generic/repeat=3,lookback=4,loss=MAPE/config.gin run
# GENERATED FILE for specific params : storage/experiments/m3_generic/repeat=3,lookback=4,loss=MAPE/forecast.csv
```
##### 5.2 Analysis of Results

##### 5.3 N-BEATS Code Structure & Review

```
.
└── N-BEATS
    ├── common
    ├── datasets
    ├── experiments
    ├── models
    ├── notebooks
    ├── storage
    ├── summary
    └── test
```

###### 5.3.1 common
```
├── common                                                                        
│   ├── __init__.py    
│   ├── experiment.py    
│   ├── http_utils.py     
│   ├── metrics.py     
│   ├── sampler.py   
│   ├── settings.py   
│   └── torch    
│       ├── __init__.py    
│       ├── losses.py     
│       ├── ops.py    
│       └── snapshots.py    
```

`experiment.py` 

This python module defines the base class for building experiment related configuration files based on ensemble parameters and also for specific combinations of *repeats*, *lookbacks* and *losses*. The *instance* method defined in this module is defined on a case to case basis for different experiments. This module is not intended for standalone execution, rather it is used as a supporting script for modules within the *experiments* directory and other custom logic. 

`settings.py`

This python module is used to configure directory paths for datasets, tests and experiment related generated data such as specific config files, snapshots and forecasts. Specifically, as a requirement, it takes in the environment variable named *STORAGE* as input from the environment. This env. var. must be set before proceeding as much of the remaining code for N-BEATS imports this particular module for path related queries. 

`metrics.py`

This module provides subroutines for commputing various metrics for `forecast` and `target` such as `MASE`, `MAPE`, `ND`, `NRMSE`, `SMAPE1`, `SMAPE2`. Reference for each is provided in the docstrings of respective functions. 

`http_utils.py`

This file provides subroutines for downloading files from the internet and saving them at a specific path. 

`sampler.py`




###### 5.3.2 datasets
```
├── datasets    
│   ├── __init__.py   
│   ├── m3.py   

```

`m3.py`

This python script is a helper module for downloading the m3 dataset and generating required `.npy` files for training and testing. It downloads the main dataset file `m3.xls` from `https://forecasters.org/data/m3comp/M3C.xls` and puts it in `storage/datasets/m3/`. Following the download, the script reads the dataset using a pandas dataframe and breaks it down into multiple `.npy` files viz. `horizons.npy`, `ids.npy`, `groups.npy`, `test.npy` and `training.npy`. The test-train split at this stage is dictated by the horizon value. The metadata for horizons is pre-loaded. There are 4 different seasonal patterns {year, quart, month, other} for which data is availble across various groups {macro, industry, finance, micro, demographic, others}. 

###### 5.3.2 experiments
```
├── experiments
│   ├── __init__.py
│   ├── m3
│   │   ├── __init__.py
│   │   ├── generic.gin
│   │   ├── interpretable.gin
│   │   └── main.py
│   ├── model.py
│   └── trainer.py
```

`m3/main.py`

This module implements the `instance` method for the `Experiment` class in `common/experiment.py`. In this implementation, this module uses modules from `common`, `experiment` and `summary` directories from `$PYTHONPATH` to create training sets and then trains those set on the model that is either `generic` or `interpretable`. It saves the forecast in a specific directory which is defined by the implementation of `Experiment` in `common/experiment.py`. It uses the `fire` library in order to take command line arguments which defines the `gin config` to be used and whether the script will **build ensemble config files** or **run a specific experiment** based on particular values of `loss`, `lookback` and `repeat`. This file also provides a subroutine to load the generated `.npy` files during an experiment. When used with an argument of `build_ensemble` it requires a `gin config` file in order to generate multiple config files in `storage/experiments/m3_generic` or `storage/experiments/m3_interpretable`. There config files reperesent various combinations of `loss`, `repeat` and `lookback` which can be run individually or in parallel. A `forecast` file for each combination of the aforementioned three parameters is generated in respective directories within `storage/experiments/`.  


###### 5.3.2 models
```
├── models
│   ├── __init__.py
│   └── nbeats.py
```
###### 5.3.2 notebooks
```
├── notebooks
│   ├── M3.ipynb
```

###### 5.3.2 storage
```
├── storage
│   ├── datasets
│   │   └── m3
│   │       ├── M3C.xls
│   │       ├── groups.npy
│   │       ├── horizons.npy
│   │       ├── ids.npy
│   │       ├── test.npy
│   │       └── training.npy
│   ├── experiments
│   └── test
```
###### 5.3.2 summary
```
├── summary
│   ├── __init__.py
│   ├── m3.py
│   └── utils.py
```
###### 5.3.2 test
```
└── test
    ├── __init__.py
    ├── __init__.pyc
    └── summary
        ├── __init__.py
        ├── __init__.pyc
        ├── test_m3.py
```


------------------

#### 6. Direction for future work

