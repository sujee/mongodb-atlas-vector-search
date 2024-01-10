import os,sys
# add parent dir to sys path
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)
sys.path.append (os.path.abspath (parent_dir))


from OpenAIClient import OpenAIClient

## Load Settings from .env file
from dotenv import find_dotenv, dotenv_values

# _ = load_dotenv(find_dotenv()) # read local .env file
config = dotenv_values(find_dotenv())

# debug
# print (config)

OPENAI_API_KEY = config.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise Exception ("'OPENAI_API_KEY' is not set.  Please set it above to continue...")


openAI_client = OpenAIClient (api_key=OPENAI_API_KEY)

word = 'apple'
model = 'text-embedding-ada-002'
embedding = openAI_client.get_embedding(word, model)
print (f"Embedding for word='{word}' using model='{model}', embeddding_length={len(embedding)}, printing first few numbers... :\n", embedding [:10] )

