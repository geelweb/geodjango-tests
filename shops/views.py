from django.shortcuts import render_to_response
from django.contrib.gis import geos, measure
from django.template import RequestContext
from geopy import geocoders

from shops import models
from shops import forms

from urllib2 import URLError

def geocode_address(address):
    address = address.encode("utf-8")
    geocoder = geocoders.GoogleV3(domain='maps.google.fr')
    try:
	place, latlon = geocoder.geocode(address)
    except (URLError, GQueryError, ValueError):
	pass
    else:
        return latlon

def get_shops(lon, lat, km):
    current_point = geos.fromstr("POINT(%s %s)" % (lon, lat))
    distance_from_point = {"km": km}
    shops = models.Shop.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    shops = shops.distance(current_point).order_by("distance")
    return shops.distance(current_point)

def home(request):
    form = forms.AddressForm(request.POST or None)
    shops = []
    lat = lon = 0
    address = ""
    if form.is_valid():
        address = form.cleaned_data['address']
        km = form.cleaned_data['distance']
        location = geocode_address(address)
        if location:
            lat, lon = location
            shops = get_shops(lon, lat, km)
    return render_to_response("home.html", {
        "form": form,
        "shops": shops,
        "latitude": lat,
        "longitude": lon,
        "address": address,
        }, context_instance=RequestContext(request))
