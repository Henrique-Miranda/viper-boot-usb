import subprocess
import json

def listDevices():
    devs = subprocess.check_output("""lsblk -o path,tran,rm,type | awk '{if($2=="usb" && $3==1 && $4=="disk")print $1}' """, shell=True)
    devices = []
    for d in devs.decode().split():
        devices.append(json.loads(subprocess.check_output(f'lsblk -O {d} -J', shell=True))['blockdevices'][0])
    return tuple(enumerate(devices))

