from ftplib import FTP

import os


class FTPHelper:

    def __init__(self):
        self._host = os.getenv('FTP_HOST')
        self._user = os.getenv("FTP_USER")
        self._pass = os.getenv("FTP_PASS")
        self._port = int(os.getenv("FTP_PORT"))
        self._ftp = None

    def _connection(self):
        self._ftp = FTP()
        self._ftp.connect(self._host, self._port)
        self._ftp.login(self._user, self._pass)

    @property
    def ftp(self):
        if self._ftp is None:
            self._connection()

    def close(self):
        if self._ftp is not None:
            self._ftp.quit()

    def exists_file(self, name, directory=""):
        if self._ftp is not None:
            if directory != "":
                self._ftp.cwd(directory)
            return name in self._ftp.nlst()
