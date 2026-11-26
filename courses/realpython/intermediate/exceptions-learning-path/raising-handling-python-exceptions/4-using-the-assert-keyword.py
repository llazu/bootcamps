"""
The assert test if a condition is true

if true, the code runs.
if false, an assert exception is raise.
"""
class WrongOSError(Exception):
    pass

import sys

# if not sys.platform.startswith("linux"):
    # raise AssertionError("Wrong OS!")

# only use the assert keyword when 
# you don't need to optimize the code
# other wise this version of assert doesn't run
assert sys.platform.startswith("linux"), "Wrong OS!"

