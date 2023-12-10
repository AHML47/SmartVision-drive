import picamera
import socket
import time

# Set up the camera
camera = picamera.PiCamera()

# Set resolution (adjust as needed)
camera.resolution = (640, 480)

# Set up the socket for streaming
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('wb')

try:
    # Start recording and streaming
    camera.start_recording(connection, format='h264')
    camera.wait_recording(3600)  # Adjust the duration as needed

finally:
    # Clean up
    camera.stop_recording()
    connection.close()
    server_socket.close()
  
