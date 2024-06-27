# from typing import Dict

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# from src.ml_model.predict import get_result

# # Define application
# app = FastAPI(
#     title="Medical Imaging app",
#     description="Medical Imaging app!",
#     version="0.1",
# )

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/api/v1/predict")
# async def predict(file: UploadFile = File(...)):
#     result = get_result(file, is_api=True)
#     return result

from typing import Dict
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.ml_model.predict import get_result

# Define application
app = FastAPI(
    title="Medical Imaging app",
    description="Medical Imaging app!",
    version="0.1",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ["image/png"]:
        raise HTTPException(status_code=400, detail="Please upload a chest X-ray image.")
    
    result = get_result(file, is_api=True)
    return result