from flask import Flask
from marvel import Marvel
import hashlib
import requests
import datetime

from pprint import pprint as pp


PUBLIC_KEY = "52cc87e2d83af6e671516e21ed089ddb"
PRIVATE_KEY = "4a84d88eeb646ee7efeb159562c6db8cf4d131df"

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

characters = m.characters
comics = m.comics 
creators = m.creators 
events = m.events 
series = m.series 
stories = m.stories

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

app = Flask(__name__)

def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/characters")
def characters():
    html = []
    params = {'ts': timestamp, 'apikey': PUBLIC_KEY, 'hash': hash_params()};
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters',
                    params=params)
    results = res.json()
    html.append(results["data"]["results"])
    return html

@app.route("/comics")
def comics():
    html = ""
    for val in comics:
        html.append(f"<p>{val}</p>")
    return html

@app.route("/creators")
def creators():
    html = ""
    for val in creators:
        html.append(f"<p>{val}</p>")
    return html

@app.route("/events")
def events():
    html = ""
    for val in events:
        html.append(f"<p>{val}</p>")
    return html

@app.route("/series")
def series():
    html = ""
    for val in series:
        html.append(f"<p>{val}</p>")
    return html

@app.route("/stories")
def stories():
    html = ""
    for val in stories.all():
        html.append(f"<p>{val}</p>")
    return html
