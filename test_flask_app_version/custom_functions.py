import random
import requests
import hashlib
import datetime


PUBLIC_KEY = "52cc87e2d83af6e671516e21ed089ddb"
PRIVATE_KEY = "4a84d88eeb646ee7efeb159562c6db8cf4d131df"

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

def get_params():
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
    story = random.choice(stories)
    story_resource = story['resourceURI'] 
    name = story['name'] 
    return story

def get_characters(characters: {}):
    character_names = []
    for char in characters:
        character_names.append(char["name"])
    return character_names

def get_character_thumbnails(story_characters: {}):
    char_thumbnails = []
    params = {'ts': timestamp, 'apikey': PUBLIC_KEY, 'hash': hash_params()}
    for char in story_characters:
        res = requests.get(char["resourceURI"], params=params)
        results = res.json()["data"]["results"][0]
        char_thumbnails.append(results["thumbnail"])
    return char_thumbnails

def character_names_and_thumbnails(character_names: [], char_pic_paths: []):
    characters = {}
    assert len(character_names)==len(char_pic_paths)
    for num in range(len(character_names)):
        characters[character_names[num]] = char_pic_paths[num]
    return characters