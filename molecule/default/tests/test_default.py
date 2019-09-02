import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_default_python_version(host):
    '''
    Ensure that the default python version is untouched
    '''
    cmd = "python --version"
    c = host.run(cmd)
    assert c.rc == 0
    assert c.stderr.strip() == "Python 2.6.6"


def test_pip_27_exists(host):
    f = host.file('/usr/local/bin/pip2.7')

    assert f.exists


def test_virtualenv(host):
    f = host.file('/opt/src/virtenv')

    assert f.exists
    assert f.is_directory


def test_venv_python_version(host):
    cmd = "source /opt/src/virtenv/bin/activate && python --version"
    c = host.run(cmd)
    assert c.rc == 0
    assert c.stderr.strip() == "Python 2.7.16"
