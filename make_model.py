import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load your dataset into a DataFrame (replace 'your_dataset.csv' with your dataset file)
df = pd.read_csv('data.csv')

# Define X (features) and y (target)
X = df[['temp', 'humidity', 'soil_moisture']]
y = df['pump_status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set (optional)
y_pred = model.predict(X_test)

# Evaluate the model's performance (optional)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Save the trained model to a file using joblib
joblib.dump(model, 'logistic_regression_model.pkl')
