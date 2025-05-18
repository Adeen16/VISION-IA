from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.dr_model import predict_dr
from app.recommendation_model import get_recommendation
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from PIL import Image
import io

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Vision-AI is running"}


@app.post("/predict/diabetic-retinopathy")
async def dr_endpoint(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    result = predict_dr(image)
    return {"dr_probability": result, "prediction": "DR Detected" if result >= 0.5 else "Healthy"}

@app.post("/recommendation")
async def recommendation_endpoint(symptoms: list[str]):
    recommendations = get_recommendation(symptoms)
    return {"recommendations": recommendations}

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_home():
    return FileResponse("frontend/index.html")
