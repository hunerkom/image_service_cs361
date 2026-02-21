# CS 361 Image Service Microservice
# Group 33, David & Mason
# Description: This microservice handles image retrieval and returns a .jpg image given an image name from the client.
# Communication Protocol: ZeroMQ
# Citation: https://github.com/jeffbass/imagezmq   -- Using this repo for reference

import os
import cv2
import zmq
import time

# Setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Image service listening on port 5555...")

while True:
    # Wait for request
    filename = socket.recv_string()
    print(f"Received request for: {filename}")
    
    # Add .png if not present
    if not filename.endswith('.png'):
        filename += '.png'

    # Check if file exists in images folder
    # All images will be in the images subfolder
    image_path = os.path.join("images", filename)
    
    if os.path.exists(image_path):
        # Read and send the image
        image = cv2.imread(image_path)
        _, buffer = cv2.imencode('.png', image)                     # Returns a status code and the encoded image
        socket.send(buffer.tobytes())
        print(f"Sent image: {filename}")
    else:
        # Send error message
        socket.send_string(f"ERROR: File {filename} not found")
        print(f"File not found: {filename}")
        
    continue
