# This is a regular python file, where we define a function that will
# be imported in the submodule's __init__.py, and thus made accessible
# as: my_package.my_module.square

def square(x):
    if x<0:
        return 10
    return x ** 2
