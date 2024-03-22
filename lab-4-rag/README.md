# Lab-4: RAG (Retrival Augmented Generation) with DB Atlas

In this lab, we will do the following:

- 👉 Load PDF documents
- 👉 Use embedding models to calculate embeddings for PDF documents
👉 Upload them into Atlas
- 👉 Then query these PDF documents

## Architecture and Dataflow

![](../images/rag-overview-2.png)

And here is the result of sample query

![](../images/rag-2-answer.png)

## Lab 4.1 - Calculate Embeddings for the documents

First step is reading, parsing, indexing PDFs.  

Very importantly we will also calculate embeddings for the documents.

And the documents along with embeddings will be uploaded into Atlas to query later.

These are some of the embedding options:

### 4.1 A: OpenAI embedding model - TODO

- API based access
- will need an OPENAI API key
- See notebook : [rag-10k-a-populate-embeddings-openai.ipynb](rag-10k-a-populate-embeddings-openai.ipynb) (TODO)

### 4.1 B: Mistral AI embedding model

- API based access
- Will need MISTRAL API key
- See notebook [rag-10k-a-populate-embeddings-mistral.ipynb](rag-10k-a-populate-embeddings-mistral.ipynb)

### 4.1 C: Open source embedding models

- Models will run locally
- Medium to large models will benefit from GPU
- See notebook: [rag-10k-a-populate-embeddings-open.ipynb](rag-10k-a-populate-embeddings-open.ipynb)

## Lab 4.2 - Query documents using LLM

Now that the documents are in Atlas, let's ask some questions about the documents.

Here we can have a combination of **embedding models** and **LLM**.  See below for some examples

| Embedding model                  | LLM                      | Code                                                                                                         |
|----------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------|
| OpenAI embed (access via API)    | OpenAI (access via API)  | TODO                                                                                                         |
| Open source model (runs locally) | OpenAI (access via API)  | [rag-10k-b-query-open-embeddings-openAI-llm.ipynb](rag-10k-b-query-open-embeddings-openAI-llm.ipynb)         |
|                                  |                          |                                                                                                              |
| Mistral embed (access via API)   | Mistral (access via API) | [rag-10k-b-query-mistral-embeddings-mistral-llm.ipynb](rag-10k-b-query-mistral-embeddings-mistral-llm.ipynb) |
| Open source model (runs locally) | Mistral (access via API) | [rag-10k-b-query-open-embeddings-mistral-llm.ipynb](rag-10k-b-query-open-embeddings-mistral-llm.ipynb)       |


## Lab 4.3 - Test run a local LLM

Running this notebook to see how well you can run an LLM 

[test-local-llm.ipynb](test-local-llm.ipynb)


## Lab 4.4 - Query documents using local LLMs

Let's query documents, this time using a LLM (Large Language Model) running locally on our laptop!

Follow [rag-10k-c-query-local-llm.ipynb](rag-10k-c-query-local-llm.ipynb)