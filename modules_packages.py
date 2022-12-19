# ### Modules ###
#
# import example_module
#
# from example_module import add
#
# print(add(1, 2, 3, 4))
# print(example_module.mul(1, 2))
#
#
# import math
#
# print(math)
#
#
# ## Built in modules & Installed modules
#
# print(dir(__builtins__))
#
# import pandas
#
#
# ### Python module search paths
#
# """
# 1. Same directory
# 2. Path/pythonpath which is list of env variable
# 3. Installation directory
# """
#
# import sys
# print(sys.path)  # Can find where python is searching for modules
#
# import datetime
# import os
# print(os.getcwd())
#
# print(datetime.datetime.utcnow())
#

# import conditional_exercise
#
# if __name__ == '__main__':
#     pass

## Packages
"""
Packages are directories which must contain a special empty __init__.py file along with not modules.
This indicates the directory is a package and can be imported the same way a module is imported.
"""

# import example_package

# import example_package
# from example_package import example_module
# from example_package.example_module import add
#
# print(add())


## Zen of python

import this
