# Ansible Collection: cisco.dnac

## Overview

The cisco.dnac Ansible Collection enables enterprise automation and management of Cisco CATALYST Center environments. It provides modules that interact with Cisco CATALYST Center APIs to automate provisioning, configuration, and operational workflows.

This collection is available on both [Ansible Galaxy](https://galaxy.ansible.com/cisco/dnac) and [Red Hat Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/dnac/).

## Compatibility Matrix

The following table shows the supported versions.

| Cisco DNA Center version | Ansible cisco.dnac version | Python dnacentersdk version |
|--------------------------|------------------------------|-------------------------------|
|2.3.5.3|6.13.3|2.6.11|
|2.3.7.6|6.25.0|2.8.3|
|2.3.7.7|6.30.2|2.8.6|
|2.3.7.9|6.33.2|2.8.6|
|3.1.3.0|6.45.0|2.10.6|
|3.1.6.0|6.47.x|2.11.x|

If your Ansible collection is older please consider updating it first.

Notes:

1. The "Python 'dnacentersdk' version" column lists the minimum recommended SDK used during testing; later SDK releases are usually compatible.
2. The "Cisco DNA Center version" column has the value of the `version` you should use for the Ansible collection.

## Requirements

- Python >= 3.9
- [dnacentersdk](https://github.com/cisco-en-programmability/dnacentersdk) (see Compatibility Matrix for tested versions)
- ansible-core >= 2.15

> **Note:** ansible-core is provided through Red Hat Ansible Automation Platform Execution Environments or can be installed via standard enterprise channels. Manual installation is not required for certified environments.

## Installation

Install the collection from Ansible Galaxy:

```bash
ansible-galaxy collection install cisco.dnac
```

To upgrade to the latest version:

```bash
ansible-galaxy collection install cisco.dnac --upgrade
```

Install the Python SDK:

```bash
pip install dnacentersdk
```

## Using this Collection

Connection details can be provided via environment variables or Ansible variable files. See the [examples directory](https://github.com/cisco-en-programmability/dnacenter-ansible/tree/main/playbooks) for sample playbooks and variable files.

### Using environment variables

First, export the environment variables where you specify your CATALYST Center credentials as ansible variables:

```bash
export DNAC_HOST=<A.B.C.D>
export DNAC_PORT=443 # optional, defaults to 443
export DNAC_USERNAME=<username>
export DNAC_PASSWORD=<password>
export DNAC_VERSION=3.1.6.0 # optional, see the Compatibility Matrix
export DNAC_VERIFY=False # optional, defaults to True
export DNAC_DEBUG=False # optional, defaults to False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks/hosts)) file that uses `[dnac_servers]` with your Cisco CATALYST Center Settings:

```ini
[dnac_servers]
dnac_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks/tag.yml)) specifying the full namespace path to the module, plugin and/or role. The module will read connection details from the environment variables above:

```yaml
- hosts: dnac_servers
  gather_facts: false
  tasks:
  - name: Create tag with name "MyNewTag"
    cisco.dnac.tag:
      state: present
      description: My Tag
      name: MyNewTag
    register: result
```

Execute the playbook:

```bash
ansible-playbook -i hosts myplaybook.yml
```

### Using vars_files

First, define a `credentials.yml` ([example](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks/vars/credentials.template)) file where you specify your CATALYST Center credentials as Ansible variables:

```yaml
---
# DNA Center connection variables
dnac_host: <A.B.C.D>
dnac_port: 443
dnac_username: <username>
dnac_password: <password>
dnac_version: 3.1.6.0
dnac_verify: False
dnac_debug: False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks/hosts)) file that uses `[dnac_servers]` with your Cisco CATALYST Center Settings:

```ini
[dnac_servers]
dnac_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks/tag.yml)) referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:

```yaml
- hosts: dnac_servers
  vars_files:
    - playbooks/credentials.yml
  gather_facts: false
  tasks:
    - name: Create tag using vars_file
      cisco.dnac.tag:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        state: present
        description: My Tag
        name: MyNewTag
      register: result
```

Execute the playbook as usual:

```bash
ansible-playbook -i hosts myplaybook.yml
```

In the `playbooks` [directory](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/playbooks) you can find more examples and use cases.

## Use Cases

This collection supports automation scenarios such as:

- Automating device and site configuration through Cisco CATALYST Center APIs.
- Managing tags, sites, templates, and policies programmatically.
- Querying inventory and operational data for reporting and validation workflows.
- Integrating Cisco CATALYST Center operations into CI/CD or ITSM workflows.
- Standardizing repeatable infrastructure changes using playbooks.

## Testing

This collection is validated against the following environments:

- Cisco DNA Center: 2.3.5.3, 2.3.7.6, 2.3.7.9, 3.1.3.0, 3.1.6.0
- ansible-core: >= 2.15
- Python: >= 3.9

Known limitations and compatibility notes are documented in the [changelog](https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/changelogs/changelog.yaml). For platform-specific issues, consult the official documentation or open a support case as appropriate.

## Contributing

Contributions are welcome. Please open issues or pull requests via the [Cisco DNA Center Ansible collection repository](https://github.com/cisco-en-programmability/dnacenter-ansible/issues). All contributors must adhere to the project's Code of Conduct.


## Code of Conduct

This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Support

This collection is available on both Ansible Galaxy and Red Hat Automation Hub.

For certified content obtained from Red Hat Automation Hub, support is provided through Red Hat Ansible Automation Platform according to your subscription agreement.

For content obtained from Ansible Galaxy, community support may be available via:
- https://forum.ansible.com/
- https://github.com/cisco-en-programmability/dnacenter-ansible/issues

Please consult your platform documentation for support eligibility and procedures.

---


## Release Notes and Roadmap

Release notes are maintained in the public changelog:
https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/changelogs/changelog.yaml

This collection follows [Semantic Versioning](https://semver.org/). For roadmap information, refer to the repository or contact Cisco for enterprise roadmap details.

---


## Related Information

- https://github.com/cisco-en-programmability/dnacentersdk
- https://docs.ansible.com/ansible/latest/user_guide/collections_using.html
- https://github.com/cisco-en-programmability/dnacenter-ansible

---


## License

This collection is licensed under the Cisco Sample Code License.

The full license text is available at:
https://github.com/cisco-en-programmability/dnacenter-ansible/blob/main/LICENSE

The license is included in the distributed collection artifact.
