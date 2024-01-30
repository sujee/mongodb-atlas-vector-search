# Vector Search Example Using Mongodb Atlas

## About

**TLDR; How to do vector search using Mongo Atlas?**  Skip to the [fun part below](#the-fun-part) if you are curiuos.

Semantic Search allows us to search by context and meaning instead of simply by keywords.

For example, let's say we are searching movie plots.

- A simple **keyword search** could be searching by **'sci-fi'**
- A **semantic search** could be **'where humans fight aliens'**

For doing semantic search, we need to convert text into  embeddings (vector of numbers).  We also need datastores that can store embeddings or vectors efficiently.  There are many [vector stores](https://aws.amazon.com/what-is/vector-databases/) coming up.  The very popular document datastore [MongoDB](https://www.mongodb.com/) now offers [Mongo Atlas](https://www.mongodb.com/atlas) that supports vector storage and search natively.

This workshop demonstrates:

- how to setup Mongo Atlas
- how to setup vector embeddings and index them
- and how to query them

You will need:

- A working Anaconda Python environment
- Mongo Atlas account (free)
- and OpenAI API Key (paid)

### The Fun Part

We will be querying movie plots using semantic search.  Here is an example.  Notice how the results not mere keyword search, but semantic search.

```text
query : fatalistic sci-fi movies
```

```text
Results: 

1
id: 573a139af29313caabcf0cff
title: Starship Troopers,
year: 1997
plot: Humans in a fascistic, militaristic future do battle with giant alien bugs in a fight for survival.

2
id: 573a139ff29313caabcff478
title: Terminator 3: Rise of the Machines,
year: 2003
plot: A cybernetic warrior from a post-apocalyptic future travels back in time to protect a 19-year old drifter and his future wife from a most advanced robotic assassin and to ensure they both survive a nuclear attack.

3
id: 573a1397f29313caabce61a5
title: Logan's Run,
year: 1976
plot: An idyllic sci-fi future has one major drawback: life must end at 30.
```

Pretty cool, eh? 😎

Follow these step by step guide to get going.

## Overall Workshop format

- **Setup** - Setup and get ready
- **Lab-1** - Connect to Atlas and query
- **Lab 2** - Perform vector search on existing collection, that already has embeddings populated.  We will use OpenAI API for this (You will need openAI key for this)
- **Lab 3** - Perform vector search using custom embeddings.  For this we will use open-source models that run locally (no API calls)
- **Lab 4** - Using RAG to query our own documents (pdf) using openAI GPT and local LLMs

## Setup

### Setup 1.1 -  Setup Python Environment

Follow [setup-python-env.md](setup-python-env.md)

## Lab-1: Connect to MongoDB Atlas

[Lab-1](lab-1-atlas-setup/README.md)



## Lab-2 - Vector Search Using OpenAI Embeddings

[lab-2](lab-2-vector-search-openai/README.md)



## Lab-3: Vector Search Using Custom Embeddings

[lab-3.md](lab-3.md)


## Lab-4: RAG (Retrieval Augmentation Generation)

[lab-4.md](lab-4.md)