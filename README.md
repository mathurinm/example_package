# An example of python package

## Why use packages?
It is a good practice to not code the same function twice, and to reuse common code from one python script to the other.

To import the function `some_function` defined in `some_file.py`, you can do:
```
from some_file import some_function
```
but this only works if you run your code in the same folder as `some_file.py`.
If you want to make `some_function` accessible from anywhere on your computer, *you should not use*
```
import sys
sys.path.append("the/path/to/some_file.py")
```
because when you share your code with other people, this breaks most of the time.

Instead, you should create a python package containing the code you need.
The following shows how to do it.

## Package structure
This repository contains a basic python package, named `my_package`.
Its structure is as follows:
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
```
import my_package
from my_package import my_function
my_function()
# etc, just like when you do: from pandas import read_csv
```


## How does it work?
Running `pip install -e .` tells python to remember where it should look when you refer to `my_package` in some code.
Whenever you run `import my_package`, it will go to this location, and run the `__init__.py`.
Inside the `__init__.py`, you have imported or defined some variables (functions, classes, constants, etc), that are now usable in your main script.

# More advanced

## Submodules
When you do:
```
from sklearn.linear_model import Lasso
```
you are using the submodule `linear_model` of `sklearn`.
When you codebase grows, splitting it into submodules is nice to keep your code organized (for example, all code related to Linear Models go into the `linear_model` submodule; preprocessing go into `sklearn.preprocessing`, etc).

in simple terms, a submodule is a package defined inside a package (meaning it also has its own `__init__.py), using this folder structure:
```
example_package
├── my_package
    └── __init__.py
    └── my_submodule
        └── __init__.py
```
usually, the `__init__.py` file import variables defined in other files inside the `my_submodule` folder (not shown here for simplicity).
