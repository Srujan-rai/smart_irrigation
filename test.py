import joblib
import pandas as pd

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

temperature=float(input("enter the temperature"))
humidity=float(input("enter the humidity"))
soil_moisture=float(input("enter the soil_moisture"))
new_data = {
    'temp': temperature,
    'humidity': humidity,
    'soil_moisture': soil_moisture
}

# Prepare the input data as a DataFrame
new_data_df = pd.DataFrame([new_data])

# Make predictions
prediction = model.predict(new_data_df)

# Interpret the prediction
if prediction[0] == 0:
    print("The pump status is OFF.")
else:
    print("The pump status is ON.")