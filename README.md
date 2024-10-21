# CountTo2Billion
Count to 2 billion in less than a second. 🤯

This is a quick demo of how to optimize your Python code using Cython. 

## Pre-requisites
- Python 3.x
- C compiler

## Installation
- Install C compiler in Ubuntu
```
sudo apt install python3-dev gcc
```
- Activate environment and install Cython
```
python3 -m venv env
source env/bin/activate
pip install cython
```

## Execution
- Compile the `.pyx` file.
```
python3 setup.py build_ext --inplace
```
- Run `test.py`
```
python3 test.py
```
