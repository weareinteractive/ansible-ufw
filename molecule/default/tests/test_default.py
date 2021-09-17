# -*- coding: utf-8 -*-
# :Project:   weareinteractive.ufw ansible role - unittests
# :Created:   Fri 17 Sep 2021 21:31:46 CEST
# :Author:    Peter Warasin <peter@endian.com>
# :License:   GPLv2
# :Copyright: © 2021 Endian s.r.l.
#


"""
test_default.py - default unittest file.

This file contains unittests using testinfra used to test if the
ansible role does what we wanted that it would do.
"""

from types import SimpleNamespace
import pytest


@pytest.fixture(name="facts", scope="module")
def fixture_facts(host):
    """
    Set up the environment before the test.

    Setup environment by retrieving information from host which we
    need for out tests.

    :param value:     host
    :type  value:     the link to the testinfra host
    :return:          an object holding the retrieved ansible facts
    :rtype:           types.SimpleNamespace
    """
    ansible_facts = host.ansible("setup")["ansible_facts"]
    ret = SimpleNamespace()
    ret.host_os = ansible_facts["ansible_lsb"]["codename"]
    return ret


def test_service(host):
    """
    Tests if the firewalld service is enabled.

    This test method checks if the firewalld service is enabled.

    :param host:      the link to the testinfra host provided by fixture
    :type  host:      Host object
    """
    service = host.service("ufw")
    assert service.is_enabled


def test_ufw_allow_tcp_ports(host, facts):
    """
    Tests if the configured TCP ports are open.

    This test method checks if iptable rules do exist which open
    ports as configured in the inventory.

    :param value:     host
    :type  value:     the link to the testinfra host
    :param facts:     Retrieved ansible facts
    :type  facts:     types.SimpleNamespace
    """
    rules = host.iptables.rules()

    testrules = [
        "-A ufw-user-input -p tcp -m tcp --dport 80 -j ACCEPT",
        "-A ufw-user-input -p tcp -m tcp --dport 443 -j ACCEPT",
    ]

    for testrule in testrules:
        assert testrule in rules


def test_ufw_allow_udp_ports(host, facts):
    """
    Tests if the configured UDP ports are open.

    This test method checks if iptable rules do exist which open
    ports as configured in the inventory.

    :param value:     host
    :type  value:     the link to the testinfra host
    :param facts:     Retrieved ansible facts
    :type  facts:     types.SimpleNamespace
    """
    rules = host.iptables.rules()

    testrules = [
        "-A ufw-user-input -p udp -m udp --dport 161 -j ACCEPT",
        "-A ufw-user-input -p udp -m udp --dport 162 -j ACCEPT",
    ]

    for testrule in testrules:
        assert testrule in rules


def test_allow_interfaces(host, facts):
    """
    Tests if firewall allows access from NICs configured in the inventory.

    This test method checks if iptable rules do exist which allow
    all traffic coming in through the NICs configured in the inventory.

    :param value:     host
    :type  value:     the link to the testinfra host
    :param facts:     Retrieved ansible facts
    :type  facts:     types.SimpleNamespace
    """
    rules = host.iptables.rules()

    testrules = [
        "-A ufw-user-input -i openvpntap0 -j ACCEPT",
        "-A ufw-user-input -i tun0 -j ACCEPT",
    ]

    for testrule in testrules:
        assert testrule in rules
