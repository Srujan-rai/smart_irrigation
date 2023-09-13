import joblib
import pandas as pd

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

# Input new data
new_data = {
    'temperature': 40,
    'humidity': 0,
    'soil_moisture': 25
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