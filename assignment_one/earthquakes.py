import numpy as np

# Author: John Janzen(janzen0907)
# Class: COET295 - Assignment 1 Python

# Haversine
# formula:	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
# c = 2 ⋅ atan2( √a, √(1−a) )
# d = R ⋅ c
def calc_distance(lat1, long1, lat2, long2):
    '''Will return the distance in KM between two Lat/Long Coordinates using Haversine Formula'''
    # Mean radius of the earth in metres
    radius = 6713 ** 3
    # Honestly, i'm not to sure what all these math symbols are. I googled them
    # and named them according to the reference you provided us.
    phi_one = lat1 * np.pi / 180
    phi_two = lat2 * np.pi / 180
    delta_phi = (lat2 - lat1) * np.pi / 180
    delta_lamda = (long2 - long1) * np.pi / 180

    a = np.sin(delta_phi / 2) * np.sin(delta_phi / 2) + np.cos(phi_one) * np.cos(phi_two) * np.sin(delta_lamda / 2) * np.sin(delta_lamda / 2)
    c =  2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = radius * c

class QuakeData:
    '''Class to represent data regarding Earth Quakes'''
    def init(self, geojson):
        # Array to hold valid EarthQuaks
        self.quake_array = []

        # Get the features from the dict
        features = geojson.get('features', [])
        
        # Var to hold the datatype structure of our data
        dtype = [
            ('quake', object),
            ('magnitude', float),
            ('felt', np.int32),
            ('significance', np.int32),
            ('lat', float),
            ('long', float)
        ]

        # Var to hold the data
        data = []

        # Loop through the features
        for feature in features:
            # Check if the type is a feature
            if feature.get('type') == 'feature':
                properties = feature.get('properties', {})
                geometry = feature.get('geometry', {})

                # Ensure that properties contains the proper fields
                if 'mag' in properties and 'time' in properties and 'felt' in properties and 'sig' in properties and 'type' in properties:
                    # Check that point does not exist 
                    if geometry.get('type') == 'Point' and 'coordinates' in geometry and len(geometry['coordinates'] == 3):
                        
                        # Get the data and build the array
                        quake = feature
                        magnitude = properties['mag']
                        felt = properties['felt']
                        signifigance = properties['sig']
                        lat, long = geometry['coordinates'][:2]
                        
                        # Add the data to the list
                        data.append((quake, magnitude, felt, signifigance, lat, long))

        # If the data is correct. Convert it to a nump array
        if data:
            self.quake_array = np.array(data, dtype=dtype)


    def set_location_filter(latitude, longitude, distance):
        '''Returns Quakes within the distance the distance of the latitude and longitude being passed in'''
        # Test commit
        junk = 'delete me'



