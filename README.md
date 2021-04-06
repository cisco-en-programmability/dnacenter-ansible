# Ansible Collection - cisco.dnac

## Ansible Modules for DNA Center

The dnacenter-ansible project provides an Ansible collection for managing and automating your Cisco DNA Center environment. It consists of a set of modules and roles for performing tasks related to DNA Center.

This collection has been tested and supports Cisco DNA Center 2.1.1.

*Note: This collection is not compatible with versions of Ansible before v2.8.*

## Requirements
- Ansible >= 2.9
- [DNA Center SDK](https://github.com/cisco-en-programmability/dnacentersdk) v2.1.1 or newer
- Python >= 3.5, as the DNA Center SDK doesn't support Python version 2.x

## Install
Ansible must be installed
```
sudo pip install ansible
```

DNA Center SDK must be installed
```
sudo pip install dnacentersdk
```

Install the collection
```
ansible-galaxy collection install cisco.dnac
```
## Use
First, define a `credentials.yml` file where you specify your DNA Center credentials as ansible variables:
```
---
dnac_host: <A.B.C.D>
dnac_port: 443  # optional, defaults to 443
dnac_username: <username>
dnac_password: <password>
dnac_version: 2.1.1  # optional, defaults to 2.1.1
dnac_verify: False  # optional, defaults to True
```

Then, create a playbook `myplaybook.yml` referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:
```
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  tasks:
  - name: Create tag
    cisco.dnac.tag:
      dnac_host: "{{dnac_host}}"
      dnac_username: "{{dnac_username}}"
      dnac_password: "{{dnac_password}}"
      dnac_verify: "{{dnac_verify}}"
      state: present
      description: My Tag
      name: MyNewTag
```

Execute the playbook:
```
ansible-playbook -i hosts myplaybook.yml
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

## Attention macOS users

If you're using macOS you may receive this error when running your playbook:

```
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called.
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
ERROR! A worker was found in a dead state
```

If that's the case try setting this environment variable:
```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement or need a new module, please open an issue or create a PR against the [Cisco DNA Center Ansible collection repository](https://github.com/cisco-en-programmability/dnacenter-ansible/issues).

## Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Releasing, Versioning and Deprecation

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

New minor and major releases as well as deprecations will follow new releases and deprecations of the Cisco DNA Center product, its REST API and the corresponding Python SDK, which this project relies on. 
