# CHORUS API

# chorusapi [![Downloads](https://static.pepy.tech/personalized-badge/chorusapi?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/izi18n)

Chorus API Package [https://piste.gouv.fr](https://piste.gouv.fr)

## How to install chorus-api

# Install

```shell
pip install chorus-api
```

# Usage

* [GET TOKEN](exemples/get_token.py)

```python
from chorusapi.client import ChorusAPI
from exemples.env import CLIENT_ID, CLIENT_SECRET

chorus_api = ChorusAPI(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

token = chorus_api.auth().get_token()
print(token)
```

* [Consulter les informations liées au dépôt d'un flux](exemples/status_depot.py)

```python
from chorusapi.client import ChorusAPI
from exemples.env import CLIENT_ID, CLIENT_SECRET, TECH_USERNAME, TECH_PASSWORD

chorus_api = ChorusAPI(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tech_username=TECH_USERNAME,
    tech_password=TECH_PASSWORD
)

status_depot = chorus_api.auth().consulter_cr("CPP0XXXXXXXXXXXXX")
print(status_depot.__dict__)
```

## More details in [examples](exemples) folders