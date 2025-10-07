import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load env variables
load_dotenv()

app = FastAPI()

# CORS (allow frontend)
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "🚀 FastAPI backend running!"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # Placeholder: later connect to Azure Blob + Vision
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}

@app.get("/results")
def results():
    # Placeholder: later connect to Cosmos DB
    return [{"id": 1, "filename": "demo.png", "text": "Hello OCR!"}]
