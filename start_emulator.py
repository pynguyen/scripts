# author: pynguyen
# email: pynguyen.dev@gmail.com

"""
requirement:
"""

import subprocess
from datetime import datetime
import sys
import getopt


def main(argv):
    emulator_path = "/Users/pynguyen/Library/Android/sdk/emulator/emulator"
    emulator_name = "Nexus_5X_API_23"
    agr_list_avds = "-list-avds"

    emulators = subprocess.run(
        [emulator_path, agr_list_avds], stdout=subprocess.PIPE, text=True)
    
    if len(emulators.stdout):
        print("All emulators: ")
        print(emulators.stdout)
        emulator_name = emulators.stdout.splitlines()[0]
    else:
        print("Not found emulators")
        sys.exit(2)

    try:
       opts, args = getopt.getopt(argv, "he:", ["emulator="])
    except getopt.GetoptError:
       print("usage: start_emulator.py -e <emulator_name>")
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print("usage: start_emulator.py -e <emulator_name>")
          sys.exit()
       elif opt in ("-e", "--emulator"):
          emulator_name = arg
    print("Starting emulator: ", emulator_name)
    subprocess.run(
        [emulator_path, "-avd", emulator_name], stdout=subprocess.PIPE, text=True)

if __name__ == "__main__":
   main(sys.argv[1:])
