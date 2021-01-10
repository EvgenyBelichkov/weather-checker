from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def main(request):
    return render(request, 'checker/index.html')


def city(request):
    msg = request.GET['request_city']
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': msg,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    }
    res = requests.get(api_url, params)
    data = res.json()
    return render(request, 'checker/city.html', {'result': data['main']['temp']})
    #return render(request, 'checker/city.html')
