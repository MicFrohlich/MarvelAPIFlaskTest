import random
import requests
import hashlib
import datetime


PUBLIC_KEY = "52cc87e2d83af6e671516e21ed089ddb"
PRIVATE_KEY = "4a84d88eeb646ee7efeb159562c6db8cf4d131df"

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

def get_params():
    """return the params for any api call"""
    params = {'ts': timestamp, 'apikey': PUBLIC_KEY, 'hash': hash_params()}
    return params

def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def get_story(stories: {}):
    """Get a Story from the list of stories for the given character"""
    story = random.choice(stories)
    story_resource = story['resourceURI'] 
    name = story['name'] 
    return story

def get_characters(characters: {}):
    """ Get the character names from the returned character data"""
    character_names = []
    for char in characters:
        character_names.append(char["name"])
    return character_names

def get_character_thumbnails(story_characters: {}):
    """Get Characters thumbnails from data"""
    char_thumbnails = []
    params = {'ts': timestamp, 'apikey': PUBLIC_KEY, 'hash': hash_params()}
    for char in story_characters:
        res = requests.get(char["resourceURI"], params=params)
        results = res.json()["data"]["results"][0]
        char_thumbnails.append(results["thumbnail"])
    return char_thumbnails

def character_names_and_thumbnails(character_names: [], char_pic_paths: []):
    """Return a dictionary with the characters name and their thumbnail"""
    characters = {}
    assert len(character_names)==len(char_pic_paths)
    for num in range(len(character_names)):
        characters[character_names[num]] = char_pic_paths[num]
    return characters

def get_index_context_data():
    """Function to get all the context data for the marvel page task"""
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
    story_name = story_results["title"]
    story_characters = story_results["characters"]["items"]

    character_names = get_characters(story_characters)
    character_pictures = get_character_thumbnails(story_characters)
    char_pic_paths = []
    for pic in character_pictures:
        char_pic_paths.append(pic['path'])

    characters = character_names_and_thumbnails(character_names, char_pic_paths)

    char_thumbnail = results["thumbnail"]
    char_thumb_path = char_thumbnail["path"]
    marvel_attribution = res.json()["attributionHTML"]

    return name, comics, story_description, story_name, char_thumb_path, characters, char_pic_paths, marvel_attribution