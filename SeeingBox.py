#!/usr/bin/python3

import picamera
import httplib
import urllib
import base64
import json
import re
from os import system
from gpiozero import Button

# CHANGE {YOUR_MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = "{YOUR_MS_API_KEY}"

# Define the GPIO pin number for the camera button (BCM numbering)
camera_button = Button(27)

# Initialize the PiCamera object
camera = picamera.PiCamera()

# Setup headers for the Microsoft Vision API request
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}

# Define the parameters for the Vision API request
params = urllib.urlencode({
    'visualFeatures': 'Description',
})

# Loop indefinitely waiting for the button press to capture an image
while True:
    # Wait for the button to be pressed
    camera_button.wait_for_press()
    
    # Capture the image and save it to a temporary file
    camera.capture('/tmp/image.jpg')

    # Read the image file into a binary format
    body = open('/tmp/image.jpg', "rb").read()

    try:
        # Establish a connection to the Microsoft Vision API endpoint
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        
        # Send the POST request to the Vision API with the image and headers
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        
        # Get the response from the Vision API
        response = conn.getresponse()
        
        # Parse the JSON response
        analysis = json.loads(response.read())
        
        # Extract the caption from the analysis results
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        
        # Validate the caption text before using it in the system call
        # The regex ensures only alphabetic characters and spaces are allowed
        if re.match("^[a-zA-Z ]+$", image_caption):
            # Use espeak to vocalize the caption
            system('espeak -ven+f3 -k5 -s120 "' + image_caption + '"')
        else:
            # Fallback message if the caption contains invalid characters
            system('espeak -ven+f3 -k5 -s120 "I do not know what I just saw"')

        # Close the connection to the Vision API
        conn.close()

    except Exception as e:
        # Print any exceptions that occur
        print(e.args)
