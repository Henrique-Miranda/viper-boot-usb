import subprocess

def formatDevice(device):
    subprocess.Popen('sgdisk --zap-all {device}', shell=True)
    subprocess.Popen('sgdisk -n 0:0:+1Mib -t 0:ef02 {device}', shell=True)
    subprocess.Popen('sgdisk -n 0:0:+50Mib -t 0:ef00 {device}', shell=True)