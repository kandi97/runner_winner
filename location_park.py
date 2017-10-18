import googlemaps
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'YOUR API KEY HERE'

google_places = GooglePlaces(YOUR_API_KEY)

def (find_park):
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    str(reverse_geocode_result)

    query_result = google_places.nearby_search(
            location=reverse_geocode_result, keyword='Parks',
            radius=500, types=[types.TYPE_FOOD])

    if query_result.has_attributions:
        print query_result.html_attributions


    for place in query_result.places:
    # Returned places from a query are place summaries.
        print place.name
        print place.geo_location
        print place.place_id