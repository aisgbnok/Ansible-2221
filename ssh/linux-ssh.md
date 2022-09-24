# Install SSH on Linux

## Install SSH on Linux Client

1. Install openssh-server on Linux client

   ```bash
   sudo apt install openssh-server
   ```

> **Note**\
> Some Distributions like Kali require extra steps:

1. Regenerate SSH keys

   ```bash
   sudo dpkg-reconfigure openssh-server
   ```

1. Enable the SSH Service

   ```bash
   sudo systemctl status ssh.service
   ```

1. (Optional) Enable Password Based Authentication

   ```bash
   sudo vim /etc/ssh/ssh_config
   ```

   Uncomment the following line:

   ```text
   PasswordAuthentication yes
   ```

   <kbd>Escape</kbd> <kbd>:</kbd> <kbd>w</kbd> <kbd>q</kbd> <kbd>Enter</kbd>

## Ansible Control Node

1. Open a terminal, on your Ansible Control Node.

1. If you haven't setup SSH on the control node:

   ```shell
    ssh-keygen
    ```

1. Enter the following command, replacing `un` with the client username and `ip` with the client's IP Address.

   ```shell
   ssh-copy-id un@ip 
   ```

1. Accept the Linux client's fingerprint, enter the password, and then select **Enter**.