# Cloud-native-AI-ML 
# Assignment :



# Student Mental Health Prediction


## Overview

This project focuses on predicting student mental health, specifically determining the presence or absence of depression. The workflow includes preprocessing data, training machine learning models, tracking performance with MLflow, saving the best model in ONNX format, and creating REST APIs with FastAPI and Flask. Additionally, both the machine learning model and the application are packaged as Docker containers for deployment flexibility.


## Dataset

The dataset used in this project contains information relevant to student mental health, including features that contribute to predicting depression.

- 'Choose your gender': 'gender'
- 'Age ' : 'age'
- 'What is your course?': 'major'
- 'Your current year of Study': 'year'
- 'What is your CGPA?': 'CGPA'
- 'Marital status': 'Marriage'
- 'Do you have Depression?': 'Depression'
- 'Do you have Anxiety?': 'Anxiety'
- 'Do you have Panic attack?': 'Panic'
- 'Did you seek any specialist for a treatment?': 'treatment'

## Training 5 ML Models

- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Random Forest
- Decision Tree
- Gradient Boosting Classifier

## Folder: MLflow

Train five machine learning models using various algorithms.

### Tracking Model Performance, Versions, and Parameters

Use MLflow to track model performance metrics, versions, and parameters.

### Saving Best Model in ONNX Format

Save the best-performing model in the ONNX format for interoperability.

### Serializing Preprocessing Transformations

Serialize and save preprocessing transformations using the transformers API in pickle format.

## Folder: FastAPI

### Creating a REST API with FastAPI

Use FastAPI to create a REST API for serving machine learning models.

### Packaging Model as a Docker Container

Package the machine learning model as a Docker container for easy deployment and scalability.

## Folder: Flask

### Creating a Dedicated Application with Flask

Develop a dedicated application using Flask to consume the machine learning API.

### Packaging Application as a Docker Container

Package the Flask application as a Docker container for streamlined deployment.

