import firebase_admin
from firebase_admin import credentials, db

# Replace these credentials with your Firebase project credentials
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/'
})

# Reference to the specific number in your Firebase Realtime Database
number_ref = db.reference('/path/to/your/number')

# Function to update the local variable with the real-time value
def callback(event):
    global real_time_number
    real_time_number = event.data
    print(f"Real-time number updated: {real_time_number}")

# Listen for real-time updates on the specific number
number_ref.listen(callback)

# Initial value of the variable (optional)
real_time_number = number_ref.get()
print(f"Initial value of real-time number: {real_time_number}")

# Keep the script running to continue listening for updates
while True:
    pass
  
