# An example of python package

## Why use packages?
It is a good practice to not code the same function twice, and to reuse common code from one python script to the other.

To import the function `some_function` defined in `some_file.py`, you can do:
```python
from some_file import some_function
```
but this only works if you run your code in the same folder as `some_file.py`.
If you want to make `some_function` accessible from anywhere on your computer, *you should not use*
```python
import sys
sys.path.append("the/path/to/some_file.py")
```
because when you share your code with other people, this breaks most of the time.

Instead, you should **create a python package** containing the code you need.
The following shows how to do it.

## Package structure
This repository contains a basic python package, named `my_package`.
Its structure is as follows (ignore the `my_submodule` folder so far):
```
example_package   (the main directory/folder)
├── my_package  (code folder, must have the name of the module)
│   └── __init__.py   (a special Python file, is executed whenever you import my_package)
|   └── utils.py   (a regular Python file in which you define functions, variables, classes, etc)
├── setup.py  (this special file must be executed to install the package)
└── README.md   (contains what you are currently reading)
```

The mandatory files, which must have exactly this name, are `setup.py` and `my_package/__init__.py`. On the other hand, note that:
- `utils.py` could have an arbitrary other name
- `README.md` is not necessary for a package, and is used here to give information to the people browsing the Github repository

## Package installation
Once you have the files defined above, you should open a terminal, move to where the `setup.py` file is (using the `cd` command), then execute
```pip install -e .```

After that, **from any location on your computer** you can open an ipython terminal and run:
```python
import my_package
from my_package import my_function
my_function()
# etc, just like when you do: from pandas import read_csv
```


## How does it work?
Running `pip install -e .` tells python to remember where it should look when you refer to `my_package` in some code.
Whenever you run `import my_package`, it will go to this location, and run the `__init__.py`.
Inside the `__init__.py`, you have imported or defined some variables (functions, classes, constants, etc), that are now usable in your main script.

The `-e` stands for `--editable`: if you use this flag, changes made to the source code after installation will have repercussions on future uses of the package. If you don't use it, when running `pip install .`, pip will copy the source code in its current state and place it in a different location, hence if you modify the source code, changes will not be taken into account (you'd need to reinstall the package for that).  

# More advanced

## Submodules
When you do:
```python
from sklearn.linear_model import Lasso
```
you are using the submodule `linear_model` of `sklearn`.
When you codebase grows, splitting it into submodules is nice to keep your code organized (for example, all code related to Linear Models go into the `linear_model` submodule; preprocessing go into `sklearn.preprocessing`, etc).

in simple terms, a submodule is a package defined inside a package (meaning it also has its own `__init__.py`), using this folder structure:
```
example_package
├── my_package
    └── __init__.py
    └── my_submodule
        └── __init__.py
```
usually, the `__init__.py` file import variables defined in other files inside the `my_submodule/` folder (not shown here for simplicity).
Here we just defined one function, `square`, in an auxiliary file inside `my_submodule/`, and we import it inside the submodule's `__init__.py`, thus making it accessible with:
```python
from my_package.my_submodule import square
# similar to: from numpy.linalg import norm
```

## Unit tests
You want to make sure that the code you wrote behaves as you expect, and that when you change other parts of the code, you don't break existing parts.
To automate these checks, you should write unit checks: functions that test the output of your code on some data, and check that it is equal to the value you want in that case. Usually, this check is done through an assertion.

In `my_package/my_submodule/test_submodule.py`, we give an example of such a test: we call our function `square(2)` and check that it returns 4.

You should run your tests regularly (with a *Continuous Integration* - CI, you can do this every time you push to your repo, for example); we recommend using `pytest` (installable with pip/conda).

At the root of the repo, run `pytest` and check the output: in all files starting with `test_`, all functions starting with `test_` are run, and if an assertion inside fails, the test fails.

**Exercice**: modify the content of `test_square` so that the test passes.

