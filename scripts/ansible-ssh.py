#!/usr/bin/env python3

"""
CDT-2221 Alpha Red Team
Author: Anthony Swierkosz; ajs2576

Installs SSH keys for Ansible to use.
"""

import subprocess

user = "Administrator"
ip = "10.1.4.7"


def windows_ssh(user, ip):
    print(f'\n\n{"":-^48}')
    print(f'{f" {user}@{ip} ":-^48}')
    print(f'{"":-^48}')

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


def main():
    print("Welcome to ")

# Only if this file is run directly
if __name__ == '__main__':
    print("Welcome, this configures SSH keys for Windows.")
    print("It's not pretty, unfortunately.")

    option = input("1) Manual 2) Auto").strip()

    if option == "1":
        user = input("Enter the username: ").strip()
        ip = input("Enter the IP address: ").strip()
        windows_ssh(user, ip)

    else:
        windows_ssh("bruh", "10.1.7.7")
        windows_ssh("bruh", "10.2.7.7")
        windows_ssh("bruh", "10.1.6.2")
        windows_ssh("bruh", "10.2.6.2")
        windows_ssh("bruh", "10.1.6.3")
        windows_ssh("bruh", "10.2.6.3")
        windows_ssh("bruh", "10.1.6.4")
        windows_ssh("bruh", "10.2.6.4")
        windows_ssh("bruh", "10.1.6.5")
        windows_ssh("bruh", "10.2.6.5")
