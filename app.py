from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('logistic_regression_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        soil_moisture = float(request.form['soil_moisture'])

        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame({
            'temp': [temp],
            'humidity': [humidity],
            'soil_moisture': [soil_moisture]
        })

        prediction = model.predict(input_data)

        pump_status = 'ON' if prediction[0] == 1 else 'OFF'

        return render_template('index.html', prediction=pump_status)

    return render_template('index.html', prediction=None)

# This block is used for running the app with Gunicorn on Render
if __name__ == '__main__':
    # Use Gunicorn as the web server
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable provided by Render
    app.run(debug=False, host=host, port=port)
