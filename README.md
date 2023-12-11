# SmartVision-drive
tsyp 11 ras challenge 


## Project Description
Smart Vision  is an innovative Heads-Up Display (HUD) designed to enhance road safety and optimize traffic flow, particularly in extreme weather conditions. This system leverages cutting-edge technologies, including AI, machine learning, computer vision, vehicle-to-vehicle communication, and IoT to provide real-time visualization of the road and deliver instructions to drivers.

## Installation
The installation process  involves the following steps:

1. Log in to the dedicated .
2. Install the physical boxes containing all electronic components in your vehicle.

Once these steps are completed, the application  is ready to enhance your driving experience.

## Usage
Smart Vision operates seamlessly once installed. Users can access the system through the app, and the HUD provides a clear visualization of the road, incorporating AI-driven insights for improved safety and traffic optimization.

## Configuration
No specific configuration is required as the system is designed to work efficiently under extreme weather conditions.
# code 
python/AI:
* a Python script that implements a Faster R-CNN (Region-based Convolutional Neural Network) model using TensorFlow and Keras. The model is designed for an object detection task on a custom dataset related to foggy weather conditions. Here's a summary of the key components and functionalities:

-Dataset Loading and Preprocessing
-Data Splitting
-Faster R-CNN Model Architecture
-Model Compilation
-Training
-Inference on a New Image
-Print Predictions

* a Python script that uses the OpenCV library to capture video from a webcam and displays the frames in a window. Additionally, it initializes the Google Maps API with a provided API key, although the Google Maps API functionality is not actively used in the provided code. Here's a breakdown of the key components and functionalities:

-Google Maps API Integration
-Video Capture with OpenCV
-Displaying Video Frames
-Exiting the Program
-Releasing Resources

Rasbery pi :
*a Python script utilizes the Firebase Admin SDK to interact with the Firebase Realtime Database. The script listens for real-time updates on a specific number in the database and prints the updated values. Here's a breakdown of the key components and functionalities:
-Firebase Admin SDK Initialization
-Firebase Realtime Database Reference
-Callback Function
-Listening for Real-Time Updates
-Initial Value Retrieval
-Infinite Loop
*
This Python script integrates Firebase Realtime Database, web browsing, and Pygame to display a web page in fullscreen. It appears to be designed for a specific use case, potentially related to a car's front camera and connecting to a URL specified in the Firebase Realtime Database. Here's a breakdown of the key components and functionalities:
-Firebase Admin SDK Initialization
-Pygame Initialization
-Main Loop
-Database Reference and Web Browsing
-Update Frequency
-Break Condition

*Python script utilizes the picamera library to capture video from a Raspberry Pi camera module and stream it over a network using a socket. Here's a breakdown of the key components and functionalities:
-Set Up Camera
-Set Up Socket for Streaming
-Accept Connection and Create File-Like Object
-Recording and Streaming
-Clean Up
*Python script uses the Firebase Realtime Database to obtain and compare coordinates of cars, and it establishes connections between cars based on proximity and certain conditions. Here's a breakdown of the key components and functionalities:
-Firebase Initialization
-Get Coordinates Function
-Calculate Distance Function
-Sorting and Distance Calculation
-Connection Establishment
-Connection Reset

**commands is a sequence of terminal and shell commands that install and update certain packages for Python development on a Raspberry Pi and PythonAnywhere.

***display a live stream from a Raspberry Pi on the windshield with the use of a projector with specific dimension

##Documentation and Resources :
-https://universe.roboflow.com/weatherdetection/foggy-weather (dataset)
-https://www.kaggle.com/datasets/dhruvagg/foggy-road-images

#schematics:
in this schematic we used the raspberry pi as main object because the rest components are connecting to it and we use camera and wire it to the camer port in raspberry and in the place of projector we used a screen connected to raspberry by HDMI and tow power resources one for the raspberry and the other for the screen and a button in place of starting order



## Credits
Special thanks to the following individuals who have contributed to the development of this project :

- [Ahmed Meliane]
- [Sahar Ktari]
- [Iheb Belaid]
- [Med Dhia Bechikh]
- [Yassine Ben Younes]
- [Meriam Kobbi]
- [Zied Chok]

We also extend our gratitude to IEEE ISIMa RAS SBc for their valuable contributions. Additionally, we acknowledge the use of various technologies, including AI, machine learning, computer vision, vehicle-to-vehicle communication, and IoT.
## Contact
For inquiries or support, please contact us at:
sahar.ktari@iee.org
meriem.kobbi@iee.org


---

**Note:** Smart Vision NavTech is a startup idea, and further details will be provided in the PPT presentation

