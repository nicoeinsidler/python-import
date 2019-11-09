# 1st attempt
# from ..sub_sub_a import a
# print(a.test_function())

# 2nd attempt
# import importlib
# importlib.import_module('..sub_sub_a', 'module')
# print(sub_sub_a.test_function())


# 3rd attempt
import sys
import pathlib

PATH_TO_MODULE = pathlib.Path('../..').resolve().absolute()
if str(PATH_TO_MODULE) not in sys.path:
    sys.path.insert(0, str(PATH_TO_MODULE))

import module.sub_a.sub_sub_a as a

print(a.test_function())