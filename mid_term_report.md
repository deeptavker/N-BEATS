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

#### 5. N-BEATS Code review

##### 5.1 Building N-BEATS

The `MAKEFILE` in the repository targets a docker-based environment for building and testing N-BEATS. However, we decided to do it without Docker as it has it's own time and memory related issues. We built N-BEATS from the source code using basic environment variables and figured out how to run various experiments. 

Demon for running an experiment on a bash terminal using N-BEATS for the 1.3Mb M3 dataset which is manually downloaded and placed in `storage/datasets/m3/`. 

```sh
git clone https://github.com/deeptavker/N-BEATS
cd N-BEATS
pip3 install -r requirements.txt
export PYTHONPATH=$PWD
export STORAGE=$PWD/storage
python3 datasets/m3.py M3Dataset download
python3 experiments/m3/main.py --config_path=$PWD/experiments/m3/generic.gin build_ensemble
python3 experiments/m3/main.py --config_path=$PWD/experiments/m3/interpretable.gin build_ensemble
python3 experiments/m3/main.py --config_path=storage/experiments/m3_generic/repeat=3,lookback=4,loss=MAPE/config.gin run
# GENERATED FILE for specific params : storage/experiments/m3_generic/repeat=3,lookback=4,loss=MAPE/forecast.csv
```

------------------

#### 6. Direction for future work

