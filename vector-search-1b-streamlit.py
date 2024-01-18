import streamlit as st
from AtlasClient import AtlasClient
from OpenAIClient import OpenAIClient
from dotenv import find_dotenv, dotenv_values
from urllib.request import urlopen
import time

DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'
INDEX_NAME = 'idx_plot_embedding'


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

    return atlas_client, openAI_client
## ---------------------------

## ---------------------------
def run_query (query, output_container):
    output_container.empty()

    with output_container.container():
        st.write (f'running query : {query}')

        t1a = time.perf_counter()
        embedding = openAI_client.get_embedding(query)
        t1b = time.perf_counter()
        st.write (f"Got embeddings from openAI API in {(t1b-t1a)*1000:,.0f} ms ({embedding [:5]} ...)")

        t2a = time.perf_counter()
        movies = atlas_client.vector_search(collection_name=COLLECTION_NAME, index_name=INDEX_NAME, attr_name='plot_embedding', embedding_vector=embedding,limit=10 )
        t2b = time.perf_counter()
        st.write (f"Altas query returned {len (movies)} movies in {(t2b-t2a)*1000:,.0f} ms")
        for idx, movie in enumerate (movies):
            md_str =  (f"""
- Movie {idx+1}
  - id: {movie["_id"]}
  - title: {movie["title"]}
  - year: {movie["year"]}
  - plot: {movie["plot"]}
""")
            st.markdown(md_str)
## ---------------------------

## init, and do it only once
atlas_client, openAI_client = initialize()

## Process queries
st.header("Atlas Vector Search 🎥")
st.markdown("""Here are some sample queries you can try...
- Humans fighting aliens
- fatalistic sci-fi movies
- go ahead, be creative!
""")
query_text = st.text_input("Movie query:")
output_container = st.empty()

if query_text:
    run_query (query_text, output_container)
