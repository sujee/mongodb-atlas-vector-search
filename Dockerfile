FROM python:3.11

WORKDIR /app

# Install all required libraries
COPY requirements-docker.txt ./
RUN  pip install -r requirements-docker.txt

# Copy resources
COPY  images/banner-1.png ./images/
COPY  AtlasClient.py\
      OpenAIClient.py \
      .env \
      lab-2-vector-search-openai/embeddings_openai.json \
      lab-2-vector-search-openai/vector-search-streamlit.py \
      ./

# RUN ls /app

EXPOSE 8501
#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "vector-search-streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]