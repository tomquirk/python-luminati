# python-luminati

Python Interface for Luminati

## Usage

```python
import requests
from luminati import Luminati

luminati = Luminati('my-user', 'passw0rd', country='us')
url = Luminati.url

requests.get('www.example.com', proxy={'https': url})
```
