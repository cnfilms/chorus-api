import json

import requests

from chorusapi.responses.api_response import RechercheStructureResponse, RechercheServiceResponse, \
    ConsulterStructureResponse
from chorusapi.exceptions.exception import ChorusApiException
from chorusapi.models.api import API


class Structures(API):
    def __init__(self, client_id, client_secret, tech_username=None, tech_password=None, sandbox=True):
        super().__init__(client_id, client_secret, tech_username, tech_password, sandbox)

    def rechercher_structure(self, siret, type_identifiant="SIRET"):
        """
        La méthode rechercherStructure permet à un gestionnaire de rechercher des structures.

        `siret`
        `type_identifiant` default is `SIRET`

        :return `chorusapi.responses.api_response.RechercheStructureResponse`
        """
        _url = "{}/cpro/structures/v1/rechercher".format(self.api_url)

        headers = self._make_headers()
        payload = {
            "structure": {
                "identifiantStructure": siret,
                "typeIdentifiantStructure": type_identifiant
            }
        }

        req = requests.post(_url, headers=headers, data=json.dumps(payload))

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return RechercheStructureResponse(req.json())

    def rechercher_services(self, id_structure):
        """
        La méthode rechercherServicesStructure permet de rechercher les services appartenant à une structure publique
        ou à une structure à laquelle l'utilisateur est rattaché.

        `id_structure`

        :return `chorusapi.responses.api_response.RechercheServiceResponse`
        """
        _url = "{}/cpro/structures/v1/rechercher/services".format(self.api_url)

        headers = self._make_headers()
        payload = {
            "idStructure": id_structure
        }

        req = requests.post(_url, headers=headers, data=json.dumps(payload))

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return RechercheServiceResponse(req.json())

    def consulter_structure(self, id_structure_cpp, code_langue="fr"):
        """
        La méthode consulterStructure permet de consulter les informations relatives à une structure à laquelle
        l'utilisateur est rattaché ou une structure publique.

        `id_structure_cpp`
        `code_langue` default is `fr`

        :return `chorusapi.responses.api_response.ConsulterStructureResponse`
        """

        _url = "{}/cpro/structures/v1/consulter".format(self.api_url)

        headers = self._make_headers()
        payload = {
            "codeLangue": code_langue,
            "idStructureCPP": id_structure_cpp
        }

        req = requests.post(_url, headers=headers, data=json.dumps(payload))

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return ConsulterStructureResponse(req.json())
