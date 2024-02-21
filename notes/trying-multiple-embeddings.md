# Trying Muliple Embeddings

## 1 - Upgrade

The free tier Atlas allows 3 vector indexes.  So I upgraded using credits to M1 (shared)

## 2 - Populate embedding

Edited [lab-3-vector-search-custom/vector-search-custom-embeddings-populate.ipynb](../lab-3-vector-search-custom/vector-search-custom-embeddings-populate.ipynb)

Enabled `BAAI/bge-large-en-v1.5` embedding model and updated the collection

## 3 - Created vector search indexes

index name : idx_plot_embedding_bge_large

```json
{
  "fields": [
    {
      "numDimensions": 1024,
      "path": "plot_embedding_bge_large",
      "similarity": "dotProduct",
      "type": "vector"
    }
  ]
}
```

Also changed all indexes to type `dotProduct`

## 4 - Updated Streamlit App

Updated model lookup table in [lab-2-vector-search-openai/vector-search-streamlit.py](../lab-2-vector-search-openai/vector-search-streamlit.py)


## 5 - Create a google project

Create a new project `atlas-vector-search` in google UI

Authorize gcloud CLI

```bash
gcloud auth login

gcloud config set project   PROJECT_ID
```

Enable Google Artifact Registry

Setup docker


```bash
gcloud auth configure-docker

gcloud services enable containerregistry.googleapis.com
```

## 6 - Build Docker

```bash
docker build .  -t  sujee/atlas-vector-search

# tag it for gcr
docker tag  sujee/atlas-vector-search:latest    gcr.io/sujee/atlas-vector-search:latest
docker tag sujee/atlas-vector-search:v-02   gcr.io/sujee/atlas-vector-search:v-02

# push
docker  push gcr.io/sujee/atlas-vector-search:latest
```