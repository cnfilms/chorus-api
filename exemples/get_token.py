from chorusapi.client import ChorusAPI
from exemples.env import CLIENT_ID, CLIENT_SECRET, SANDBOX

chorus_api = ChorusAPI(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    sandbox=SANDBOX
)

token = chorus_api.auth().get_token()
print(token)
