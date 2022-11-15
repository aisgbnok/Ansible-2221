#!/usr/bin/env python3

"""
CDT-2221 Alpha Red Team
Author: Anthony Swierkosz; ajs2576

Updates local Ansible inventory with repository inventory.
"""

import shutil
from os import path, makedirs


def update_inventory():
    """
    Updates the local Ansible inventory file with the repository inventory.

    :return: None
    """
    # Generate source path from current file location
    base_path = path.dirname(__file__)
    src_path = path.abspath(path.join(base_path, "..", "configs", "red-inventory.yaml"))

    # Generate destination path and create directories
    dest_path = "/etc/ansible/hosts"
    if not path.exists(dest_path):
        makedirs(path.dirname(dest_path), exist_ok=True)

    # Copy file
    shutil.copy(src_path, dest_path)


# Only if this file is run directly
if __name__ == '__main__':
    update_inventory()