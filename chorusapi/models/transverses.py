import json

import requests

from chorusapi.exceptions.exception import ChorusApiException
from chorusapi.models.api import API
from chorusapi.responses.api_response import ConsulterCrResponse, HealthCheckResponse, ConsulterCrDetailleResponse, \
    InformationSiretResponse, AnnuaireDestinataireResponse, RecupererDevisesResponse


class Transverses(API):
    def __init__(self, client_id, client_secret, tech_username=None, tech_password=None, sandbox=True):
        super().__init__(client_id, client_secret, tech_username, tech_password, sandbox)

    def health_check(self):
        """
        Permet de vérifier la disponibilité des API CPRO.

        :return `chorusapi.responses.api_response.HealthCheckResponse`
        """
        headers = self._make_headers()
        _url = "{}/cpro/transverses/v1/health-check".format(self.api_url)

        req = requests.get(_url, headers=headers, allow_redirects=True)
        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return HealthCheckResponse(req.json())

    def consulter_cr(self, numero_flux_depot):
        """
        Le service ConsulterCR permet de consulter les informations liées au dépôt d'un flux et de récupérer au
        format PDF le compte rendu de traitement du flux déposé via le portail ou le service exposé
        DeposerFluxFacture.

        `numero_flux_depot`
        
        :return `chorusapi.responses.api_response.ConsulterCrResponse`
        """

        headers = self._make_headers()
        data = {
            'numeroFluxDepot': numero_flux_depot
        }
        _url = "{}/cpro/transverses/v1/consulterCR".format(self.api_url)

        req = requests.post(_url, data=json.dumps(data), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return ConsulterCrResponse(req.json())

    def consulter_cr_detaille(self, numero_flux_depot):
        """
        Le service ConsulterCRDetaille permet de consulter l'état d'intégration d'un flux émis en API,
        avec le cas échéant les erreurs identifiées par le système pour l'irrecevabilité du flux
        ou le rejet d'une ou plusieurs demandes de paiement.

        `numero_flux_depot`

        :return `chorusapi.responses.api_response.ConsulterCrDetailleResponse`
        """

        headers = self._make_headers()
        data = {
            'numeroFluxDepot': numero_flux_depot
        }
        _url = "{}/cpro/transverses/v1/consulterCRDetaille".format(self.api_url)

        req = requests.post(_url, data=json.dumps(data), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return ConsulterCrDetailleResponse(req.json())

    def information_siret(self, siret_structure):
        """
        La méthode consulterInformationSIRET permet de récupérer les données de la structure de type SIRET correspondant
        aux paramètres dans le référentiel de l'INSEE (service exposé ne fonctionnant pas sur l'espace de qualification).

        siret_structure

        :return `chorusapi.responses.api_response.InformationSiretResponse`
        """

        headers = self._make_headers()
        data = {
            'siretStructure': siret_structure
        }
        _url = "{}/cpro/transverses/v1/consulter/information/siret".format(self.api_url)

        req = requests.post(_url, data=json.dumps(data), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return InformationSiretResponse(req.json())

    def annuaire_destinataire(self):
        """
        La méthode TelechargerAnnuaireDestinataire permet de récupérer l’annuaire des destinataires.

        :return `chorusapi.responses.api_response.AnnuaireDestinataireResponse`
        """

        headers = self._make_headers()
        _url = "{}/cpro/transverses/v1/telecharger/annuaire/destinataire".format(self.api_url)

        req = requests.post(_url, data=json.dumps({}), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return AnnuaireDestinataireResponse(req.json())

    def devises(self, code_langue="FR"):
        """
        La méthode recupererDevise permet de récupérer la liste des codes devises
        pouvant être renseignées lors de la saisie d'une facture.

        `code_langue` default is `FR`

        :return `chorusapi.responses.api_response.RecupererDevisesResponse`
        """

        headers = self._make_headers()
        data = {
            'codeLangue': code_langue
        }
        _url = "{}/cpro/transverses/v1/recuperer/devises".format(self.api_url)

        req = requests.post(_url, data=json.dumps(data), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return RecupererDevisesResponse(req.json())
