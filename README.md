# DistilBERT_Sentiment_Model_Deployment
# Sentiment Analysis Flask Application

This Flask application provides sentiment analysis as a service, utilizing the `distilbert-base-uncased` model from Hugging Face's Transformers library. It is designed to be easily deployable using Docker and served with Gunicorn for handling web requests efficiently.

## Features

- Sentiment analysis using the `distilbert-base-uncased` model.
- Web service built with Flask.
- Application served using Gunicorn for efficiency and scalability.
- Dockerized deployment for simplicity and consistency across environments.

## Prerequisites

- Docker installed on your local machine.
- Basic knowledge of Docker commands and operations.

## Getting Started

Follow these instructions to get the application up and running on your local machine for development, testing, or production use.

### Building the Docker Image

1. Navigate to the root directory of the project where the `Dockerfile` is located.
2. Build the Docker image using the following command:

    ```bash
    docker build -t sentiment-analysis-app .
    ```

    This command creates a Docker image named `sentiment-analysis-app` based on the Dockerfile in the current directory.

### Running the Docker Container

To run the application inside a Docker container, execute:

```bash
docker run -d -p 80:80 sentiment-analysis-app
```
### Testing the Application

With the application running, you can perform sentiment analysis by sending a POST request to the `/generate` endpoint. Use the following Python script as an example to test the service:

```python
import requests

url = 'http://localhost/generate'
data = {"text": "I love learning new things every day!"}
response = requests.post(url, json=data)
print(response.json())
```
