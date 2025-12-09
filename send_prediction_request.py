import requests

# URL of your Flask app
url = 'http://127.0.0.1:5000/predict'

# Example feature values (replace these with actual feature values)
data = {
    'features': [24500, 49000, 23500, 24500, 24300, 2100, 3100, 4100, 49281]  # Ensure these values are appropriate for your model
}

# Send a POST request with the feature values
try:
    response = requests.post(url, json=data)

    # Print the response status code for debugging
    print("Response status code:", response.status_code)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Print parsed JSON response
        prediction_result = response.json().get('prediction', 'No prediction found')
        print("The background color is predicted as :", prediction_result)  # This should contain "light" or "dark"
    else:
        # Print raw response text and error message
        print("Response text:", response.text)  # Print raw response text
        print("Error occurred:", response.json().get('error', 'Unknown error'))  # Print any error returned from the server
except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print("Request failed:", e)
