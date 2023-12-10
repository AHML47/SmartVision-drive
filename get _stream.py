import firebase_admin
from firebase_admin import credentials, db
import webbrowser
from time import sleep

import pygame
from pygame.locals import *


pygame.init()


cred = credentials.Certificate("/home/Desktop/cars-db-753d9-firebase-adminsdk-jvbnk-284e139beb.json")

firebase_admin.initialize_app(cred, {'databaseURL': 'https://cars-db-753d9-default-rtdb.firebaseio.com/'})

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('front camera')

clock = pygame.time.Clock()

while True:
	
	partner_ref = db.reference('/cars/car_1/connect_to') #this line changed from car to ather
	url_ref =  db.reference(partner_ref.get())
    try:
        
        website_url = url_ref.get()

        if website_url:
            
             pygame_frame = pygame.surfarray.make_surface(webbrowser.open(website_url))
             screen.blit(pygame_frame, (0, 0))
			 pygame.display.flip()
			 clock.tick(60)
			 

        sleep(0.01)  # Check for updates every 10 seconds

		else :
			cap.release()
			pygame.quit()
			break 	
