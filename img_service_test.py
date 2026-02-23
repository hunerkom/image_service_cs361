# CS 361 Image Service Microservice Test
# Group 33, David & Mason
# Description: Verifies that the image service properly retrieves and returns images as intended.
# Communication Protocol: ZeroMQ

import zmq

# Setup ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Ask for an image named test
filename = "test"   # try without .png on purpose
print(f"Requesting: {filename}")

socket.send_string(filename)

# Receive response
reply = socket.recv()

# Check if it's an error or image bytes
try:
    # Try decoding as UTF-8 (error messages are strings)
    message = reply.decode("utf-8")
    if message.startswith("ERROR"):
        print("Server replied with error:", message)
    else:
        print("Received unexpected text:", message)
except UnicodeDecodeError:
    # If decoding fails, it's binary image data
    print(f"Received {len(reply)} bytes of image data")

    # Save the image to verify
    with open("received_test_image.png", "wb") as f:
        f.write(reply)
    print("Saved as received_test_image.png")

