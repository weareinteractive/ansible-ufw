# Ansible franklinkim.ufw role

[![Build Status](https://img.shields.io/travis/weareinteractive/ansible-ufw.svg)](https://travis-ci.org/weareinteractive/ansible-ufw)
[![Galaxy](http://img.shields.io/badge/galaxy-weareinteractive.ufw-blue.svg)](https://galaxy.ansible.com/weareinteractive/ufw)
[![GitHub Tags](https://img.shields.io/github/tag/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)
[![GitHub Stars](https://img.shields.io/github/stars/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)

> `franklinkim.ufw` is an [Ansible](http://www.ansible.com) role which:
>
> * installs ufw
> * configures ufw
> * configures ufw rules
> * configures service

## Installation

Using `ansible-galaxy`:

```shell
$ ansible-galaxy install franklinkim.ufw
```

Using `requirements.yml`:

```yaml
- src: franklinkim.ufw
```

Using `git`:

```shell
$ git clone https://github.com/weareinteractive/ansible-ufw.git franklinkim.ufw
```

## Dependencies

* Ansible >= 2.4

## Variables

Here is a list of all the default variables for this role, which are also available in `defaults/main.yml`.

```yaml
---
# ufw_rules:
#   - { [port: ""] [rule: allow] [proto: any] [from_ip: any] [to_ip: any] }
# ufw_applications:
#   - { name: OpenSSH [rule: allow, from_ip: any] }
#

# package name (version)
# depricated: `ufw_package` will be removed in future releases! Use `ufw_packages`
ufw_package: ufw
# added to support systems where ufw packages are split up
ufw_packages:
  - "{{ ufw_package }}"
# list of rules
ufw_rules: [{ port: 22, rule: allow }]
# list of profiles located in /etc/ufw/applications.d
ufw_applications: []
# /etc/defaut/ufw settings
ufw_ipv6: "yes"
ufw_default_input_policy: DROP
ufw_default_output_policy: ACCEPT
ufw_default_forward_policy: DROP
ufw_default_application_policy: SKIP
# firewall state: enabled | disabled
ufw_state: enabled
ufw_logging: "off"
# always reset the firewall
ufw_reset: yes

```

## Handlers

These are the handlers that are defined in `handlers/main.yml`.

```yaml
---

- name: reload ufw
  ufw:
    state: reloaded
  when: ufw_state == 'enabled'

```


## Usage

This is an example playbook:

```yaml
---

- hosts: all
  roles:
    - franklinkim.ufw
  vars:
    ufw_rules:
      - { port: 22, rule: allow }
      - { port: 80, rule: allow }
      - { from_ip: '127.0.0.1/8' }
      - { from_ip: '127.0.42.0/24', rule: deny }
    ufw_default_forward_policy: ACCEPT
    ufw_logging: full
    ufw_applications:
     - { name: "OpenSSH" }

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

*Note: To update the `README.md` file please install and run `ansible-role`:*

```shell
$ gem install ansible-role
$ ansible-role docgen
```

## License
Copyright (c) We Are Interactive under the MIT license.
