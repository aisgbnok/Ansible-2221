# Install SSH on Windows

## Requirements

- Windows client running build 1809 and later.
- Sign into an Administrator account on the Windows device.

## Install SSH on Windows Client

### Install SSH

1. Open Settings, select **Apps**, then select **Optional Features**, or open `ms-settings:optionalfeatures` in a browser.
1. At the top of the page, select **Add a feature**, then:
   1. Search **ssh**, and find **OpenSSH Server**
   1. Select **OpenSSH Server**, and then select **Install**.
   1. Do the same for **OpenSSH Client** if it is not already installed.
1. Run the following commands from an elevated PowerShell prompt:

```powershell
# Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service sshd
```

### Generate SSH key

Run the following command from a PowerShell prompt on your client:

```powershell
ssh-keygen -t ed25519
```

1. Select **Enter**, to keep the default save path.
1. Enter a password and generate an ssh key.

To start the `ssh-agent` service each time your computer is rebooted, and use `ssh-add` to store the private key run the following commands from an elevated PowerShell prompt:

```powershell
# By default the ssh-agent service is disabled. Configure it to start automatically.
# Make sure you're running as an Administrator.
Get-Service ssh-agent | Set-Service -StartupType Automatic

# Start the service
Start-Service ssh-agent

# This should return a status of Running
Get-Service ssh-agent

# Now load your key files into ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

## Ansible Control Node

1. Open a terminal, on your Ansible Control Node.
1. If you haven't setup SSH on the control node:

   ```bash
    ssh-keygen
    ```

1. Enter the following command, replacing `un` with the client username and `ip` with the client's IP Address.

   ```bash
   ssh-copy-id un@ip 
   ```

1. Accept the Windows Client's fingerprint, enter the password, and then select **Enter**.