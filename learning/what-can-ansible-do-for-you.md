# What can Ansible Do for You?

## Remote Management

Ansible calls upon the secure shell to access remote systems.

You need the get  `id_rsa.pub` ssh key from the control node and paste it into the `authorized_keys` file on managed nodes.

```shell
cd ~/.ssh
vim authorized_keys
```

## Orchestration

Orchestration is not automation.
Automation is a single task.
Orchestration is the management of many automated tasks.
This might be complicated because of the complex ordering and dependencies of these tasks.

`orchestrate.yml`
```yaml
---
- name: Orchestration Example
  hosts: logicservers
  serial: 1 # Makes sure that all the tasks run against one logicserver before moving to the next server.

  tasks:
    - name: Shutdown Server
      debug:
        msg: "Shutdown {{ inventory_hostname }}"

    - name: Upgrade Server
      debug:
        msg: "Upgrade {{ inventory_hostname }}"

    - name: Start Server
      debug:
        msg: "Start {{ inventory_hostname }}"

    - name: Verify Server
      debug:
        msg: "Verify {{ inventory_hostname }}"
```
\
`myhosts`
```text
[logicservers]
server1   ansible_host=127.0.0.1  ansible_connection=local  deprecation_warnings=false
server2   ansible_host=127.0.0.2  ansible_connection=local
server3   ansible_host=127.0.0.3  ansible_connection=local
server4   ansible_host=127.0.0.4  ansible_connection=local
```
Run the playbook with the custom inventory:
```shell
ansible-playbook orchestrate.yml -i myhosts
```

## System Configuration Management

- Ansible was designed to be minimal in nature
- Ansible is agentless
- Ansible uses SSH
- Ansible is state driven
  - Determines the state of machines and then takes actions depending on their states.
- Idempotent
  - We can safely execute actions against systems and not have a detrimental effect on those systems.

In this example we will show Ansible's state-driven design.

`ntp.yml`
```yaml
---
- name: NTP Configuration
  hosts: all
  become: yes

  tasks: 
    - name: Ensure NTP is Installed
      apt:
        name:
          - ntp
        state: present # This ensures that NTP is present. If it isn't then ntp will be installed.

    - name: Ensure NTP is started now and at boot
      service:
        name: ntp
        state: started
        enabled: yes
```

Upon executing the playbook you will get a `changed` status if NTP needed to be installed or an `ok` status if it was already installed.

## React to configuration changes

Ansible needs to be able to react to changes with "hooks". Here is an example:

`change.yml`
```yaml
---
- name: React with Change Example
  hosts: webservers
  serial: 1

  tasks:
    - name: Install nginx
      debug:
        msg: "Install nginx on: {{ inventory_hostname }}"

    - name: Upgrade nginx
      debug:
        msg: "Upgrade nginx on: {{ inventory_hostname }}"

    - name: Configure nginx
      debug:
        msg: "Start nginx on: {{ inventory_hostname }}"
      notify: restart nginx
      changed_when: True # This will imitate a "change" event.

    - name: Verify nginx
      debug:
        msg: "Verify nginx on: {{ inventory_hostname }}"

  handlers:
    - name: restart nginx
      debug:
        msg: "CALLED HANDLER FOR RESTART"
```

```shell
ansible-playbook change.yml -i myhosts
```

## Infrastructure Management

Ansible can not only help with configuration management, but can also build and manage infrastructures.

We can use playbooks to build our infrastructures from the ground up.

With dynamic inventories we can reflect new devices.

Playbooks can provision underlying hardware for us.

Ansible does a great job because it is primed to manage the virtualization on top of that physical infra.

Ansible can make sure physical components are in place and then automating the virtualization on top of the physical components.

Ansible has a wide range of support for Operating Systems which is also beneficial.

## Repeating Tasks Across Fleets

- Ad hoc tasks are great
- Manipulate execution strategies and forks

### Strategies & Forks
Going back to the `change.yml` playbook from earlier we can choose to instead take a specific strategy instead of using the `serial`.

`change.yml`
```yaml
---
- name: React with Change Example
  hosts: webservers
  strategy: free # Do this as quickly as possible, dictated by forks number.
```

For example, this will allow 30 forks to be configured at a time.
```shell
ansible-playbook change.yml -f 30 -i myhosts
```