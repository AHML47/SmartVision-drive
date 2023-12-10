import cv2
import googlemaps


google_maps_key = 'VOTRE_CLE_API'
gmaps = googlemaps.Client(key=google_maps_key)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

   
    cv2.imshow('Location Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
