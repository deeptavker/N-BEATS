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


###### 5.3.2 datasets
```
├── datasets    
│   ├── __init__.py   
│   ├── m3.py   

```
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

- Extend the architecture for multivariate time series forecasting
- Extend the architecture for graph convolutions (applications to traffic forecasting models)

