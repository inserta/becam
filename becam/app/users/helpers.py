# -*- encoding: utf-8 -*-
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

import paramiko
import posixpath
import getpass
import os


@deconstructible
class SFTPStorage(Storage):

    def __init__(self):
        self._user = "u88749362-python"
        self._pass = "PythonProject2019*"
        self._host = "home674974141.1and1-data.host"
        self._port = 22
        self._base_url = "http://becam.becheckin.com/"
        self._root_path = "/"
        self._sftp = None
        self._known_host_file = None
        self._params = {
            'username': self._user,
            'password': self._pass
        }

    def _connect(self):
        self._ssh = paramiko.SSHClient()
        known_host_file = self._known_host_file or os.path.expanduser(
            os.path.join("~", ".ssh", "known_hosts")
        )

        if os.path.exists(known_host_file):
            self._ssh.load_host_keys(known_host_file)
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self._ssh.connect(self._host, self._port, **self._params)
        except paramiko.AuthenticationException as e:
            if self._interactive and 'password' not in self._params:
                if 'username' not in self._params:
                    self._params['username'] = getpass.getuser()
                self._params['password'] = getpass.getpass()
                self._connect()
            else:
                raise paramiko.AuthenticationException(e)
        except Exception as e:
            print(e)

        if self._ssh.get_transport():
            self._sftp = self._ssh.open_sftp()

    @property
    def sftp(self):
        """Lazy SFTP connection"""
        if not self._sftp or not self._ssh.get_transport().is_active():
            self._connect()
        return self._sftp

    def _remote_path(self, name):
        return posixpath.join(self._root_path, name)

    def exists(self, name):
        try:
            self.sftp.stat(self._remote_path(name))
            return True
        except IOError:
            return False

    def url(self, name):
        return "{}{}".format(self._base_url, name)