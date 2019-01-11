# nk-proxy
A simple proxy wrapper for internal proxy service.  Supports both https and https endpoints.  Currently https endpoint operates under ssl-insecure until self-signed certificates are installed.

# Basic Usage

pip install `git+https://github.com/NewKnowledge/nk-proxy.git@<branch-name or commit-hash>#egg=nk_proxy`. Typically, this is done by adding it to `requirements.txt` (pip) or `environment.yml` (conda). Make sure git is installed on the system or container.

At the top of each file that uses a proxy, put:
```
import requests
from nk_proxy import get_proxy
proxy = get_proxy()

response = requests.get('http/https://www.website.com', proxies=proxy.as_dict, verify=False)

assert response.status_code == 200
```
Note: *verify=False*, is required for https endpoints to ensure certificate verification is not performed.

Proxy status can be tested using the folowing:
```
from nk_proxy import get_proxy, test_proxy
proxy = get_proxy()

http_proxy_status = test_proxy(proxy.http_proxy)
assert http_proxy_status

https_proxy_status = test_proxy(proxy.https_proxy)
assert https_proxy_status

```
# Configure
Currently no configuration options exist.  
