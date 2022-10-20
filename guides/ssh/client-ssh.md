# Configuring SSH on Client Devices

## Windows

To allow remote SSH connections, you need to start the sshd service on the Windows managed node.
By default, the sshd service is set to start manually.
To allow remote SSH connections each time your device is rebooted, run the following commands from an elevated PowerShell prompt:

```powershell
# Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service sshd
```

## Linux

> **Note**\
> Linux traditionally comes with OpenSSH configured by default.
> Skip to [Configuring SSH on Server Devices](server-ssh.md#linux) guide.

### Check if OpenSSH is Running

To check if OpenSSH is already running on your Linux device, run the following command in a terminal:

```shell
systemctl status sshd
```

### Start OpenSSH

To start OpenSSH on your Linux device, run the following command in a terminal:

```shell
sudo systemctl enable sshd --now
```