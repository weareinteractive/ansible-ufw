# Ansible Ufw Role

[![Build Status](https://img.shields.io/travis/weareinteractive/ansible-ufw.svg)](https://travis-ci.org/weareinteractive/ansible-ufw)
[![Galaxy](http://img.shields.io/badge/galaxy-franklinkim.supervisor-blue.svg)](https://galaxy.ansible.com/list#/roles/1382)
[![GitHub Tags](https://img.shields.io/github/tag/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)
[![GitHub Stars](https://img.shields.io/github/stars/weareinteractive/ansible-ufw.svg)](https://github.com/weareinteractive/ansible-ufw)

> `ufw` is an [ansible](http://www.ansible.com) role which:
>
> * installs ufw
> * configures ufw
> * configures ufw rules
> * configures service

## Installation

Using `ansible-galaxy`:

```
$ ansible-galaxy install franklinkim.ufw
```

Using `requirements.yml`:

```
- src: franklinkim.ufw
```

Using `git`:

```
$ git clone https://github.com/weareinteractive/ansible-ufw.git franklinkim.ufw
```

## Dependencies

* Ansible 1.9

## Variables

Here is a list of all the default variables for this role, which are also available in `defaults/main.yml`.

```
# ufw_rules:
#   - { [port: ""] [rule: allow] [proto: any] [from_ip: any] [to_ip: any] }
# ufw_applications:
#   - { name: OpenSSH [rule: allow] }
#

# package name (version)
ufw_package: ufw
# list of rules
ufw_rules: []
# list of profiles located in /etc/ufw/applications.d
ufw_applications: []
# /etc/defaut/ufw settings
ufw_ipv6: 'yes'
ufw_default_input_policy: DROP
ufw_default_output_policy: ACCEPT
ufw_default_forward_policy: DROP
ufw_default_application_policy: SKIP
# firewall state: enabled | disabled
ufw_state: enabled
ufw_logging: 'off'
```

## Example playbook

```
- host: all
  sudo: yes
  roles:
    - franklinkim.ufw
  vars:
    ufw_rules:
      - { ip: '127.0.0.1/8' }
      - { ip: '172.17.42.0/24', rule: deny }
      - { port: 80, rule: allow }
    ufw_default_forward_policy: ACCEPT
    ufw_applications:
     - { name: "OpenSSH" }
     - { name: "IMAP", rule: deny }
```

## Testing

```
$ git clone https://github.com/weareinteractive/ansible-ufw.git
$ cd ansible-ufw
$ vagrant up
```

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests and examples for any new or changed functionality.

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License
Copyright (c) We Are Interactive under the MIT license.
