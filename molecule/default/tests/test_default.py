import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

user_name = 'sensu'
user_group = 'sensu'
user_home = '/opt/sensu'
ruby_bin = '/usr/local/bin/ruby'
run_dir = '/var/run/sensu'


def test_user(host):
    assert user_group in host.user(user_name).groups
    assert host.user(user_name).home == user_home
    assert host.file(user_home).exists
    assert host.file(user_home).is_directory


def test_rbenv(host):
    assert host.file(ruby_bin).exists
    assert host.file(ruby_bin).is_file
    with host.sudo(user_name):
        host.run('{0} --version'.format(ruby_bin)).rc == 0


def test_sensu(host):
    assert host.service('sensu-client').is_running
    assert host.service('sensu-client').is_enabled
    assert host.file(run_dir).exists
    assert host.file(run_dir).is_directory
    assert host.file(run_dir).user == user_name
