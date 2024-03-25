# Vector Search and RAG Using MongoDB Atlas + Embedding Models +  LLMs

## About

This repo has sample code showcasing  building Vector Search / RAG (Retrieval-Augmented Generation) applications using built-in Vector Search capablities of [MongoDB Atlas](https://www.mongodb.com/atlas), embedding models and LLMs (Large Language Models).


## What is Vector Search?

[vector search explained](vector-search.md)

## Hackathon specific notes

* [2024-03-23 - Mistral AI hackathon](README-mistral-hackathon-2024-03-23.md)

## Labs

### Setup: Setup Python Environment

Follow [setup-python-env.md](setup-python-env.md)

### Lab-1: Connect to MongoDB Atlas

Setup Atlas in the cloud and make sure we can connect to it.

[Lab-1](lab-1-atlas-setup/README.md)



### Lab-2 - Vector Search Using OpenAI Embeddings

Perform vector search on an already indexed collection.  This collection is pre-populated with embeddings using an OpenAI embedding model.

[lab-2](lab-2-vector-search-openai/README.md)


### Lab-3: Vector Search Using Custom Embeddings

We will populate collections data with custom embeddings, using open source embedding models and query them.

[lab-3](lab-3-vector-search-custom/README.md)

### Sample streamlit app

[streamlit app](lab-2-vector-search-openai/vector-search-streamlit.py)

[screencast](https://drive.google.com/file/d/1pwuglLA7GTKqVlJSG-Tg-xubse6h0YP5/view?usp=drive_link) | [screenshot 1](images/streamlit-ui-2.png) | [screenshot 2](images/streamlit-ui-3b.png)


### Lab-4: RAG (Retrieval Augmentation Generation)

Index PDF files and store the index in Atlas with embeddings, and ask questions about the documents using LLMs

[lab-4](lab-4-rag/README.md)

## Dockerizing and Deploying the App

[dockerize.md](dockerize.md)

## Some Fun Benchmarks

[Vector search results using different embedding models](benchmark-search-results.md)

[Local embedding models benchmark](benchmark-embedding-models.md)

[LLMs performance on RAG](benchmark-LLMs.md)


## Useful Resources

- [RAG Series Part 1: How to Choose the Right Embedding Model for Your Application](https://www.mongodb.com/developer/products/atlas/choose-embedding-model-rag/) by Apoorva Joshi