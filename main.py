from selectDevice import selectDevice
from formatDevice import formatDevice
from grubInstall import grubInstall
import os

class App(object):
    def __init__(self):
        self.sDevice = selectDevice()
        self.dPath = self.sDevice['path']
        datapartType = input('Select type for the data partition. \n [1] - fat32 \n [2] - ntfs \n [3] - ext4 \n [4] - exfat \n ')
        formatDevice(self.dPath, datapartType)
        grubInstall(self.dPath)
        print('DONE!')


if os.geteuid() != 0:
    exit('You need sudo permissions to run this script!')

app = App()


# test efi boot sudo qemu-system-x86_64 -m 1024 -enable-kvm -usb -device usb-host,hostbus=2,hostaddr=3
# extract windows iso 7z x -tudf -y "Win7_Pro_SP1_BrazilianPortuguese_x64 - PHDowns.iso" -owin7x64/
