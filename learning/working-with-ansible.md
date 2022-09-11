# Working with Ansible

## Hosts and Variables

Example Ansible Inventory file

```text
[southeast]
localhost                   ansible_connection=local
other1.example.com          ansible_connection=ssh              ansible_user=ubuntu

[northeast]
other2.example.com
10.10.100.10

[southwest]
10.10.200.10

[east:children]
southeast
northeast
```

To the right of each listing you can have variables for example `ansible_connection`.
You can also have subgroups like `[east:children]`, when referencing `east` all hosts in the subgroups will be executed upon.
By default, an `all` grouping is already created that executes upon all hosts in the inventory file.

## Working with code in Ansible

You can find collections and modules in the [Collections Index](https://docs.ansible.com/ansible/latest/collections/index.html).

Here is another ad hoc example: 

```shell
ansible localhost -m find -a "paths=Downloads file_type=file"
```

## Working with playbooks in Ansible

`first.yml`

```yaml
---
- name: My First Playbook
  hosts: localhost

  tasks:
    - name: Test Reachability
      ping:

    - name: Install Stress
      homebrew:
        name: stress
        state: present
```
To run an ansible playbook:
```shell
ansible-playbook first.yml
```
To get additional information add the `-v` parameter
```shell
ansible-playbook first.yml -v
```

## Ansible Cfg file

```text
[defaults]
# Use the YAML callback plugin.
stdout_callback = yaml
# Use the stdout_callback when running ad-hoc commands.
bin_ansible_callbacks = True
interpreter_python = auto_silent
```


