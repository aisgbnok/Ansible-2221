# Building Great Tasks

## Using Host Groups

`hosts`
```text
10.0.1.[1:3] # Range of IP Addresses

[all_hosts]
# Aliases ansible_ssh_host=IP_Address
target1 ansible_ssh_host=10.0.1.239
target2 ansible_ssh_host=10.0.1.94
target3 ansible_ssh_host=10.0.1.252
target4 ansible_ssh_host=10.0.1.133
target5 ansible_ssh_host=10.0.1.4
target6 ansible_ssh_host=10.0.1.82

[webservers]
target1
target2
target3

[dbservers]
target4
target5
target6

[backupservers]
target6 backup_file=/tmp/test1 # We set a variable

[all:vars]
# This variable applies to all systems
temp_file=/tmp/test2

[webservers:vars]
# Variables at the webservers level
temp_file=/tmp/test3
```

The main takeaway is the host groups and how convenient they are.

`webservers.yml`
```yaml
---
- hosts: webservers
  become: yes

  tasks:
    - name: Uninstall testpackage and sync apt index
      apt:
        name: testpackage
        state: absent
        update_cache: yes
```
```shell
ansible-playbook webservers.yml
```

## Using Tags

Tags can be used to specify what tasks to run.

`tags.yml`
```yaml
---
- hosts: webservers
  become: yes

  tasks:
    - name: Install Apache2
      apt:
        name: apache2
        state: present
        update_cache: yes
        cache_valid_time: 3600
      tags: apache2

    - name: Install NTP
      apt:
        name: ntp
        state: present
      tags: ntp

    - name: Start NTP
      service: name=ntp state=started enabled=yes
      tags: ntp_start
```

To use the tags you can specify what tag you want to run.

```shell
ansible-playbook tags.yml --tags ntp
```

To see all the tags inside a playbook you can use the `--list-tags` parameter.

```shell
ansible-playbook tags.yml --list-tags
```

To run everything except a specific tag:

```shell
ansible-playbook tags.yml --skip-tags ntp_start
```

## Running tasks against localhost (control node)

`controlnode.yml`
```yaml
---
- hosts: localhost

  tasks:
    - name: Get local information
      debug:
        var: hostvars[inventory_hostname]
        verbosity: 1
```
```shell
ansible-playbook controlnode.yml -v
```

---

`conn_controlnode.yml`
```yaml
---
- hosts: localhost
  connection: local

  tasks:
    - name: Get local information
      debug:
        var: hostvars[inventory_hostname]
        verbosity: 1
```
`connection: local` bypasses the SSH and just directly communicates with the local node.
Improves performance because there is less overhead now that SSH is not used.

```shell
ansible-playbook conn_controlnode.yml -v
```

## Using the command line to control execution

Reference the `tags.yml` from above.
```shell
ansible-playbook tags.yml --start-at-task 'Install NTP'
```
You must use the exact name for the task.

### Interactive

This lets you interactively step through the playbook and choose what to execute.

```shell
ansible-playbook tags.yml --step
```

Ansible is idempotent which means we can run a playbook on systems over and over again without producing disastrous results.

## Variables in the Inventory File

`hosts`
```text
10.0.1.[1:3] # Range of IP Addresses

[all_hosts]
target1 ansible_ssh_host=10.0.1.239
target2 ansible_ssh_host=10.0.1.94
target3 ansible_ssh_host=10.0.1.252
target4 ansible_ssh_host=10.0.1.133
target5 ansible_ssh_host=10.0.1.4
target6 ansible_ssh_host=10.0.1.82

[webservers]
target1
target2
target3

[dbservers]
target4
target5
target6

[backupservers]
target6 backup_file=/tmp/test1

[all:vars]
temp_file=/tmp/test2

[webservers:vars]
temp_file=/tmp/test3
```
For example, we are assinging `backup_file=/tmp/test1` for `target6`.

```text
[all:vars]
temp_file=/tmp/test2
```
This will apply to all the systems.

How do we consume these variables?

`invvars.yml`
```yaml
---
- hosts: webservers

  tasks:
    - name: Create a file
      file:
        dest: "{{temp_file}}"
        state: "{{file_state}}"
      when: temp_file is defined
```

The `temp_file` variable is defined in the inventory `hosts` file.
The `file_state` will be passed in the command line.

```shell
ansible-playbook invvars.yml -e file_state=touch
```
This will create the file.

```shell
ansible-playbook invvars.yml -e file_state=absent
```
This will remove the file.

## Dynamic Inventories

Thanks to APIs we can have cloud providers provide a dynamic inventory file for us.

First we need to ensure that the appropriate software is installed on your control node.
For example AWS uses boto3.

Now create a directory called `inventory` at `/opt/ansible/`.
Create a `aws_ec2.yml` file.

Fill out the file for aws_access_key, and etc.

Now modify the Ansible config file. `/etc/ansible/ansible.cfg`.
Change the `[inventory]` section, and add `enable_plugins = aws_ec2` under that section.

To test:
```shell
ansible-inventory -i /opt/ansible/inventory/aws_ec2.yaml --list
```
Now it loads the hosts from AWS, and it will show you all the hosts.

## Using Templates

- Templates are often used with configuration management and automation
- Ansible uses Jinga2 for templating

`jinja2.j2`
```text
A message from your node:
 {{ inventory_hostname }}

Today's message:
{{ webserver_message }}
THANKS
```

`use_templates.yml`
```yaml
---
- name: Make sure Web Server is running
  hosts: webservers
  become: yes
  vars:
    webserver_message: "This is my clever message"

  tasks:
    - name: Start httpd
      service:
        name: apache2
        state: started

    - name: Create index.html using Jinja2
      template:
        src: jinja2.j2
        dest: /var/www/html/index.html
```

## Conditional Execution

- Key component that makes Ansible more useful
- Tags are nice, but using them exclusively is too manual and static.
- Conditional execution allows Ansible to take actions based on certain conditions.


- We can use Ansible facts, variables, and other criteria.
- The `when` statement is the recommended approach in Ansible
  - If the value evaluates to `True`, then the task will be executed.

`cond.yml`
```yaml
---
- hosts: all_hosts
  become: yes

  tasks:
    - name: Upgrade in Redhat
      when: ansible_os_family == "Redhat"
      yum: name=* state=latest

    - name: Upgrade in Debian
      when: ansible_os_family == "Debian"
      apt: upgrade=dist update_cache=yes
```

## Loops

`loop1.yml`
```yaml
---
- hosts: webservers
  become: yes
  vars:
    packages: [git, vim, ruby]

  tasks:
    - name: Install packages
      apt:
        name: "{{packages}}"
        state: latest
```

This will ensure everything under the packages variable is installed.

Using dictionaries we can also loop.

`loop2.yml`
```yaml
---
- hosts: webservers
  become: yes
  vars:
    websites:
      aws_sites:
        author: asequeira
        author_id: as001
      ms_sites:
        author: bsmith
        author_id: bs002
      google_sites:
        author: psmith
        author_id: ps001
      misc_sites:
        author: asequeira
        author_id: as001

  tasks:
    - name: Print data
      debug:
        msg: "Here are the results: {{item.value.author_id}}"
      with_dict: "{{websites}}"
      when: 'item.value.author_id == "as001"'
```

The `with_dict` statement ensures that we iterate through every item in the websites dictionary.
We also have the `when` statement that ensures we only run when the `item.value.author_id == "as001"`.

## Testing plays with check mode

- We often find ourselves testing things against actual equipment.
  - This isn't ideal or very good. Even though Ansible is safe/idempotent.
- Instead, we can take advantage of the check mode with Ansible for testing.
- However, this won't work if actual access to remote devices is required to test.

For example:
```shell
ansible-playbook use_templates.yml --check
```
The `--check` parameter is great for checking basic issues before actually executing on live machines.

> **Note**\
> Take advantage of this feature during development of scripts!