#!/usr/bin/env python3

import requests
import datetime

URL = "http://api.open-notify.org/iss-now.json"

def main() :
    resp = requests.get(URL).json()

    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    time = datetime.datetime.fromtimestamp(resp["timestamp"])

    print(f"""
    Timestamp: {time}
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    """)

if __name__ == "__main__":
    main()
