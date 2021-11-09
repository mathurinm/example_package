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

## Package structure
This repository contains a basic python package.
Its structure is as follows:
```
example_package   (the main directory/folder)
├── my_package  (code folder, must have the name of the module)
│   └── __init__.py   (a special Python file, is executed whenever I import my_package)
|   └── utils.py   (a regular Python file in which I can define functions, variables, classes, etc)
├── setup.py  (this special file must be executed to install the package)
└── README.md   (contains what you are currently reading)
```

The mandatory files, which must have exactly this name, are `setup.py` and `my_package/__init__.py`. On the other hand, note that:
- `utils.py` could have an arbitrary other name
- `README.md` is not necessary

## Package installation
Once you have the files defined above, you should open a terminal, move to where the `setup.py` file is (using `cd`), then execute
```pip install -e .```

After that, **from any location on your computer** you can open an ipython terminal and run:
```
import my_package
from my_package import my_function
my_function()
# etc, just like when you do: from sklearn.linear_model import Lasso
```


## How does it work?
Running `pip install -e .` tells python to remember where it should look when you refer to `my_pakage` in some code.
Whenever you run `import my_package`, it will go to this location, and run the `__init__.py`.
Inside the `__init__.py`, you have imported or defined some variables (functions, classes, constants), that are now usable in your main script.

## TODO: submodules
More advanced note: `my_package` could have submodules, i.e. subfolders inside `my_package`, with their own `__init__.py` file. For example `np.linalg` is a submodule of `numpy`, `sklearn.linear_model` is a submodule of scikit-learn, etc.