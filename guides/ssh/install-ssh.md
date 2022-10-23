# Installing SSH

## Windows

### Requirements

- Windows Server 2019 or Client version 1809 and later.
- An account that is a member of the built-in Administrators group.

### Check if OpenSSH is Installed

#### OpenSSH Windows Capability

To check if OpenSSH is already installed on your Windows device, run the following command in an elevated PowerShell prompt:

> **Warning**\
> Must be using an Elevated PowerShell Prompt!

> **Note**\
> You can press <kbd>Tab</kbd> to autocomplete in PowerShell.

```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

Both OpenSSH Client and Server should have a state of `Installed`, if not continue to the installation guide.

### Install OpenSSH on Windows

#### If your Windows device doesn't have OpenSSH installed and is running Windows version 1809 or later:

1. Open Windows Settings, select **Apps**, then select **Optional Features**, or go to [`ms-settings:optionalfeatures`](ms-settings:optionalfeatures) in a browser.
1. At the top of the page, select **Add a feature**.
1. Search **SSH** to find the **OpenSSH Server** feature.
1. Select **OpenSSH Server** and **OpenSSH Client** if available, and then select **Install**.

#### If your Windows installation is older than version 1809:

1. Go to the **[Win32-OpenSSH releases on GitHub](https://github.com/PowerShell/Win32-OpenSSH/releases)**.
1. Under the **Assets** section of the latest release, download the appropriate MSI installer for your device architecture `Win32` or `Win64`.
1. Run the **Microsoft Windows Installer (MSI)** and follow its steps to complete installation.
1. In an elevated PowerShell prompt, run the following command to add OpenSSH to the System Path.
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path",[System.EnvironmentVariableTarget]::Machine) + ';' + ${Env:ProgramFiles} + '\OpenSSH', [System.EnvironmentVariableTarget]::Machine)
   ```
1. Restart any PowerShell prompts to reload System Path.
1. Run the following PowerShell command to verify that OpenSSH was successfully installed.
   ```powershell
   ssh -V
   ```
   ```powershell
   Get-Service -Name ssh*
   ```

## Linux

> **Note**\
> Linux traditionally comes with OpenSSH installed by default.
> Skip to the [Configuring SSH on Client Devices](client-ssh.md#linux) or [Configuring SSH on Server Devices](server-ssh.md#linux) guide.

1. Ensure the `openssh-server` package is installed using your distribution's package manager.
   ```shell
   sudo apt install openssh-server
   sudo apt install openssh-client
   ```
   ```shell
   sudo yum install openssh-server
   ```
   > **Note**\
   > Some distributions like Kali require you to regenerate the default SSH keys.
1. Regenerate your distribution's default SSH keys.
   ```shell
   sudo dpkg-reconfigure openssh-server
   ```
1. Enable the SSH service.
    ```shell
   sudo systemctl status ssh.service
   ```
1. (Optional) Enable password based SSH authentication.
   ```shell
   sudo vim /etc/ssh/ssh_config
   ```
   Uncomment the following line:
      ```text
   PasswordAuthentication yes
   ```
   Save the `ssh_config` file: <kbd>Escape</kbd><kbd>:</kbd><kbd>w</kbd><kbd>q</kbd><kbd>Enter</kbd>.