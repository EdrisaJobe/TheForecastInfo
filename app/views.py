from django.shortcuts import render
import urllib.request
import json
import http

# Create your views here.

def index(request):

    # grabbing api from OpenWeather
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=aa237aa0b8bfefa9b4156b04460b1e24').read()

        # holds all information we need to grab from source
        data_list = json.loads(source) 
        # var that renders everything on html page
        data = {
            "country_code": str(data_list['sys']['country']),
            "name": str(data_list['name']),
            "temp": str(data_list['main']['temp']) + ' °F',
            "humidity": str(data_list['main']['humidity']) + ' %',
            "pressure": str(data_list['main']['pressure']) + ' hPa',
            "main": str(data_list['weather'][0]['main']),
            "description": str(data_list['weather'][0]['description']),
            "icon": data_list['weather'][0]['icon'] # image, str not needed
        }
    else:
        data = {}

    return render(request, 'index.html', data)

# about page

def about(request):
    
    return render(request, 'about.html')
