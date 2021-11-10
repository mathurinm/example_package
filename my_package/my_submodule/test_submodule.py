# this is a unit test file, designed to check that the code works as expected
# test files should have a name starting with `test_` and inside,
# test functions should also have a name starting with `test_`

import numpy as np
from my_package.my_submodule import square


def test_square():
    """We test that, on some simple cases, our `square` function behaves
    as expected."""

    np.testing.assert_equal(4, square(2))
    # this is wrong on purpose, fix it:
    np.testing.assert_equal(10, square(- 1))

    # np.testing functions are nice because if the assertion is wrong,
    # they raise a detailed, precise error message:
    # compare: `np.testing.assert_equal(1, 2)``
    # vs the python built-in  `assert 1 == 2`
