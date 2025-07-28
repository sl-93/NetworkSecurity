import os, sys
from dotenv import load_dotenv
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.constants.training_pipeline import (DATA_INGESTION_DATABASE_NAME, 
                                                         DATA_INGESTION_COLLECTION_NAME)

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from fastapi.responses import RedirectResponse
import pandas as pd


load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(mongo_db_url)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful!")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)