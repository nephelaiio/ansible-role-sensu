import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

user_name = 'sensu'
user_group = 'sensu'
user_home = '/opt/sensu'
user_rbenv = '{0}/embedded'.format(user_home)
ruby_bin = '{0}/bin/ruby'.format(user_rbenv)


def test_user(host):
    assert user_group in host.user(user_name).groups
    assert host.user(user_name).home == user_home
    assert host.file(user_home).exists
    assert host.file(user_home).is_directory


def test_rbenv(host):
    assert host.file(user_rbenv).exists
    assert host.file(user_rbenv).is_directory
    assert host.file(ruby_bin).exists
    assert host.file(ruby_bin).is_file
    with host.sudo(user_name):
        host.run('{0} --version'.format(ruby_bin)).rc == 0


def test_sensu(host):
    assert host.service('sensu-client').is_running
    assert host.service('sensu-client').is_enabled
