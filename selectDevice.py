from listDevices import listDevices
import os


def selectDevice():
    devices = listDevices()
    for n, device in devices:
        if device['rm'] and device['tran'] == 'usb' and device['type'] == 'disk':
            print(f'ID: {n} Brand: {device["vendor"]} Model: {device["model"]} Path: {device["path"]} '
                  f'Label: {device["label"]} Size: {device["size"]}')

    option = int(input('Select a device listed above by ID: '))
    sDevice = devices[option][1]
    print('The device selected is : ', sDevice['path'])
    warn = input('This device will be FULL ERASED, do you want to continue? [y\\N]').lower()
    if warn == 'y':
        return sDevice

    os.system('clear')
    selectDevice()
