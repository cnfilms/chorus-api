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

# Consulter les informations liées au dépôt d'un flux
status_depot = chorus_api.auth().consulter_cr("CPP0011117000000000300163")
print_as_table(status_depot)
