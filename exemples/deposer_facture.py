from chorusapi.utils.chorus_utils import base_64_encode_file
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

# Deposer Facture
deposer_facture_xml = chorus_api \
    .auth() \
    .deposer_flux(fichier_flux=base_64_encode_file("pdf/facture_1819.pdf"),
                  file_name="facture_1819.pdf")

print_as_table(deposer_facture_xml)
