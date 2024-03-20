# Lab-4: RAG (Retrival Augmented Generation) with DB Atlas

In this lab, we will do the following:

- 👉 Load PDF documents
- 👉 Use embedding models to calculate embeddings for PDF documents
👉 Upload them into Atlas
- 👉 Then query these PDF documents

## Architecture and Dataflow

![](../images/rag-1.svg)

And here is the result of sample query

![](../images/rag-2-answer.png)

## Lab 4.1 - Calculate Embeddings for the documents

First step is reading, parsing, indexing PDFs.  

Very importantly we will also calculate embeddings for the documents.

And the documents along with embeddings will be uploaded into Atlas to query later.

These are some of the embedding options:

- 4.1 A) **OpenAI** embedding model - TODO
    - API based access
    - will need an OPENAI API key
    - See notebook : [rag-10k-a-populate-embeddings-openai.ipynb](rag-10k-a-populate-embeddings-openai.ipynb) (TODO)
- 4.1 B) **Mistral AI embedding model**.
    - API based access
    - Will need MISTRAL API key
    - See notebook [rag-10k-a-populate-embeddings-mistral.ipynb](rag-10k-a-populate-embeddings-mistral.ipynb)
- 4.1 C) **Local / embedding models**
    - Models will run locally
    - Medium to large models will benefit from GPU
    - See notebook: [rag-10k-a-populate-embeddings-local.ipynb](rag-10k-a-populate-embeddings-local.ipynb)

## Lab 4.2 - Query documents using OpenAI LLM (ChatGPT)

Now that the documents are in Atlas, let's ask some questions about the documents.  Our LLM here will be OpenAI Chat GPT

Follow [rag-10k-b-query-openAI.ipynb](rag-10k-b-query-openAI.ipynb)

## Lab 4.3 - Test run a local LLM

Running this notebook to see how well you can run an LLM 

[test-local-llm.ipynb](test-local-llm.ipynb)


## Lab 4.4 - Query documents using local LLMs

Let's query documents, this time using a LLM (Large Language Model) running locally on our laptop!

Follow [rag-10k-c-query-local-llm.ipynb](rag-10k-c-query-local-llm.ipynb)