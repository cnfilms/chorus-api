from chorusapi.responses.api_response import DeposerFluxResponse, RechercheFactureResponse
from chorusapi.constants.syntax_flux_constant import SyntaxFlux
from chorusapi.exceptions.exception import ChorusApiException
from chorusapi.models.api import API
import requests
import json


class Factures(API):
    def __init__(self, client_id, client_secret, tech_username=None, tech_password=None, sandbox=True):
        super().__init__(client_id, client_secret, tech_username, tech_password, sandbox)

    def deposer_flux(self, fichier_flux, file_name, avec_signature=False,
                     syntaxe_flux=SyntaxFlux.IN_DP_E2_CII_FACTURX):
        """
        La méthode deposerFluxFacture permet de déposer un fichier XML ou PDF/A3 permettant de renseigner les données
        nécessaires à la constitution d'un flux facture.

        `fichier_flux`: Le fichier facture encodé en base64
        `file_name`: Le nom du fichier + extension
        `avec_signature`: default `False`
        `syntaxe_flux`: default is `chorusapi.constants.syntax_flux_constant.SyntaxFlux.IN_DP_E2_CII_FACTURX`

        :return `chorusapi.responses.api_response.DeposerFluxResponse`
        """
        headers = self._make_headers()
        data = {
            'idUtilisateurCourant': 0,
            'fichierFlux': fichier_flux,
            'nomFichier': file_name,
            'syntaxeFlux': syntaxe_flux,
            'avecSignature': avec_signature,
        }
        _url = "{}/cpro/factures/v1/deposer/flux".format(self.api_url)

        req = requests.post(_url, data=json.dumps(data), headers=headers, allow_redirects=True)

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return DeposerFluxResponse(req.json())

    def rechercher_facture(self, numero_flux_depot):
        """
        La méthode rechercherFactureParFournisseur permet d'afficher les factures émises correspondant aux paramètres
        de recherche renseignés.

        `numero_flux_depot`

        :return `chorusapi.responses.api_response.RechercheFactureResponse`
        """

        _url = "{}/cpro/factures/v1/rechercher/fournisseur".format(self.api_url)

        headers = self._make_headers()
        payload = {"numeroFluxDepot": numero_flux_depot, "typeFacture": "FACTURE"}

        req = requests.post(_url, headers=headers, data=json.dumps(payload))

        if req.status_code != 200:
            raise ChorusApiException(self._make_error_msg(req))

        return RechercheFactureResponse(req.json())
