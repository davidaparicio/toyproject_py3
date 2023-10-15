# My Project

A brief description of your project.

## Installation

How to install your project.

```
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install pytest
```

## Usage

Provide usage examples or API documentation.


## Project structure

- [The Anatomy of a Minimalist Python Repository Boilerplate](https://medium.com/@tszumowski/the-anatomy-of-a-minimalist-python-repository-boilerplate-26cb2a296ba4)
- [Other boilerplate](https://github.com/topics/python-boilerplate)
- [Python Boilerplate](https://www.python-boilerplate.com/py3+executable+unittest)
- [Unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)


```Python3
toyproject/
|-- project/
|   |-- __init__.py
|   |-- main.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- user.py
|   |   |-- product.py
|   |-- utils/
|   |   |-- __init__.py
|   |   |-- helpers.py
|-- tests/
|   |-- __init__.py
|   |-- test_user.py
|   |-- test_product.py
|-- setup.py
|-- README.md
|-- .gitignore
```

## Poetry

Remember, when using Poetry:

    To activate the project's virtual environment, use poetry shell.
    To run commands within the virtual environment without activating it, use poetry run <command>. For example, to run a Python script: poetry run python script.py.

Poetry brings simplicity and a modern touch to Python project management. It's a great choice for those who prefer an all-in-one solution compared to the traditional setuptools + pip + venv combo.

## __init__

For most of these __init__.py files, their primary purpose is to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as "string", from unintentionally hiding valid modules that occur later (deeper) on the module search path.

Remember, the use of __init__.py allows you to control what gets exposed when the package is imported using the from package import * syntax, and they also allow you to split a module into multiple files but still allow them to be imported as a unified whole.

## Some issues

- [Adding Parent Directory to Python Path](https://safjan.com/python-add-parent-directory-to-path/)
- [ModuleNotFoundError: no module named Python Error (Fixed)](https://www.freecodecamp.org/news/module-not-found-error-in-python-solved/)
- [What’s New In Python 3.12](https://docs.python.org/3/whatsnew/3.12.html)

``` 
daparici@FVFJ81HR1WGC toyproject_py3 % python3 tests/test_product.py
Traceback (most recent call last):
  File "/Users/daparici/code/github.com/davidaparicio/toyproject_py3/tests/test_product.py", line 2, in <module>
    from my_project.models.product import Product
ModuleNotFoundError: No module named 'my_project'

daparici@FVFJ81HR1WGC toyproject_py3 % pwd
/Users/daparici/code/github.com/davidaparicio/toyproject_py3
daparici@FVFJ81HR1WGC toyproject_py3 % export PYTHONPATH=$PYTHONPATH:/Users/daparici/code/github.com/davidaparicio/toyproject_py3
daparici@FVFJ81HR1WGC toyproject_py3 % python3 tests/test_product.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```