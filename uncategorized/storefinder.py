from datetime import timedelta
from operator import itemgetter
import os
import time

import googlemaps
from dotenv import load_dotenv

# ORIGIN_ADDRESS = "Torsgatan 53, 113 37 Stockholm, Sweden"
ORIGIN_ADDRESS = "Rålambsvägen 54, 112 56 Stockholm, Sweden"
QUERY = "Grocery store Stockholm, Sweden"
TRAVEL_MODE = "transit"


def fetch_lat_lng(google_maps_client: googlemaps.Client, address: str) -> dict[str, str]:
    return google_maps_client.geocode(address)[0]["geometry"]["location"]


def fetch_places(google_maps_client: googlemaps.Client, query: str):
    response = google_maps_client.places(query=query)
    results = response["results"]

    while "next_page_token" in response:
        time.sleep(2)
        next_page_token = response["next_page_token"]
        response = google_maps_client.places(query=query, page_token=next_page_token)
        results.extend(response["results"])

    return results


def main():
    load_dotenv()

    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

    location = fetch_lat_lng(gmaps, ORIGIN_ADDRESS)

    print(f"Fetching locations for query: \"{QUERY}\" . . .")
    stores = fetch_places(gmaps, QUERY)
    print(f"{len(stores)} locations found . . .")

    print(f"Calculating routes with origin: {ORIGIN_ADDRESS} . . .")
    results = []
    for store in stores:
        store_location = store["geometry"]["location"]
        store_address = store["formatted_address"]
        store_name = store["name"]

        routes = gmaps.directions(origin=location, destination=store_location, mode=TRAVEL_MODE, alternatives=True)
        min_route_time = min(route["legs"][0]["duration"]["value"] for route in routes)
        results.append((store_name, store_address, min_route_time))

    results.sort(key=itemgetter(2))

    print(f"Locations sorted by shortest transit travel time from: {ORIGIN_ADDRESS}:")
    name_width = max(len(result[0]) for result in results) + 4
    for name, address, transit_time_seconds in results:
        print(f"[{timedelta(seconds=transit_time_seconds)}] - {name.ljust(name_width, ' ')}{address}")


if __name__ == '__main__':
    main()
