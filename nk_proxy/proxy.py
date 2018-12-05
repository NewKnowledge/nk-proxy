from collections import namedtuple
import requests

PROXY = namedtuple('Proxy', 'url domain port ssl')


class NKProxy:
    def __init__(self):
        self._http_proxy = PROXY('upstream-proxy-service-service:8080', 'upstream-proxy-service-service', '8080', False)
        self._https_proxy = PROXY('upstream-proxy-service-service:8080', 'upstream-proxy-service-service', '8080', True)

    @property
    def http_proxy(self):
        return self._http_proxy

    @property
    def https_proxy(self):
        return self._https_proxy

    @property
    def as_dict(self):
        return {'http': self.http_proxy.url,
                'https': self.https_proxy.url}


def get_proxy():
    return NKProxy()


def test_proxy():
    try:
        response = requests.get('https://www.google.com'.format(protocol), proxies=get_proxy().as_dict, verify=False)

        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

