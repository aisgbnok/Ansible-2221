# What is Ansible?

## Basics

Ansible is a task execution engine. It can run on a variety of different systems. It can reach out an execute tasks on the local or a remove system.

"Control Node" - Ansible System that controls other systems.

Ansible is clientless, meaning you don't have to install client software to run ansible.
Ansible uses SSH to make connections to remote systems and configure them.
However, you have to set up the SSH so that it functions properly between Ansible and remote nodes.

Ansible scripts are written in human-readable text files (YAML).
Ansible itself is written in the Python programming language.

Ansible is very effective at maintaining, monitoring, operating massive fleets of systems.

> Graphical UX
> Red Hat Tower (Paid)
> AWX (Open-Source)

"Ad Hoc Command"

```shell
ansible myservers -m ping
```

## Life before Ansible

### Before
- Server admins were siloed
  - siloed means separation between server admins and other IT admins
- "By hand" management
  - log into the OS by hand and manage the configurations
- Server tools were developed to help with management
  - Still a manual configuration approach
  - Tools became more sophisticated, and creating a larger learning curve
- Virtualization drove the push for automation
  - Many virtual servers could be quickly established
  - By hand management was still an issue

### After
- Growth of DevOps
- Server teams can work side by side with development staff
- Provision architectures an applications with ease and transparency.

## Ansible History & Red Hat

Ansible is open-source and free. However, it was purchased by Red Hat.

- Ansible was released in 2012 by Michael DeHaan.
- In 2015 Red Hat purchased Ansible Inc.
  - Ansible and it's resources are open-source.
  - Red Hat has wrapped some paid services around Ansible.
    - Ansible Consulting, Ansible Tower, etc.
- 