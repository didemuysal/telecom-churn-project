# Churn Prediction with Logistic Regression

This project implements a churn prediction model using logistic regression, developed and deployed using AWS Elastic Beanstalk with Docker containers. The model is trained on a dataset of customer data and predicts the likelihood of customer churn based on their attributes.

## Technologies Used
- **Python**: For implementing the machine learning model and the API.
- **Pipenv**: For dependency management.
- **scikit-learn**: For training and validating the logistic regression model.
- **Flask**: For creating a REST API to expose the model for predictions.
- **AWS Elastic Beanstalk**: For deploying the Flask app.
- **Docker**: For containerizing the application.

## Project Structure

- **train.py**: Contains the logic for training the logistic regression model, including data preprocessing, feature extraction, and model training. The trained model is saved as a pickle file (`model_C=1.0.bin`).
- **predict.py**: Implements a Flask API that loads the trained model and exposes an endpoint `/predict` for making predictions.
- **predict-test.py**: A test script to check the functionality of the `/predict` endpoint.
- **Dockerfile**: The Docker configuration file to containerize the application for deployment.
- **data-week-3.csv**: The dataset used for training the model.

## Requirements

- Python 3.8 or higher
- Docker
- AWS Account for Elastic Beanstalk deployment
