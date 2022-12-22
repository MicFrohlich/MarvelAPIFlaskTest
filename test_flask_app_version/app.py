from flask import Flask, render_template
from marvel import Marvel
from custom_functions import (
    get_story, 
    get_characters, 
    hash_params, 
    get_params, 
    get_character_thumbnails,
    character_names_and_thumbnails,
    get_index_context_data
)
import requests
import datetime
import inspect

from pprint import pprint as pp

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

app = Flask(__name__)


@app.route("/")
def my_favourite_marvel_character():
    (
        name, 
        comics, 
        story_description, 
        story_name, 
        char_thumb_path, 
        characters, 
        char_pic_paths,
        marvel_attribution
    ) = get_index_context_data()
    return render_template(
        './index.html', 
        name=name, 
        comics=comics, 
        story_desc=story_description,
        story_name=story_name,
        char_thumbnail=char_thumb_path,
        characters=characters,
        character_pictures=char_pic_paths,
        marvel_attribution=marvel_attribution
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


