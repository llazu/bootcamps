# raise allows you to raise your own exceptions
import sys

# create your own exeptions
class WrongOsError(Exception):
    pass

# checks if the OS is linux
if not sys.platform.startswith("linux"):
    #raise Exception("oops...")
    raise WrongOsError("Wrong OS!")

# raise forces the exception and the termination
# of the program