# Readme for Mistral Hackathon (2024-03-23)

## shortlink: bit.ly/mongodb-mistral

## Overview

This workshop will demonstrate how to develop a RAG application of querying PDF documents using:

* MongoDB Atlas as a vector storage
* Mistral as embedding model
* Mistral as LLM

(This workshop is part of workshop collection covering vector search, embeddings and LLMs.  You can access all the workshops in [README.md](README.md))

Slide: [1](https://docs.google.com/presentation/d/1-lJ9azv1AVbTnFLEj6TgJgq7pOUBMiLVjSDrMz50PiQ/edit?usp=sharing) |  [2](https://docs.google.com/presentation/d/1lzaZMlu_2m8juuav-Jo7z_fFVifGhTXROvxQdIPZScE/edit?usp=sharing)

Here is an overview of RAG workflow

![](images/rag-overview-3-mistral.png)


See below for [handy references](#handy-references)

## What do you need to run this workshop?

* A (free) MongoDB Atlas account;  Sign up here : https://www.mongodb.com/cloud/atlas/register
* A Mistral API key; Get it here: https://console.mistral.ai/
* A Jupyter notebook environment.  [Google Colab](https://colab.research.google.com/) (recommended) or a Python dev environment.

## Understanding LLM and Vector Store!

    "Vector stores reduce search space by providing relevant documents to LLM"

A simple way to think about this is a librarian helping out a student by giving relevant books (click for larger image)

<a href="images/LLM-and-vector-storage.jpeg"><img src="images/LLM-and-vector-storage.jpeg" width="40%"></a>

## Step-1: Setup Atlas

Follow [this quick start](lab-1-atlas-setup/setup-atlas.md) to setup Atlas.

[Test your connection to Atlas](lab-1-atlas-setup/atlas-test.ipynb)

## Step-2: Process documents and load them to Atlas

Here we will be reading, parsing, indexing PDFs.  

Very importantly we will also calculate **embeddings** for the documents.

And the documents along with embeddings will be stored in Atlas to query later.

| Embedding model | Embedding size       | details                                | Code                                                                                                 |
|-----------------|----------------------|----------------------------------------|------------------------------------------------------------------------------------------------------|
| Mistral         | 1024                 | API access (will need MISTRAL API KEY) | [rag-10k-a-populate-embeddings-mistral.ipynb](lab-4-rag/rag-10k-a-populate-embeddings-mistral.ipynb) |
| Open (various)  | varies (384 to 1024) | Runs locally                           | [rag-10k-a-populate-embeddings-open.ipynb](lab-4-rag/rag-10k-a-populate-embeddings-open.ipynb)       |



## Step-3: Query Documents with LLM

Now that the documents are in Atlas, let's ask some questions about the documents.

Here we can have a combination of **embedding models** and **LLM**.  See below for some examples

| Embedding model                  | LLM                      | Code                                                                                                         |
|----------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------|
| Mistral embed (access via API)   | Mistral (access via API) | [rag-10k-b-query-mistral-embeddings-mistral-llm.ipynb](lab-4-rag/rag-10k-b-query-mistral-embeddings-mistral-llm.ipynb) |
| Open source model (runs locally) | Mistral (access via API) | [rag-10k-b-query-open-embeddings-mistral-llm.ipynb](lab-4-rag/rag-10k-b-query-open-embeddings-mistral-llm.ipynb)       |

## Extra: Run local LLM

This notebook demonstrates how to run [Mistral instruct 7b 0.2 model](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) locally

| Embedding model                  | LLM                                    | Code                                                                         |
|----------------------------------|----------------------------------------|------------------------------------------------------------------------------|
| Open source model (runs locally) | Mistral-Instruct-7B-v02 (runs locally) | [rag-10k-c-query-local-llm-mistral-instruct-1.ipynb](lab-4-rag/rag-10k-c-query-local-llm-mistral-instruct-1.ipynb) |


### Benchmark: CPU vs. GPU

| LLM           | Mistral API          | Mistral 7B on GPU                                                                         | Mistral 7B on CPU                                                                                  |
|---------------|----------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Response time | 2 - 7 seconds        | 2 - 5 secs                                                                                | 90 - 150 secs                                                                                      |
| Model         | Mistral-large-latest | mistral-7b-instruct-v0.2.Q4_K_M.gguf                                                      | mistral-7b-instruct-v0.2.Q4_K_M.gguf                                                               |
| Performance   |                      | ~ 50 tokens / sec                                                                         | ~ 5 tokens / sec                                                                                   |
| Hardware      |                      | - Ubuntu Linux 22.04<br>- 16 core CPU <br>- 32 G Memory <br>- Nvidia 2070 with 8GB memory | - Ubuntu Linux 22.04<br>- 16 core CPU<br>- 32 G Memory<br>- Nvidia 2070 with 8GB memory (disabled) |


## Extra 2: Try other labs

[Start here](README.md) for other workshops on Atlas vector search, embeddings, RAG and LLMS


## Handy References

### MongoDB Atlas

- Run on cloud, easy, free : https://mongodb.com
- Local
    - [Local setup](https://www.mongodb.com/community/forums/t/introducing-a-local-experience-for-atlas-atlas-search-and-atlas-vector-search-with-the-atlas-cli/246403)
    - [Local with Docker Compose](https://www.mongodb.com/docs/atlas/cli/stable/atlas-cli-deploy-docker/)
- [Atlas vector search forum](https://www.mongodb.com/community/forums/c/atlas/vector-search/168) - for posting questions and getting help

### Tutorials

- [MongoDB Semantic Search Tutorial (Python, Java, Node.js)](https://www.mongodb.com/products/platform/atlas-vector-search)
- [RAG Series Part 1: How to Choose the Right Embedding Model for Your Application](https://www.mongodb.com/developer/products/atlas/choose-embedding-model-rag/)