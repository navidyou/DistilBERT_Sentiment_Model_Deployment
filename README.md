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
data = {"text": "I love coding every day!"}
response = requests.post(url, json=data)
print(response.json())
```

# Why the distilbert-base-uncased model:

## 1. Efficiency and Performance
DistilBERT is a smaller, faster, cheaper, and lighter version of BERT. It retains 97% of BERT's language understanding capabilities while being 40% smaller and 60% faster. This efficiency makes it particularly suitable for real-time applications and scenarios where computational resources are limited, such as deploying models in a web application.

## 2. Versatility in Natural Language Processing (NLP)
The model has been pre-trained on a large corpus of text, allowing it to understand the nuances of the English language (assuming the use of the uncased variant). This pre-training makes it adaptable to a wide range of NLP tasks, including sentiment analysis, with minimal additional fine-tuning required.
