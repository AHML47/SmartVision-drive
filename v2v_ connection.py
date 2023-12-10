import firebase_admin
from firebase_admin import credentials, db
import math

cred = credentials.Certificate("/home/Desktop/cars-db-753d9-firebase-adminsdk-jvbnk-284e139beb.json")

firebase_admin.initialize_app(cred, {'databaseURL': 'https://cars-db-753d9-default-rtdb.firebaseio.com/'})
coordinates_ref = db.reference('/cars/')
def get_coordinates():
    coordinates_ref = db.reference('/cars/')  # Replace with the path to your coordinates node
    coordinates_snapshot = coordinates_ref.get()

    coordinates_list = []

    if coordinates_snapshot:
        # Iterate through all child nodes
        for object_id, object_data in coordinates_snapshot.items():
            coordinates_list.append({
                'id': object_id,
                'name': object_data.get('username', ''),
                'x': object_data.get('position-h', 0),
                'y': object_data.get('position-v', 0)
            })

    return coordinates_list


def calculate_distance(coord1, coord2):
    
    
    coord1['x'] = radians(coord1['x'])
    coord2['x'] = radians(coord2['x'])
    coord2['y'] = radians(coord2['y'])
    coord2['y'] = radians(coord2['y'])
      
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a)) 
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
if __name__ == "__main__":
	while(True):
		all_coordinates = get_coordinates()

    
		sorted_coordinates = sorted(all_coordinates, key=lambda coord: (coord['name'], coord['y']))

		for i in range(len(sorted_coordinates)):
			for j in range(i+1, len(sorted_coordinates)):
				dist = calculate_distance(sorted_coordinates[i], sorted_coordinates[j])
				if(dist<=0.005 and abs(sorted_coordinates[i]['x']-sorted_coordinates[i]['j'])<0.000000000001):
					if (sorted_coordinates[i]['y']<sorted_coordinates[j]['y']):
						connection_ref = db.reference('/cars/car_'+str(sorted_coordinates[i]['name']+'/connect_to')
						connection_set = connection_ref.set('/cars/car_'+str(sorted_coordinates[j]['name']+'/connect_to')
					elif(sorted_coordinates[i]['y']>sorted_coordinates[j]['y']) :
						connection_ref = db.reference('/cars/car_'+str(sorted_coordinates[j]['name']+'/connect_to')
						connection_set = connection_ref.set('/cars/car_'+str(sorted_coordinates[i]['name']+'/connect_to')
				else :
					connection_ref = db.reference('/cars/car_'+str(sorted_coordinates[i]['name']+'/connect_to')
					connection_set = connection_ref.set('')
					connection_ref = db.reference('/cars/car_'+str(sorted_coordinates[j]['name']+'/connect_to')
					connection_set = connection_ref.set('')
			

                                  
