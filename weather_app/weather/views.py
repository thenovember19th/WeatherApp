from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def get_weather_data(city):
    api_key = '67c5cf1ece6c6b4531cd4856dd390218'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def index(request):
    city = request.GET.get('city', 'London')
    weather_data = get_weather_data(city)
    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'wind_speed': weather_data['wind']['speed'],
        'humidity': weather_data['main']['humidity'],
        'description': weather_data['weather'][0]['description'],
    }
    return render(request, 'index.html', context)