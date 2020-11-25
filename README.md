# Ansible Collection - cisco.dnac

## Ansible Modules for DNA Center

The dnacenter-ansible project provides an Ansible collection for managing and automating your Cisco DNA Center environment. It consists of a set of modules and roles for performing tasks related to DNA Center.

This collection has been tested and supports Cisco DNA Center 2.1.1.

*Note: This collection is not compatible with versions of Ansible before v2.8.*

## Requirements
Ansible v2.9 or newer

## Install
Ansible must be installed
```
sudo pip install ansible
```

Install the collection
```
ansible-galaxy collection install cisco.dnac
```
## Use
First, define a `hosts.yml` file where you specify your DNA Center servers and their associated credentials:
```
dnac_servers:
  hosts:
    dnac_server:
      dnac_host: 10.10.10.10
      dnac_port: 443
      dnac_username: myuser
      dnac_password: mypass
```

Then, create a playbook `myplaybook.yml` referencing your hosts file and specifying the full namespace path to the module, plugin and/or role:
```
- hosts: dnac_servers
  gather_facts: no
  tasks:
  - name: Create tag
    cisco.dnac.tag:
      state: present
      description: My Tag
      name: MyNewTag
```

Execute the playbook:
```
ansible-playbook -i hosts.yml myplaybook.yml
```
In the `playbooks` directory you can find more examples and use cases.


## Update
Getting the latest/nightly collection build

Clone the dnacenter-ansible repository.
```
git clone https://github.com/cisco-en-programmability/dnacenter-ansible.git
```

Go to the dnacenter-ansible directory
```
cd dnacenter-ansible
```

Pull the latest master from the repo
```
git pull origin master
```

Build and install a collection from source
```
ansible-galaxy collection build --force
ansible-galaxy collection install cisco-dnac-* --force
```

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement or need a new module, please open an issue or create a PR against the [Cisco DNA Center Ansible collection repository](https://github.com/cisco-en-programmability/dnacenter-ansible.git/issues).