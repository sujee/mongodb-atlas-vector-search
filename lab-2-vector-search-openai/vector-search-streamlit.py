import os, sys
me = os.path.abspath(__file__)
this_dir = os.path.dirname(me)
parent_dir = os.path.dirname(this_dir)
sys.path.append (os.path.abspath (parent_dir))

import streamlit as st
from AtlasClient import AtlasClient
from OpenAIClient import OpenAIClient
from dotenv import find_dotenv, dotenv_values
from urllib.request import urlopen
import time
import json
from llama_index.embeddings import HuggingFaceEmbedding
import re


DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'


## Initialize only once
@st.cache_resource
def initialize():
    config = dotenv_values(find_dotenv())

    ATLAS_URI = config.get('ATLAS_URI')
    OPENAI_API_KEY = config.get("OPENAI_API_KEY")

    if not ATLAS_URI:
        raise Exception ("'ATLAS_URI' is not set.  Please set it above to continue...")

    if not OPENAI_API_KEY:
        raise Exception ("'OPENAI_API_KEY' is not set.  Please set it above to continue...")

    ip = urlopen('https://api.ipify.org').read()
    print (f"My public IP is '{ip}.   Make sure this IP is allowed to connect to cloud Atlas")

    atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
    print ('Atlas client initialized')

    openAI_client = OpenAIClient (api_key=OPENAI_API_KEY)
    print ("openAI client initialized")

    cached_embeddings_openai = {}
    cached_embedding_file = os.path.join(this_dir, 'embeddings_openai.json')

    if os.path.exists(cached_embedding_file):
        with open(cached_embedding_file, "r") as f:
            str = f.read()
            cached_embeddings_openai = json.loads(str)

    return atlas_client, openAI_client, cached_embeddings_openai
## ---------------------------


## init, and do it only once
atlas_client, openAI_client, cached_embeddings_openai  = initialize()
# print (cached_embeddings)

lookup_table = {
    'OpenAI' : {'attribute' : 'plot_embedding',  'index_name': 'idx_plot_embedding'},
    'BAAI/bge-small-en-v1.5' : {'attribute' : 'plot_embedding_bge_small',  'index_name': 'idx_plot_embedding_bge_small'},
    'BAAI/bge-large-en-v1.5' : {'attribute' : 'plot_embedding_bge_large',  'index_name': 'idx_plot_embedding_bge_large'},
}

def clean_string(string : str) -> str:
    string = string.lower().strip()
    string = re.sub(r'\s+', ' ', string).strip()  #consolidate into single space
    return re.sub(r'[^a-zA-Z0-9\s]', '', string).strip()

## ---------------------------
def get_embeddings (text : str, embeddding_model : str) -> list[float]:
    if embeddding_model == 'OpenAI':
        if text in cached_embeddings_openai.keys():
            st.write ("using cached OpenAI embeddings")
            embedding = cached_embeddings_openai.get (text)
        else:
            t1a = time.perf_counter()
            embedding = openAI_client.get_embedding(text)
            t1b = time.perf_counter()
            st.write (f"Got embeddings from openAI API in {(t1b-t1a)*1000:,.0f} ms")
            ## save it in cache
            session_state['cached_embeddings_openai'][text] = embedding
    else:
        hf_embed_model = HuggingFaceEmbedding(model_name=embeddding_model)
        embedding = hf_embed_model.get_text_embedding(text)
    return embedding
## ---------------------------

## ---------------------------
def run_query (query, selected_embedding, output_container):
    output_container.empty()

    with output_container.container():
        st.write (f"running query : '{query}'")
        attr_name = lookup_table[selected_embedding]['attribute']
        index_name = lookup_table[selected_embedding]['index_name']
        st.write (f"selected embedding model : {selected_embedding}")
        # st.write (f"attr_name : {attr_name}")
        # st.write (f"index_name : {index_name}")

        with st.spinner('Finding movies...'):
            embedding = get_embeddings(text = query, embeddding_model= selected_embedding)

            t2a = time.perf_counter()
            movies = atlas_client.vector_search(collection_name=COLLECTION_NAME, index_name=index_name, attr_name=attr_name, embedding_vector=embedding,limit=10 )
            t2b = time.perf_counter()
            st.write (f"Altas query returned {len (movies)} movies in {(t2b-t2a)*1000:,.0f} ms")

        for idx, movie in enumerate (movies):
            md_str =  (f"""
- Movie {idx+1}
  - id: {movie["_id"]}
  - title: **{movie["title"]}**
  - year: {movie["year"]}
  - search_score: **{movie["search_score"]:,.2f}**
  - plot: *{movie["plot"]}*
""")
            st.markdown(md_str)
## ---------------------------


## we are going to cache openai calls here
session_state = st.session_state
session_state['cached_embeddings_openai'] = cached_embeddings_openai


## Process queries
st.header("🎥 Movies Vector Search with MongoDB Atlas")
st.image('images/banner-1.png')
st.markdown("""Here are some sample queries you can try...
- Humans fighting aliens
- fatalistic sci-fi movies
- futuristic christmas movies
- sci-fi story with a friendly alien
- relationship drama between two good friends
- college graduates working in a big city discover new relationships
- household pets get lost but go on a long journey to find home
- go ahead, try your own queries!
""")


selected_embedding = st.selectbox("Select embedding model", ["OpenAI",
                                                             # "BAAI/bge-large-en-v1.5",
                                                             "BAAI/bge-small-en-v1.5" ])
query_text = st.text_input("Movie query:")

# if 'Select embedding model' not in st.session_state:
#     st.session_state['Select embedding model'] = []
output_container = st.empty()
query_text = clean_string (query_text)
if query_text:
    run_query (query_text, selected_embedding, output_container)
