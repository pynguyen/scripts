# scripts
### adb_capture.py
Usage: 
adb_capture.py -a <app_name> -d <device_id>

By default script will get the first device to run

Examples:
```sh
python adb_capture.py
python adb_capture.py -a Telegram
python adb_capture.py -a Telegram -d emulator-5554
```

### start_emulator.py
Usage:

start_emulator.py -e <emulator_name>

By default script will get the first emulator to run

Open start_emulator.py file. Edit emulator_path variable according to your computer:
```sh
emulator_path = "/Users/pynguyen/Library/Android/sdk/emulator/emulator"
```

Examples:
```sh
python start_emulator.py
python start_emulator.py -e Pixel_2_API_R
```