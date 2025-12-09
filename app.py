from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

# Load your Voting Classifier model
model = joblib.load('voting_classifier (1).pkl')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route for the homepage to serve the HTML form
@app.route('/')
def home():
    return render_template('VIBRANT FUSION NEXUS.html')  # Ensure this HTML file is in a 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.json
    print("Received data:", data)  # Log received data for debugging
    
    # Prepare features
    features = np.array(data['features']).reshape(1, -1)  # Adjust shape if needed
    
    # Make prediction
    try:
        prediction = model.predict(features)
        print("Prediction:", prediction)  # Log the prediction
        
        # Mapping prediction to light/dark
        if prediction == 0:
            result = "DARK"  # Assuming class 0 corresponds to light
        elif prediction == 1:
            result = "LIGHT"   # Assuming class 1 corresponds to dark
        elif prediction == 2:
            result = "LIGHT"  # Assuming class 2 corresponds to light
        else:
            raise ValueError("Prediction out of range")

    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({'error': str(e)}), 500
    
    # Return prediction as JSON response
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
