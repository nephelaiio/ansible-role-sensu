import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    assert 'sensu' in host.user('sensu').groups
    assert host.user('sensu').home == "/opt/sensu"
    assert host.file('/opt/sensu').exists
    assert host.file('/opt/sensu').is_directory


def test_rbenv(host):
    assert host.file('/opt/sensu/.rbenv').exists
    assert host.file('/opt/sensu/.rbenv').is_directory
    assert host.file('/opt/sensu/.rbenv/2.4.1/bin/ruby').exists
    assert host.file('/opt/sensu/.rbenv/2.4.1/bin/ruby').is_file
