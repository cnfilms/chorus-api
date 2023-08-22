from chorusapi.client import ChorusAPI
from exemples.env import CLIENT_ID, CLIENT_SECRET, TECH_USERNAME, TECH_PASSWORD, SANDBOX
from exemples.utils.print_dict import print_as_table

chorus_api = ChorusAPI(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tech_username=TECH_USERNAME,
    tech_password=TECH_PASSWORD,
    sandbox=SANDBOX
)

# Recherche Structure
recherche_structure = chorus_api.auth().rechercher_structure("21380538500019")
print_as_table(recherche_structure)
# print("Libelle :", recherche_structure.libelle)
# print("*************************************")
# for structure in recherche_structure.liste_structures:
#     print_as_table(structure.__dict__)
