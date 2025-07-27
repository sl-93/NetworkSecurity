## NetworkSecurity: MLOps-Driven Network Security System
## Overview

The NetworkSecurity project is an end-to-end machine learning pipeline designed to detect and mitigate phishing attacks within a corporate network environment. Leveraging MLOps best practices, this system automates data ingestion, validation, transformation, model training, evaluation, and deployment, ensuring robust and scalable security solutions.

## Key Features
- Data Ingestion & Validation: Automates the extraction of network traffic data, performs schema validation, and detects data drift to maintain model accuracy.

- Data Transformation: Utilizes techniques like KNN imputation to handle missing values, ensuring clean and reliable datasets.

- Model Training & Evaluation: Implements Random Forest classifiers for phishing detection, with comprehensive performance metrics to assess model efficacy.

- Deployment Pipeline: Employs Docker for containerization, AWS EC2 for hosting, and FastAPI for serving predictions, facilitating seamless model deployment.

- CI/CD Integration: Utilizes GitHub Actions for continuous integration and deployment, automating testing and deployment workflows.

- Artifact Management: Integrates with AWS S3 for storing model artifacts and logs, ensuring traceability and reproducibility.

## MLOps Architecture

- The project follows a structured MLOps pipeline:

- Data Ingestion: Fetches data from MongoDB, followed by a train-test split.

- Data Validation: Applies schema validation and drift detection.

- Data Transformation: Handles missing values and encodes categorical variables.

- Model Training: Trains a Random Forest classifier and evaluates its performance.


## Technologies Used
- Programming Language: Python 3.10

- Machine Learning: scikit-learn (RandomForestClassifier, KNNImputer), pandas, numpy

- Data Storage: MongoDB

- MLOps Tools: MLflow, DAGsHub

- CI/CD: GitHub Actions

- Data Validation: Evidently

- Other Tools: awscli

## Setup Instructions
Clone the repository:

git clone https://github.com/sl-93/NetworkSecurity.git
cd NetworkSecurity
