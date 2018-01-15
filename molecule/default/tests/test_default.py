import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

user_home = '/opt/sensu'
ruby_bin = '/usr/local/bin/ruby'
run_dir = '/var/run/sensu'


def test_rbenv(host):
    assert host.file(ruby_bin).exists
    assert host.file(ruby_bin).is_file
    host.run('{0} --version'.format(ruby_bin)).rc == 0


def test_sensu(host):
    assert host.service('sensu-client').is_running
    assert host.service('sensu-client').is_enabled
    assert host.file(run_dir).exists
    assert host.file(run_dir).is_directory
