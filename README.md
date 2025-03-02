# DS-Project-_-Jinsheng-Yu-Shanyu-Wang
# Car Price Prediction API 🚗

## Overview
This project predicts car prices based on input features using a machine learning model. The API is built with **FastAPI** and deployed on **Render**.

## Features
- **Predicts car prices** based on input features
- **Uses XGBoost model** for high accuracy
- **Deployed on Render** for public access

## Setup & Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/car-price-prediction.git
   cd car-price-prediction
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API**:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```
   - API runs at: `http://127.0.0.1:8000/`
   - Documentation: `http://127.0.0.1:8000/docs`

## Live API
- **API URL**: [https://car-price-api-m4xn.onrender.com](https://car-price-api-m4xn.onrender.com)
- **Docs**: [https://car-price-api-m4xn.onrender.com/docs](https://car-price-api-m4xn.onrender.com/docs)

## Example Request
```json
{
  "Levy": 1500,  
  "Manufacturer": 3,  
  "Model": 25,  
  "Prod_year": 2018,  
  "Category": 2,  
  "Leather_interior": 1,  
  "Engine_volume": 2.0,  
  "Mileage": 45000,  
  "Cylinders": 4,  
  "Doors": 4,  
  "Wheel": 1,  
  "Color": 5,  
  "Airbags": 6,  
  "Drive_4x4": false,  
  "Drive_front": true,  
  "Drive_rear": false,  
  "Gear_box_automatic": true,  
  "Gear_box_manual": false,  
  "Gear_box_tiptronic": false,  
  "Gear_box_variator": false,  
  "Fuel_cng": false,  
  "Fuel_diesel": false,  
  "Fuel_hybrid": false,  
  "Fuel_hydrogen": false,  
  "Fuel_lpg": false,  
  "Fuel_petrol": true,  
  "Fuel_plug_in_hybrid": false  
}
```

## Response
```json
{
    "predicted_price": 8789.54...
}
```

## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss.

## License
MIT

