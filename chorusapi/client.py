from chorusapi.models.factures import Factures
from chorusapi.models.structures import Structures
from chorusapi.models.transverses import Transverses


class ChorusAPI(Factures, Structures, Transverses):
    def __init__(self, client_id, client_secret, tech_username=None, tech_password=None, sandbox=True):
        """
        :param client_id:
        :param client_secret:
        :param tech_username:
        :param tech_password:
        :param sandbox:
        """
        super().__init__(client_id, client_secret, tech_username, tech_password, sandbox)
