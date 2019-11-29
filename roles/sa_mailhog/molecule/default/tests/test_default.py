import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mailhog_running_and_enabled(host):
    assert not host.ansible(
        "service",
        "name=mailhog enabled=true state=started")['changed']


def test_mailhog_listens_on_ports(host):
    # WebUI
    assert host.socket("tcp://0.0.0.0:8025").is_listening
    # SMTP
    assert host.socket("tcp://0.0.0.0:1025").is_listening
