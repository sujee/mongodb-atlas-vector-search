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
OPENAI_API_KEY = config.get("OPENAI_API_KEY")

if not ATLAS_URI:
    raise Exception ("'ATLAS_URI' is not set.  Please set it above to continue...")

if not DB_NAME:
    raise Exception ("'DB_NAME' is not set.  Please set it above to continue...")

if not OPENAI_API_KEY:
    raise Exception ("'OPENAI_API_KEY' is not set.  Please set it above to continue...")

from openai import OpenAI

openai_client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key= OPENAI_API_KEY,
)
print ("OpenAI Client initialized!")

# https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

def get_embedding(text: str,  model="text-embedding-ada-002") -> list[float]:
    text = text.replace("\n", " ")
    resp = openai_client.embeddings.create (
		input=[text],
		model=model  )

    return resp.data[0].embedding

atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
print (atlas_client)

ip = urlopen('https://api.ipify.org').read()
print (f"My public IP is '{ip}.   Make sure this IP is allowed to connect to cloud Atlas")


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

## Search by embeddings
print ('======== Going to do an embedding search ========================')
plot = 'a futuristic Sci-fi movie'
embedding = get_embedding (plot)
print (f"Embedding for text='{plot}', embeddding_length={len(embedding)}, printing first few numbers... :\n", embedding [:10] )


