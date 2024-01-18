import os,sys
# add parent dir to sys path
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)
sys.path.append (os.path.abspath (parent_dir))


from AtlasClient import AtlasClient
from urllib.request import urlopen

## Load Settings from .env file
from dotenv import find_dotenv, dotenv_values

# _ = load_dotenv(find_dotenv()) # read local .env file
config = dotenv_values(find_dotenv())

# debug
# print (config)

ATLAS_URI = config.get('ATLAS_URI')
DB_NAME = config.get ('DB_NAME')

if not ATLAS_URI:
    raise Exception ("'ATLAS_URI' is not set.  Please set it above to continue...")

DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'

ip = urlopen('https://api.ipify.org').read()
print (f"My public IP is '{ip}.   Make sure this IP is allowed to connect to cloud Atlas")

atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
print ('Atlas client initialized')

## first find some movies
print ('======== Finding some sample movies ========================')
movies = atlas_client.find (collection_name="embedded_movies", limit=5)
print (f"Found {len (movies)} movies")
for idx, movie in enumerate (movies):
    print(f'{idx+1}\nid: {movie["_id"]}\ntitle: {movie["title"]},\nyear: {movie["year"]}\nplot: {movie["plot"]}\n')
print ('================================')

## find movies from year 1999
print ('=======  Finding movies from year 1999 =========================')
movies_1999 = atlas_client.find(collection_name="embedded_movies", filter={"year": 1999}, limit=5)
print (f"Found {len (movies_1999)} movies from year 1999")
for idx, movie in enumerate (movies_1999):
    print(f'{idx+1}\nid: {movie["_id"]}\ntitle: {movie["title"]},\nyear: {movie["year"]}\nplot: {movie["plot"]}\n')



