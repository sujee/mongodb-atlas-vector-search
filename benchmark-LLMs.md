# Benchmark for doing RAG with LLMs

These benchmarks are done on this machine

- Ubuntu 22.04 with Nvidia CUDA drivers (Driver Version: 525.147.05   CUDA Version: 12.0)
- Intel 8 core CPU @ 3.6 GHZ
- 32 GB Memory
- Nvidia GEFORCE 2070 with 8 GB memory

I measured timings to various questions I asked here (both LLMs got same questions)

Using OpenAI : [lab-4-rag/rag-10k-b-query-openAI.ipynb](lab-4-rag/rag-10k-b-query-openAI.ipynb)

Using local LLM : [lab-4-rag/rag-10k-c-query-local-llm.ipynb](lab-4-rag/rag-10k-c-query-local-llm.ipynb)

My Local LLM:

- mistral-7b-instruct-v0.2.Q4_K_M.gguf (4 bit quantized, medium).  [Model card here](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
- Smallest 'recommended' model
- Model size : 4.37 GB
- when using GPU, the model takes about 6.5 GB or GPU memory
- I am running it through [llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/) with GPU support compiled in


|               | openAI API  (includes network latency) | local LLM (GPU) | Local LLM (CPU)  |
|---------------|----------------------------------------|-----------------|------------------|
| Time to query |  1 - 2 secs                           | 2 - 5 secs      | 2  - 7 minutes ! |
|               |                                        |                 |                  |