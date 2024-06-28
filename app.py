from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load the pre-trained model, label encoder, and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=JSONResponse)
async def predict(request: Request, N: float = Form(...), P: float = Form(...), K: float = Form(...), 
                  temperature: float = Form(...), humidity: float = Form(...), ph: float = Form(...), 
                  rainfall: float = Form(...)):

    # Preprocess the input
    input_values = np.array([N, P, K, temperature, humidity, ph, rainfall]).reshape(1, -1)
    input_values_scaled = scaler.transform(input_values)

    # Make a prediction
    predicted_label = model.predict(input_values_scaled)
    predicted_crop_name = label_encoder.inverse_transform(predicted_label)[0]

    return JSONResponse(content={"prediction": predicted_crop_name})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
