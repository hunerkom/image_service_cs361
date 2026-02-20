361_image_service
CS 361 Microservice that returns an image file using ZeroMQ communication.

Group 33: David & Mason

Description
This microservice handles image retrieval and returns .jpg images given an image name from the client. It uses imagezmq and ZeroMQ for efficient communication between client and server.

pip install -r requirements.txt

Communciation contract: REFINE LATER ON but send a string with the needed file's name. The service will send back a .png file.
