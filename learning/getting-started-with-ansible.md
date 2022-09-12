# Getting Started with Ansible

## Ansible Structure

The Ansible control node is the system that has Ansible installed and manages other nodes.

You need to have an Ansible inventory.
The Ansible inventory file is by default the `hosts` file found at `/etc/ansible/hosts`.

The `ansible.cfg` file is an important file.
It includes a bunch of parameters and configurations for modifying the default Ansible behavior.

Ansible playbooks are basically Ansible scripts.
They are written in YAML.
They contain some basic data for defining the playbook, and then they include tasks that execute on the specified nodes.


To run an Ansible playbook:

```shell
ansible-playbook sample.yml
```

An ad hoc Ansible command can be performed whenever you want:

```shell
ansible myservers -m ping
```

## Installing Ansible

[Follow Ansible's guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

the pip3 version is best, the ppa version (specific) is also fine. Though it installed the release candidate for me. best to use the pip3 install.

> **Note**\
> The pip install does not provide you with a default `ansible.cfg` file.
> IInstalling using OS package manager will.

```shell
sudo apt upgrade
```

```shell
sudo apt install python3 python3-pip
```
```shell
python3 -m pip install --user ansible
```

> **Note**\
> Must add Ansible `~/.local/bin` to your `$PATH` env var.
> https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/

```shell
ansible --version
```

