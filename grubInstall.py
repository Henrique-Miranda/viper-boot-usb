import subprocess


def grubInstall(device):
    subprocess.run(f'umount -f /mnt*', shell=True)
    subprocess.run(f'mount {device}3 /mnt', shell=True)
    subprocess.run('mkdir -p /mnt/boot/EFI', shell=True)
    subprocess.run(f'mount {device}2 /mnt/boot/EFI', shell=True)
    p1 = subprocess.Popen('grub-install --target=x86_64-efi --recheck --removable --efi-directory=/mnt/boot/EFI '
                          '--boot-directory=/mnt/boot', shell=True)
    p2 = subprocess.Popen(f'grub-install --force --target=i386-pc --recheck --boot-directory=/mnt/boot {device}', shell=True)
    p3 = subprocess.Popen(f'grub-install --force --target=i386-pc --recheck --boot-directory=/mnt/boot {device}3', shell=True)
    
    subprocess.run('mkdir -p /mnt/boot/ISOs', shell=True)
    p1.wait()
    p2.wait()
    p3.wait()
    subprocess.run(f'umount -f /mnt*', shell=True)
