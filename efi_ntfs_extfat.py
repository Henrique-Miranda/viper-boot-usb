import subprocess
# Testing Cloning configs from Rufus compatibility with EFI:NTFS Driver see more at: https://github.com/pbatard/rufus and https://github.com/pbatard/uefi-ntfs
## TODO: Implements extraction of ISO files to Viper Boot partition.


def formatDevice(device):
    subprocess.run(f'umount -f {device}*', shell=True)
    subprocess.run(f'sgdisk --zap-all --clear {device}', shell=True)
    subprocess.run(f'sgdisk -g {device}', shell=True)
    subprocess.run(f'sgdisk -n 1:0:-2M -t 1:0700 -c 1:"Viper Boot" {device}', shell=True)
    subprocess.run(f'sgdisk -n 2:0:+512K -t 2:0700 -c 2:"UEFI" {device}', shell=True) #ntfs-uefi support
    subprocess.run(f'umount {device}', shell=True)
    #subprocess.run(f'sgdisk -A 2:set:2 {device}', shell=True)
    subprocess.run(f'umount {device}', shell=True)
    subprocess.run(f'wipefs -af {device}1', shell=True)
    subprocess.run(f'wipefs -af {device}2', shell=True)
    subprocess.run(f'mkfs.vfat -F12 -n "UEFI_NTFS" {device}2', shell=True)
    subprocess.run(f'mkfs -t ntfs -f {device}1', shell=True)
    #subprocess.run(f'mkfs.exfat {device}1', shell=True)
    subprocess.run(f'umount {device}', shell=True)
    subprocess.run(f'dd bs=512 count=1024 if=uefi-ntfs.img of={device}2', shell=True)

