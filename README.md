# nephelaiio.sensu

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-sensu.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-sensu)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.sensu-blue.svg)](https://galaxy.ansible.com/nephelaiio/sensu/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/sensu) to install and configure sensu services from gem packages. This is a workaround for [Sensu Issue 1676](https://github.com/sensu/sensu/issues/1676)

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

- hosts: servers
  roles:
     - role: sensu


## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Debian Stretch

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
