"""
try:
    run this code
exception:
    execute this code when
    there is an exception
"""
import sys

class WrongOsError(Exception):
    pass

def windows_interaction():
    if not sys.platform.startswith("windows"):
        raise WrongOsError(
            "WARNING - Windows Only. ",
            f"Your system: '{sys.platform}'"
        )
    print("Doing important Windows work!")



