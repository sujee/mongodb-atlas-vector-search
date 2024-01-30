# Lab-3: Vector Search Using Custom Embeddings

In the previous lab, we queried movie collection with embeddings already populated.

In this lab, we will do the following:

- 👉 Experiment with few embedding models running locally (no API calls or keys required)
- 👉 Use these embedding models to populuate custom embeddings in the collection
- 👉 Then query using our custom embeddings

## Lab 3.1 - Experiment with Various Embedding Models

Follow this notebook: [local-embeddings-test.ipynb](local-embeddings-test.ipynb)

## Lab 3.2 - Populate the collection with custom embeddings

We are going to build on the previous section of generating local embeddings.  We will actually upload the embeddings to movies collection.

Follow [vector-search-custom-embeddings-populate.ipynb](vector-search-custom-embeddings-populate.ipynb)

## Lab 3.3 - Query using Custom Embeddings

Now we have every thing ready to query using the custom embeddings we just setup!

Follow [vector-search-custom-embeddings-query.ipynb](vector-search-custom-embeddings-query.ipynb)