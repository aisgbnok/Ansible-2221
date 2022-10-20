# Configuring SSH on Server Devices

> **Note**\
> This guide only pertains to Linux/Unix based Ansible Control Nodes.
> Each section explains how to configure the Ansible CN to control varying OS hosts or managed nodes.

## Windows

### Passwordless SSH Authentication

To enable passwordless SSH authentication between a control node and a managed node, you must copy the Ansible CN's public RSA key to the managed node.

#### Administrator Account

If you are using an administrator account on the managed node, then the CN's RSA key must be placed in the `C:\ProgramData\ssh\administrators_authorized_keys` file.
Additionally, the file must be given specific permissions for the OpenSSH server to accept it.
Run the following commands in an elevated PowerShell prompt, replacing `user`@`ip` with the managed node's corresponding values.

```bash
scp ~/.ssh/id_rsa.pub user@ip:/ProgramData/ssh/administrators_authorized_keys
```

```bash
ssh user@ip 'icacls.exe ""C:\ProgramData\ssh\administrators_authorized_keys"" /inheritance:r /grant ""Administrators:F"" /grant ""SYSTEM:F""'
```

#### Standard User

If you are using a standard account on the managed node, then the CN's RSA key must be placed in the users `.ssh\authorized_keys` file.
Run the following commands in an elevated PowerShell prompt, replacing `user`@`ip` with the managed node's corresponding values.

```bash
scp ~/.ssh/id_rsa.pub user@ip:/Users/`user`/.ssh/authorized_keys
```

## Linux

```bash
ssh-copy-id user@ip
```