# soccerML
predict soccer matches 

## Setup

- [Requirements](#markdown-header-requirements)
- [Initial setup](#markdown-header-initial-setup)
- [Handle Dependencies](#markdown-header-handle-dependencies)

### Requirements

#### Python 3.6

Make sure you have Python 3.6 installed on your local system.
It's currently the latest supported language of tensorflow.

```sh
https://www.python.org/downloads/release/python-368/
```

### Initial setup

Setup virtual environment locally on your project.

```sh
virtualenv -p python3 ./venv
```

### Handle dependencies
```sh
# Make sure that you use venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# After adding new dependencies
pip freeze > requirements.txt
```

## football api evaluation
There were 3 different soccer api in the final evaluation process as data provider.

Following aspects were considered in the evaluation process:
+ diversity of data
+ documentation
+ price

| criteria  |api-football   | football-data  | apifootball  |
|---|---|---|---|
| data diversity  | ++  | +  | +  |   
| documentation | ++  | 0  | 0 |   
| price  |  + | 0  |  0 |   

api-football was the winner of the evaluation process and will be choosen as data provider 
for the soccer prediction.