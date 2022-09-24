# Configuring SSH on Client Devices

## Windows

### Generate SSH Key

To use key-based authentication, you first need to generate public/private key pairs for your client.
To generate key files using the RSA algorithm, run the following command from a PowerShell prompt on your client:

> **Warning**\
> In my limited testing, it seems that the Windows client must use RSA to achieve passwordless SSH.

```powershell
ssh-keygen
```

You can press Enter to accept the default, or specify a path and/or filename where you would like your keys to be generated.
At this point, you'll be prompted to use a passphrase to encrypt your private key files.

Now you have a public/private RSA key pair in the location specified.
The `.pub` files are public keys, and files without an extension are private keys.

### Start SSHD

By default the sshd service is set to start manually.
To allow remote SSH connections each time your device is rebooted, run the following commands from an elevated PowerShell prompt:

```powershell
# Set the sshd service to be started automatically
Get-Service -Name sshd | Set-Service -StartupType Automatic

# Now start the sshd service
Start-Service sshd
```

## Linux

