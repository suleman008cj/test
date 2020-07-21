import json
import hmac
import hashlib
import datetime
from websocket import create_connection
from websocket import recv

api_key = '48913646dd3750cbad26a1c200f55b'
api_secret ='cf92d265b5124257eb56a1ec87e465a84eba13eee5c79122cdeae1dead49'


def generate_signature(secret, message):
    message = bytes(message, 'utf-8')
    secret = bytes(secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest()


def get_time_stamp():
    d = datetime.datetime.utcnow()
    epoch = datetime.datetime(1970, 1, 1)
    return str(int((d - epoch).total_seconds()))


# Get open orders

method = 'GET'
timestamp = get_time_stamp()
path = '/live'
signature_data = method + timestamp + path
signature = generate_signature(api_secret, signature_data)

url = 'wss://api.delta.exchange:2096'


class delta(object):

    def __init__(self, api_secret, api_key,timestamp,signature):
        self.api_secret = api_secret
        self.api_key = api_key
        self.url = 'wss://api.delta.exchange:2096'
        self.timestamp = timestamp
        self.signature = signature
        self.payload = {'type':'auth',
        'api-key': self.api_key,
                        'signature': self.signature,
                        'timestamp': self.timestamp}
        self.ws = create_connection(url)

    def get_chanid(self):
        self.ws.send(json.dumps(self.payload))
        get_chanid = {'type': 'subscribe',
                      'payload': {'channels': [{'name': 'ticker',
                      'symbols': ['BTCUSD_28Dec', 'ETHBTC_28Dec']},
                      {'name': 'l2_orderbook',
                      'symbols': ['BTCUSD_28Dec']}]}}

        self.ws.send(json.dumps(get_chanid))
        while True:
            self.ws.send(json.dumps({'type':'ping'}))
            


bit = delta(api_secret, api_key,timestamp,signature)
bit.get_chanid()
