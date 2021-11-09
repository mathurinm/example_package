This is a very basic python package.
Its structure is the common one to all Python packages:
```
module_example   (the parent directory)
├── my_module  (must be the name of the module)
│   └── __init__.py   (a special Python file, is executed whenever I import my_module)
|   └── utils.py   (a regular Python file in which I can define functions, variables, classes)
├── setup.py  (must be executed to install the package)
└── README.md   (this file)
```

Once you have defined all these files, you should open a terminal, move to where the `setup.py` file is, then execute
`pip install -e .`

After that, from any location on your computer you can open an ipython terminal and run:
```
import my_module
from my_module import my_function
# etc, just like from sklearn.linear_model import Lasso
```


More advanced note: `my_module` could have submodules, i.e. subfolders inside my_module, with their own __init__.py file. For example `np.linalg` is a submodule of `numpy`, `sklearn.linear_model` is a submodule of scikit-learn, etc.