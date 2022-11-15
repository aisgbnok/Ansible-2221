# Configuring SSH on Server Devices

> **Note**\
> This guide only pertains to Linux/Unix based Ansible Control Nodes.
> Each section explains how to configure the Ansible CN to control varying OS hosts or managed nodes.

## Generate Control Node SSH Key

You may need to generate an SSH key for the control node.
For example, if the `.ssh` directory doesn't exist in your user profile.

```shell
ssh-keygen -t ed25519
```

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

```bash
sudo ssh user@ip 'icacls "C:\ProgramData\ssh\\administrators_authorized_keys" /remove "NT AUTHORITY\Authenticated Users"'
```

```bash
sudo ssh user@ip 'icacls "C:\ProgramData\ssh\\administrators_authorized_keys" /inheritance:r'
```

#### Standard User

If you are using a standard account on the managed node, then the CN's RSA key must be placed in the users `.ssh\authorized_keys` file.
Run the following commands in an elevated PowerShell prompt, replacing `user`@`ip` with the managed node's corresponding values.

```bash
scp ~/.ssh/id_rsa.pub user@ip:/Users/`user`/.ssh/authorized_keys
```

## Linux

Copy the CN's public key to a Linux managed node.

> **Note**\
> If you receive `ERROR: No identities found`, then an SSH key is not found.
> This most likely means you need to [generate an SSH key.](#generate-control-node-ssh-key)

```bash
ssh-copy-id user@ip
```

###  Kali
> **Note**\
> Some distributions like Kali require you to regenerate the default SSH keys.
1. Regenerate your distribution's default SSH keys.
   ```shell
   sudo dpkg-reconfigure openssh-server
   ```
2. Enable the SSH service.
    ```shell
   sudo systemctl status ssh.service
   ```
3. (Optional) Enable password based SSH authentication.
   ```shell
   sudo vim /etc/ssh/ssh_config
   ```
   Uncomment the following line:
      ```text
   PasswordAuthentication yes
   ```
   Save the `ssh_config` file: <kbd>Escape</kbd><kbd>:</kbd><kbd>w</kbd><kbd>q</kbd><kbd>Enter</kbd>.