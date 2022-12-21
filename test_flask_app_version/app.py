from flask import Flask, render_template
from marvel import Marvel
from custom_functions import (
    get_story, 
    get_characters, 
    hash_params, 
    get_params, 
    get_character_thumbnails,
    character_names_and_thumbnails
)
import requests
import datetime
import inspect

from pprint import pprint as pp

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/characters")
def characters():
    params = get_params()
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009399',
                    params=params)
    results = res.json()["data"]["results"][0]
    comics_data = results["comics"]
    stories_data = results["stories"]
    events_data = results["events"]
    series_data = results["series"]

    comics = comics_data["items"]
    events = events_data["items"]
    name = results["name"]
    series = series_data["items"]
    stories = stories_data["items"]

    story_resource = get_story(stories)
    story_data_req = requests.get(story_resource['resourceURI'], params=params)
    story_results = story_data_req.json()["data"]["results"][0]

    story_description = story_results["description"]
    story_characters = story_results["characters"]["items"]

    character_names = get_characters(story_characters)
    character_pictures = get_character_thumbnails(story_characters)
    char_pic_paths = []
    for pic in character_pictures:
        char_pic_paths.append(pic['path'])

    characters = character_names_and_thumbnails(character_names, char_pic_paths)

    char_thumbnail = results["thumbnail"]
    char_thumb_path = char_thumbnail["path"]
    
    return render_template(
        './index.html', 
        name=name, 
        comics=comics, 
        story_desc=story_description,
        char_thumbnail=char_thumb_path,
        characters=characters,
        character_pictures=char_pic_paths
    )

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


