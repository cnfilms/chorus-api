# CHORUS-API / PISTE.GOUV.FR

# chorus-api [![Downloads](https://static.pepy.tech/personalized-badge/chorus-api?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/chorus-api)

Chorus API Package [https://piste.gouv.fr](https://piste.gouv.fr)

## How to install chorus-api

# Install

```shell
pip install chorus-api
```

## 1.0.5
#### CHANGES
* Fix **_base_64_encode_file_** method in utils
* Allow pass encoding

## 1.0.4

#### CHANGES

`Integration de l'état courant`

* Le service ConsulterCR permet de consulter les informations liées au dépôt d'un flux et de récupérer au format PDF le
  compte rendu de traitement du flux déposé via le portail ou le service exposé DeposerFluxFacture.

| Key                            | code                           | description                                                                                      |
|--------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------|
| IN_RECU                        | IN_RECU                        | Le flux a été reçu par Chorus Pro                                                                |
| IN_TRAITE_SE_CPP               | IN_TRAITE_SE_CPP               | Le fichier arrivé dans le système d’échange Chorus Pro                                           |
| IN_EN_ATTENTE_TRAITEMENT_CPP   | IN_EN_ATTENTE_TRAITEMENT_CPP   | Le flux est en liste d’attente                                                                   |
| IN_EN_COURS_TRAITEMENT_CPP     | IN_EN_COURS_TRAITEMENT_CPP     | Le flux est en cours de traitement                                                               |
| IN_INCIDENTE                   | IN_INCIDENTE                   | Flux non traité par le système d’échange, il sera nécessaire de reprendre le flux intégralement. |
| IN_REJETE                      | IN_REJETE                      | Le flux a été traité mais rejeté car il comporte des anomalies                                   |
| IN_EN_ATTENTE_RETRAITEMENT_CPP | IN_EN_ATTENTE_RETRAITEMENT_CPP | Le flux a été bloqué, il attend une reprise manuelle                                             |
| IN_INTEGRE                     | IN_INTEGRE                     | Le flux a été traité et tout a été intégré dans Chorus Pro.                                      |
| IN_INTEGRE_PARTIEL             | IN_INTEGRE_PARTIEL             | Cela concerne des flux qui sont en rejet partiel, seules les factures correctes sont intégrées.  |

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