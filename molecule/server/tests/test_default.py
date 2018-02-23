import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sensu(host):
    assert host.service('sensu-server').is_enabled
    assert host.service('sensu-api').is_running
    assert host.service('sensu-api').is_enabled
