import subprocess


def formatDevice(device, datapartType='ntfs'):
    subprocess.run(f'umount -f {device}*', shell=True)
    subprocess.run(f'sgdisk --zap-all {device}', shell=True)
    subprocess.run(f'sgdisk -g {device}', shell=True)
    subprocess.run(f'sgdisk -n 1:0:+1M -t 1:ef02 -c 1:"BIOS boot partition" {device}', shell=True)
    subprocess.run(f'sgdisk -n 2:0:+50M -t 2:ef00 -c 2:"EFI System" {device}', shell=True)
    subprocess.run(f'sgdisk -n 3:0:0 -t 3:0700 -c 3:"Viper Boot" {device}', shell=True)
    subprocess.run(f'umount {device}', shell=True)
    subprocess.run(f'sgdisk -h 1:2:3 {device}', shell=True)
    subprocess.run(f'sgdisk -A 3:set:2 {device}', shell=True)
    subprocess.run(f'umount {device}', shell=True)
    subprocess.run(f'wipefs -af {device}1', shell=True)
    subprocess.run(f'wipefs -af {device}2', shell=True)
    subprocess.run(f'mkfs.vfat -v -F 32 {device}2', shell=True)
    subprocess.run(f'wipefs -af {device}3', shell=True)
    if datapartType == 'ntfs':
        subprocess.run(f'mkfs -t ntfs -f {device}3', shell=True)
    elif datapartType == 'fat32':
        subprocess.run(f'mkfs.vfat -v -F 32 {device}3', shell=True)
    elif datapartType == 'ext4':
        subprocess.run(f'mkfs.ext4 {device}3', shell=True)
    else:
        exit('[Error] The filesystem selected for datapart is not supported!')
    subprocess.run(f'umount {device}', shell=True)


