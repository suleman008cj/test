from websocket import create_connection
import json

# Copy the web brower header and input as a dictionary
headers = json.dumps({
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Host': 'streamer.cryptocompare.com',
    'Origin': 'https://www.cryptocompare.com',
    'Pragma': 'no-cache',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    'Sec-WebSocket-Key': 'in6dCK/XY9j+9rWAeNRDXQ==',
    'Sec-WebSocket-Version': '13',
    'Upgrade': 'websocket',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
})

# Launch the connection to the server.
ws = create_connection('wss://streamer.cryptocompare.com/v2',headers=headers)

# Perform the handshake.
ws.send(json.dumps({"action": "SubAdd", "subs": ["11~BTC", "21~BTC", "5~CCCAGG~BTC~USD", "11~ETH", "21~ETH", "5~CCCAGG~ETH~USD", "11~BCH", "21~BCH", "5~CCCAGG~BCH~USD", 
                    "11~EOS", "21~EOS", "5~CCCAGG~EOS~USD", "11~XRP", "21~XRP","5~CCCAGG~XRP~USD", "11~LTC", "21~LTC", "5~CCCAGG~LTC~USD", 
                    "11~ETC", "21~ETC", "5~CCCAGG~ETC~USD", "11~BSV", "21~BSV", "5~CCCAGG~BSV~USD", "11~LINK", "21~LINK", "5~CCCAGG~LINK~USD", "11~ATOM", "21~ATOM", "5~CCCAGG~ATOM~USD"]}))

# Printing all the result
while True:
    try:
        result = ws.recv()
        print(result)
    except Exception as e:
        print(e)
        break
