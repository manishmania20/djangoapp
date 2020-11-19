from django.shortcuts import render

# Create your views here.
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
# for floor operation
import math
  
  
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=bf12716d614bf07180c89c2aecb56135').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 

        temp_celc = math.floor(float(str(list_of_data['main']['temp'] - 272.15)))
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "description": str(list_of_data['weather'][0]['description']),
            "temp": str(temp_celc) + u'\u00b0' + 'C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']) + '%', 
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "main/index.html", data) 