#!/usr/bin/python3

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data time
from datetime import datetime

## for working with geocoder
import reverse_geocoder as rg


ISSURL = "http://api.open-notify.org/iss-now.json"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    iss_data = requests.get(ISSURL)
    iss_info = iss_data.json()

    #print("\niss_info:", iss_info)

    iss_timestamp = iss_info['timestamp']
    #print("\nEpoch timestamp:", iss_timestamp)
    new_iss_timestamp = datetime.fromtimestamp(iss_timestamp).strftime('%Y-%m-%d %H:%M:%S')

    #print(new_iss_timestamp)

    iss_longitude = iss_info['iss_position']['longitude']
    iss_latitude = iss_info['iss_position']['latitude']
    #print("\nLongitude:", iss_longitude)
    #print("Latitude:", iss_latitude)

    coords_tuple = (iss_latitude, iss_longitude)
    iss_loc = rg.search(coords_tuple)
    print("\niss_loc:", iss_loc)
    #print(iss_loc[0]['name'])
    iss_city = iss_loc[0]['name']
    iss_country = iss_loc[0]['cc']
    iss_location = iss_city + ", " + iss_country
    #print(iss_location)


    print("\nCurrent Location of the ISS:")
    print("Timestamp:", new_iss_timestamp)
    print("Lon:", iss_longitude)
    print("Lat:", iss_latitude)
    print("City/Country:", iss_location)


if __name__ == "__main__":
    main()

