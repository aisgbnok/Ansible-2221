# Configuring Ansible

## Ansible Inventory

You need to overwrite the default Ansible inventory located at `/etc/ansible/hosts` with the inventory you want to use.
This will allow you to use the repository's playbooks.

> **Note**\
> This repository [contains inventories in the `configs` directory](../../configs) that may be helpful.

Example command for overwriting default Ansible inventory, also known as the hosts file.

```shell
sudo cp configs/gray-inventory.yml /etc/ansible/hosts
```
