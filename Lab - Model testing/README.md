# Serving an NLP Model (Transformer) using FastAPI

This repository provides a step-by-step guide for serving a Question Answering (QA) model based on the DistillBERT transformer architecture using FastAPI.
The model is pre-trained on the SQUAD dataset (Stanford Question Answering Dataset).



## Part 1:  Serve an NLP model (transformer) using FastAPI

We will use a QA (Question answering) model and serve it using FastAPI and we'll try a tool to query our API using curl requests (postman).

![Lab - Model testing](/Screens/FastAPI_QA.png)

![Lab - Model testing](/Screens/FastAPI_QA_Response.png)

![Lab - Model testing](/Screens/FastAPI_QA_postman.png)

## Part 2: Containerizing the API using Docker
To save time in production and facilitate the deployment process, it is essential to use Docker.
![FastAPI](Lab - Model testing/Screens/FastAPI_Docker.png)

## Part 3: Serving a Transformer Model using TFX
TFX provides a faster and more efficient way to serve deep learning models. But it has some 
important key points that you need to understand before using it. The model must be a 
registered model type from TensorFlow so that it can be used by TFX

## Part 4: Load Testing using Locust
We will use it to test the loading of the three methods seen previously:
- Using fastAPI only, 
- Using Dockerized fastAPI and 
- By serving the model with TFX using fastAP

![FastAPI](Lab - Model testing/Screens/locust_fastapi_QA.png)
![FastAPI](Lab - Model testing/Screens/results_locust.png)

