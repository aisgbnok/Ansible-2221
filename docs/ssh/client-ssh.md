# Configuring SSH on Client Devices

## Windows

To allow remote SSH connections, you need to start the sshd service on the Windows managed node.
By default the sshd service is set to start manually.
To allow remote SSH connections each time your device is rebooted, run the following commands from an elevated PowerShell prompt:

```powershell
# Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service sshd
```

## Linux
