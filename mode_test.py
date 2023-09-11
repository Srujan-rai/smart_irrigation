import joblib
import pandas as pd


model = joblib.load('your_saved_model.pkl')

temperature = float(input("Enter temperature (ing Celsius): "))
humidity = float(input("Enter humidity (in percentage): "))
soil_moisture = float(input("Enter soil moisture level: "))


user_input_data = pd.DataFrame({
    'temperature': [temperature],
    'humidity': [humidity],
    'soil_moisture': [soil_moisture]
})


prediction = model.predict(user_input_data)


if prediction[0] == 0:
    print("Based on the input, the pump status is OFF.")
else:
    print("Based on the input, the pump status is ON.")
