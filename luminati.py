from random import random

class Luminati:
    def __init__(self, username, password, port=22225, country=''):
        self._username = username
        self._password = password
        self._port = port
        self._current_proxy_url = ''

        self.refresh_url()

    def refresh_url(self):
        session_id = random()
        super_proxy_url = (
            "http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d"
            % (self._username, f'country-{self._country}' if self._country else '', session_id, self._password, self._port)
        )

        self._current_proxy_url = super_proxy_url

        return super_proxy_url

    @property
    def url(self):
        return self._super_proxy_url

