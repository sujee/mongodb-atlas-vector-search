# Vector Search Example Using MongoDB Atlas

## About

This repo has sample code showcasing  building Vector Search / RAG (Retrieval-Augmented Generation) applications using built-in Vector Search capablities of [MongoDB Atlas](https://www.mongodb.com/atlas) and LLMs (Large Language Models).


## What is Vector Search?

"Vector Search  represents data as vectors in a high-dimensional space and performs searches based on the similarity between these vectors"

For example, let's say we are searching movie plots.

- A simple **keyword search** could be searching by **'sci-fi'**
- A **vector search** could be **'where humans fight aliens'**

Here is an example.  Notice how the results not mere keyword search.

```text
query : fatalistic sci-fi movies
```

```text
Results: 

1
title: Starship Troopers,
year: 1997
plot: Humans in a fascistic, militaristic future do battle with giant alien bugs in a fight for survival.

2
title: Terminator 3: Rise of the Machines,
year: 2003
plot: A cybernetic warrior from a post-apocalyptic future travels back in time to protect a 19-year old drifter and his future wife from a most advanced robotic assassin and to ensure they both survive a nuclear attack.

3
title: Logan's Run,
year: 1976
plot: An idyllic sci-fi future has one major drawback: life must end at 30.
```

Pretty cool, eh? 😎

## Labs

### Setup: Setup Python Environment

Follow [setup-python-env.md](setup-python-env.md)

### Lab-1: Connect to MongoDB Atlas

Setup Atlas on the cloud and make sure we can connect.

[Lab-1](lab-1-atlas-setup/README.md)



### Lab-2 - Vector Search Using OpenAI Embeddings

Perform vector search on already indexed collection.  This collection is pre-populated with embeddings using OpenAI embedding model.

[lab-2](lab-2-vector-search-openai/README.md)


### Lab-3: Vector Search Using Custom Embeddings

We will populate collections data with custom embeddings, using open source embedding models and query them.

[lab-3](lab-3-vector-search-custom/README.md)


### Lab-4: RAG (Retrieval Augmentation Generation)

Index PDF files and store in Atlas with embeddings, and ask questions about the documents using LLMs

[lab-4](lab-4-rag/README.md)

## Some Fun Benchmarks

[Local embedding models benchmark](benchmark-embedding-models.md)

[LLMs performance on RAG](benchmark-LLMs.md)
