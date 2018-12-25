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