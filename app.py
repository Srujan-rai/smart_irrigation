from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('your_saved_model.pkl')  # Replace with your model path

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        soil_moisture = float(request.form['soil_moisture'])

        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame({
            'temperature': [temperature],
            'humidity': [humidity],
            'soil_moisture': [soil_moisture]
        })

        # Make predictions
        prediction = model.predict(input_data)

        # Interpret the prediction
        pump_status = 'ON' if prediction[0] == 1 else 'OFF'

        return render_template('index.html', prediction=pump_status)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)