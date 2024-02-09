import requests
import json

# Your Azure Face API endpoint and subscription key
endpoint = "https://visionapiface.cognitiveservices.azure.com/"  # Replace with your endpoint
subscription_key = "207f2ed296064e0bab05643c7115ba8d"  # Replace with your subscription key
image_url = "./Anurag.jpeg"  # URL of the image to analyze

# URL for the Face Detect API
face_api_url = endpoint + 'face/v1.0/detect'

# Request headers
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

# Request parameters
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    # Removed unsupported attributes from 'returnFaceAttributes'
}

# Making the POST request to the Azure Face API
response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    try:
        faces = response.json()
        if faces:  # Check if any faces were detected
            for face in faces:
                # Print the face ID of each detected face
                print(f"Face ID: {face.get('faceId', 'No Face ID Found')}")
        else:
            print("No faces detected.")
    except json.JSONDecodeError:
        print("Error decoding the JSON response.")
else:
    # If the response was not successful, print the error
    print(f"Error: {response.status_code}. {response.text}")
