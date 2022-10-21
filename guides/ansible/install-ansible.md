# Installing Ansible

## Ubuntu

> **Note**\
> You can press <kbd>Tab</kbd> to autocomplete in Ubuntu Terminal.

```shell
sudo apt upgrade
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

## CentOS

> **Warning**\
> Make sure not to update any service such as Apache/HTTP!
> That goes against the rules!

```shell
sudo yum install epel-release
sudo yum upgrade
sudo yum install ansible
```