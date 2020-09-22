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
    ├── processed_files
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

