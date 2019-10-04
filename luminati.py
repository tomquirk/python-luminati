from random import random


class Luminati:
    def __init__(self, username, password, port=22225, country=None, protocol="http"):
        if not (username and password):
            raise Exception("invalid params", username, password)
        self._username = username
        self._password = password
        self._port = port
        self._country = country
        self._protocol = protocol
        self._current_proxy_url = ""

        self.refresh_url()

    def refresh_url(self, country=None):
        country = country or self._country
        session_id = random()
        super_proxy_url = "%s://%s%s-session-%s:%s@zproxy.lum-superproxy.io:%d" % (
            self._protocol,
            self._username,
            f"-country-{country}" if country else "",
            session_id,
            self._password,
            self._port,
        )

        self._current_proxy_url = super_proxy_url

        return super_proxy_url

    @property
    def url(self):
        return self._current_proxy_url
