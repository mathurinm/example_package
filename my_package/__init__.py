print("my_package is being imported")  # noqa E402

from .utils import my_function
# we will be able to do: from my_module import my_function, or
# my_module.my_function
