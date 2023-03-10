# Ansible weareinteractive.ufw role

[![Build Status](https://img.shields.io/travis/weareinteractive/ansible-ufw.svg)](https://travis-ci.org/weareinteractive/ansible-ufw)
[![Galaxy](http://img.shields.io/badge/galaxy-weareinteractive.ufw-blue.svg)](https://galaxy.ansible.com/weareinteractive/ufw)
[![GitHub Tags](https://img.shields.io/github/tag/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)
[![GitHub Stars](https://img.shields.io/github/stars/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)

> `weareinteractive.ufw` is an [Ansible](http://www.ansible.com) role which:
>
> * installs ufw
> * configures ufw
> * configures ufw rules
> * configures service

## Installation

Using `ansible-galaxy`:

```shell
$ ansible-galaxy install weareinteractive.ufw
```

Using `requirements.yml`:

```yaml
- src: weareinteractive.ufw
```

Using `git`:

```shell
$ git clone https://github.com/weareinteractive/ansible-ufw.git weareinteractive.ufw
```

## Dependencies

* Ansible >= 2.10

## Variables

Here is a list of all the default variables for this role, which are also available in `defaults/main.yml`.

| Variable             | Default     | Comments (type)                                   |
| :---                 | :---        | :---                                              |
| ufw_allow_tcp_ports | | List of tcp ports/services which are open to the public |
| ufw_allow_udp_ports | | List of udp ports/services which are open to the public |
| ufw_allow_interfaces | | List of interfaces through which access is generally allowed |
| ufw_ports_acl | | List of dictionary structure containing rule configuration. Structure is documented below. |


ufw_ports_acl structure
-----------------------

```yaml
ufw_ports_acl:
  - name: SSH
    port: 22
    ips: "{{ firewall_ssh_ips }}"
  - name: SNMP
    port: 161
    proto: UDP
    ips: "{{ firewall_snmp_ips }}"
```

| Variable             | Default     | Comments (type)                                   |
| :---                 | :---        | :---                                              |
| name | | A name identifying the rule |
| port | | Destination port |
| proto | | Protocol to be used |
| ips | | List of source IP addresses |






```yaml
---
# Start the service and enable it on system boot
ufw_enabled: true

# List of packages to install
ufw_packages: ["ufw"]

# The service name
ufw_service: ufw

# List of rules to be applied
# see https://docs.ansible.com/ansible/latest/collections/community/general/ufw_module.html for documentation
ufw_rules:
  - rule: allow
    to_port: 22

# Manage the configuration file
ufw_manage_config: false

# Configuration object passed to the configuration file
ufw_config:
  IPV6: "yes"
  DEFAULT_INPUT_POLICY: DROP
  DEFAULT_OUTPUT_POLICY: ACCEPT
  DEFAULT_FORWARD_POLICY: DROP
  DEFAULT_APPLICATION_POLICY: SKIP
  MANAGE_BUILTINS: "no"
  IPT_SYSCTL: /etc/ufw/sysctl.conf
  IPT_MODULES: ""

# Path to the configuration file
ufw_config_file: /etc/default/ufw

ufw_allow_tcp_ports:
  - 80
  - 443
  - ssh

ufw_allow_udp_ports:
  - 161

ufw_allow_interfaces:
  - openvpntun+

firewall_ssh_ips: "{{ firewall_ssh_ips_default }}"
firewall_ssh_ips_default:
  - x.x.x.x
  - y.y.y.y

firewall_snmp_ips: "{{ firewall_snmp_ips_default }}"
firewall_snmp_ips_default:
  - a.a.a.a
  - b.b.b.b

ufw_ports_acl:
  - name: SSH
    port: 22
    ips: "{{ firewall_ssh_ips }}"
  - name: SNMP
    port: 161
    proto: UDP
    ips: "{{ firewall_snmp_ips }}"


```

## Handlers

These are the handlers that are defined in `handlers/main.yml`.

```yaml
---

- name: reset ufw
  community.general.ufw:
    state: reset

- name: reload ufw
  community.general.ufw:
    state: reloaded
  when: ufw_enabled | bool

```


## Usage

This is an example playbook:

```yaml
# @see https://docs.ansible.com/ansible/latest/collections/community/general/ufw_module.html#examples
---

- hosts: all
  become: true
  roles:
    - weareinteractive.ufw
  vars:
    ufw_rules:
      # Set loggin
      - logging: "full"
      # Allow OpenSSH
      - rule: allow
        name: OpenSSH
      # Delete OpenSSH rule
      - rule: allow
        name: OpenSSH
        delete: true
      # Allow all access to tcp port 80
      - rule: allow
        to_port: '80'
        proto: tcp
    # Manage the configuration file
    ufw_manage_config: true
    # Configuration object passed to the configuration file
    ufw_config:
      IPV6: "yes"
      DEFAULT_INPUT_POLICY: DROP
      DEFAULT_OUTPUT_POLICY: ACCEPT
      DEFAULT_FORWARD_POLICY: DROP
      DEFAULT_APPLICATION_POLICY: SKIP
      MANAGE_BUILTINS: "no"
      IPT_SYSCTL: /etc/ufw/sysctl.conf
      IPT_MODULES: ""

```


## Testing

```shell
$ git clone https://github.com/weareinteractive/ansible-ufw.git
$ cd ansible-ufw
$ make test
```

## Contributing
In lieu of a formal style guide, take care to maintain the existing coding style. Add unit tests and examples for any new or changed functionality.

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

*Note: To update the `README.md` file please install and run `ansible-readme`:*

```shell
$ gem install ansible-readme
$ ansible-readme
```

## License
Copyright (c) We Are Interactive under the MIT license.
