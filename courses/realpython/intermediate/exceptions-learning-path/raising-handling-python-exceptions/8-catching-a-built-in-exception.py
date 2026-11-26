import sys

class WrongOsError(Exception):
    pass

def windows_interaction():
    if not sys.platform.startswith("win"):
        raise WrongOsError (
            ("WARNING"
            "Windows Only"
            f"Using {sys.platform}"
            )
        )

def mac_interaction():
    if not sys.platform.startswith("darwin"):
        raise WrongOsError(
            (
                "Warning!\n"
                "Wrong OS.\n"
                "MAC only\n"
                f"Using {sys.platform}"
            )
        )

try:
   #mac_interaction()
   windows_interaction()
except WrongOsError as error:
    print("Using wrong OS!")
else:
    print("✅ No problem, work done")
    print("📝 Read logging file...")
    try:
        with open("file.log") as log_file:
            print(log_file.read())
    except FileNotFoundError as error:
        print("🥺 Oops", error)

print("happens after")