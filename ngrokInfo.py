import requests


def listNgroks():
    url = "http://localhost:4040/api/tunnels"
    with requests.get(url) as resp:
        return resp.json()


# Get the ngrok hostname
resp = listNgroks()
address = resp['tunnels'][0]['public_url']

# Save ngrok hostname to desired file
PATH = '/home/code/scripts/ngrokHostname.txt'
with open(PATH, 'w') as f:
    f.write(address)
