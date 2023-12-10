from flask import Flask, render_template, Response
import requests
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/home/tsypisimasbras/cars-db-753d9-firebase-adminsdk-jvbnk-284e139beb.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cars-db-753d9-default-rtdb.firebaseio.com/'
})
raspi_ip = db.reference('https://cars-db-753d9-default-rtdb.firebaseio.com/cars/car_car123/camera-ip')

def callback(event):
    global real_time_number
    real_time_number = event.data
    



raspi_ip.listen(callback)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        # Replace the URL with your Raspberry Pi's IP address
        response = requests.get('http://{raspi_ip}:8000')
        frame = response.content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
