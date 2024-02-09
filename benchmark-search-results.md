# Comparing Vector Search Results for Different Embedding Models

This is a fun experiment to see how differnet embeddings affect the search results.

MongoDb Atlas is neutral on embeddings.  We can plug in any embedding model.

Here I have setup two embeddings using two different models

- OpenAI embedding model (text-embedding-ada-002): This model is available via API call only.  [more information](https://openai.com/blog/new-and-improved-embedding-model)
- BAAI/bge-small-en-v1.5: This is an open source model. [more information](https://huggingface.co/BAAI/bge-small-en-v1.5)

## Results

And here are the top-5 vector search results, for the query :

**"humans fighting aliens"**

The search score in bracket (0.85) is a number between 0.0 and 1.0.  Closer to 1.0 is better!  We see OpenAI models are scoring higher in the 0.8 range.  Open source model (BAAI/bge-small-en-v1.5) is scoring in 0.6 - 0.7 range.  Not bad!

**Update:** ON Jan 25, 2024, OpenAI has announced new embedding models: `text-embedding-3-small` and `text-embedding-3-large`. [Read more](https://openai.com/blog/new-embedding-models-and-api-updates).  I will update the results with the new models.

Overall the Top-5 results are pretty similar.  Which is good to see.

You can read the plot lines to see evaulate the matches yourself 😄

---

|             | OpenAI Embedding (text-embedding-ada-002)                                                                                                                                     | BAAI/bge-small-en-v1.5                                                                                                                                                                                                |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feature     | API acceess only                                                                                                                                                              | Open Source.  Runnable locally                                                                                                                                                                                        |
| Search Rank |                                                                                                                                                                               |                                                                                                                                                                                                                       |
| 1           | **V: The Final Battle** (0.85) :  A small group of human resistance fighters fight a desperate guerilla war against the genocidal extra-terrestrials who dominate Earth.      | **Independence Day** (0.77) :  The aliens are coming and their goal is to invade and destroy Earth. Fighting superior technology, mankind's best weapon is the will to survive                                        |
| 2           | **Falling Skies** (0.85) : Survivors of an alien attack on earth gather together to fight for their lives and fight back.                                                     | **Falling Skies** (0.73) :  Survivors of an alien attack on earth gather together to fight for their lives and fight back.                                                                                            |
| 3           | **Starship Troopers** (0.84) : Humans in a fascistic, militaristic future do battle with giant alien bugs in a fight for survival.                                            | **Starship Troopers** (0.72) :  Humans in a fascistic, militaristic future do battle with giant alien bugs in a fight for survival.                                                                                  |
| 4           | **Battlefield Earth** (0.84) :  After enslavement & near extermination by an alien race in the year 3000, humanity begins to fight back.                                      | **Enemy Mine** (0.68) :  A soldier from Earth crash-lands on an alien world after sustaining battle damage. Eventually he encounters another survivor, but from the enemy species he was fighting; they band together |
| 5           | **Independence Day** (0.81) : The aliens are coming and their goal is to invade and destroy Earth. Fighting superior technology, mankind's best weapon is the will to survive | **V: The Final Battle**  (0.68) :  A small group of human resistance fighters fight a desperate guerilla war against the genocidal extra-terrestrials who dominate Earth.                                             |

---

