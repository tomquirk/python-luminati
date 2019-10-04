# python-luminati

A handy Python interface for [luminati.io](https://luminati.io/)

## Usage

```python
import requests
from luminati import Luminati

luminati = Luminati('my-user', 'passw0rd', country='us')
url = luminati.url

res = requests.get('www.example.com', proxy={'https': url})

# refresh the URL (i.e. get a new session)
resNext = requests.get('www.example.com', proxy={'https': luminati.refresh_url()})
```
