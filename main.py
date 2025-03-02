import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
with open("model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]

# Define input schema (matching model.feature_names_in_)
class CarFeatures(BaseModel):
    Levy: float
    Manufacturer: int
    Model: int
    Prod_year: int  # Matches "Prod. year"
    Category: int
    Leather_interior: int  # Matches "Leather interior"
    Engine_volume: float  # Matches "Engine volume"
    Mileage: int
    Cylinders: float
    Doors: int
    Wheel: int
    Color: int
    Airbags: int
    Drive_4x4: bool
    Drive_front: bool
    Drive_rear: bool
    Gear_box_automatic: bool
    Gear_box_manual: bool
    Gear_box_tiptronic: bool
    Gear_box_variator: bool
    Fuel_cng: bool
    Fuel_diesel: bool
    Fuel_hybrid: bool
    Fuel_hydrogen: bool
    Fuel_lpg: bool
    Fuel_petrol: bool
    Fuel_plug_in_hybrid: bool  # Matches "Fuel_plug-in hybrid"

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running!"}

@app.post("/predict")
def predict_price(features: CarFeatures):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([features.dict()])

        # Column name mapping to match model feature names
        column_mapping = {
            "Prod_year": "Prod. year",
            "Leather_interior": "Leather interior",
            "Engine_volume": "Engine volume",
            "Fuel_plug_in_hybrid": "Fuel_plug-in hybrid"
        }

        # Apply column renaming
        input_df.rename(columns=column_mapping, inplace=True)

        # Ensure input matches model's expected features
        model_features = model.feature_names_in_
        input_df = input_df[model_features]  # Keep only necessary columns

        # Make prediction
        predicted_price = model.predict(input_df)[0]

        return {"predicted_price": float(predicted_price)}

    except Exception as e:
        return {"error": str(e)}

print("✅ FastAPI Endpoints Created Successfully!")

