# author: pynguyen
# email: pynguyen.dev@gmail.com

"""
requirement:
pip install -U pure-python-adb 
(https://github.com/Swind/pure-python-adb)
"""

from ppadb.client import Client as AdbClient
from datetime import datetime
import sys
import getopt


def main(argv):
    app_name = "screen"
    device_id = ""

    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    if len(devices):
        device_id = devices[0].serial
        print("devices: {}".format(device_id))
    else:
        print("Not found devices")
        sys.exit(2)
    
    try:
       opts, args = getopt.getopt(argv, "ha:d:", ["aname=", "device="])
    except getopt.GetoptError:
       print("usage: adb_capture.py -a < app_name > -d < device_id >")
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print("usage: adb_capture.py -a < app_name > -d < device_id >")
          sys.exit()
       elif opt in ("-a", "--aname"):
          app_name = arg
       elif opt in ("-d", "--device"):
          device_id = arg

    device = client.device(device_id)

    now = datetime.now()
    time = now.strftime("%Y%m%d_%H%M%S")
    screenshot_shell = "screencap -p /sdcard/{}_{}.png".format(app_name, time)
    pull_source_shell = "/sdcard/{}_{}.png".format(app_name, time)
    pull_target_shell = "{}_{}.png".format(app_name, time)

    device.shell(screenshot_shell)
    device.pull(pull_source_shell, pull_target_shell)

    print(pull_target_shell)


if __name__ == "__main__":
   main(sys.argv[1:])
