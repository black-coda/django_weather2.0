from django.shortcuts import render
import urllib
import json



# Create your views here.
def index_____(request):
    url = 'https://api.weatherbit.io/v2.0/current?city={}&key=bd0ddb893319407f87237d48b526e8bc&include=minutely'
    city = 'lagos'
    url = url.format(city)
    response = request.get(url).json()
   

    data = {
        'timezone' : response['data'][0]['timezone'],
        'wind_dirc': response['data'][0]['wind_cdir'],
        'icon': response['data'][0]['weather']['icon'],
        'icon_description': response['data'][0]['weather']['description'],
        'temp' : response['data'][1]['temp'],
        'wind-speed' : response['data'][0]['wind_spd'],
        
    }

    context = {'weather': data}

    return render(request, 'weather/index.html',)

"""
def index_(request):
    url = 'https://api.weatherbit.io/v2.0/current?city={}&key=bd0ddb893319407f87237d48b526e8bc&include=minutely'
    city = ''
    url = url.format(city)
    response = request.get(url).json()

    data = {
        'timezone' : response['data'][0]['timezone'],
        'wind_dirc': response['data'][0]['wind_cdir'],
        'icon': response['data'][0]['weather']['icon'],
        'icon_description': response['data'][0]['weather']['description'],
        'temp' : response['data'][1]['temp'],
        
    }


    return render(request, 'weather/index_.html', data)

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = 'https://api.weatherbit.io/v2.0/current?city={}&key=bd0ddb893319407f87237d48b526e8bc&include=minutely'
        url = url.format(city)
        response = request.get(url).json()

        data = {
            'timezone' : response['data'][0]['timezone'],
            'wind_dirc': response['data'][0]['wind_cdir'],
            'icon': response['data'][0]['weather']['icon'],
            'icon_description': response['data'][0]['weather']['description'],
            'temp' : response['data'][1]['temp'],
            
        }

        print(data)
    
    else:
        data = {

        }

    return render(request, 'weather/index.html', data)


def index(request):
    return render(request, 'weather/index.html')

"""

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.weatherbit.io/v2.0/current?city={}&key=bd0ddb893319407f87237d48b526e8bc&include=minutely').read()
        source = source.format(city)
        list_of_data = json.loads(source)

        data = {
            'timezone' : str(list_of_data['data'][0]['timezone']) ,
            'wind_dirc': str(list_of_data['data'][0]['wind_cdir']),
            'icon': str(list_of_data['data'][0]['weather']['icon']),
            'icon_description': str(list_of_data['data'][0]['weather']['description']),
            'temp' : str(list_of_data['data'][1]['temp']),
            
        }

        print(data)
    else:
        data = {

        }

    return render(request, 'weather/index.html', data)