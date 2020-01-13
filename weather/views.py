import requests #import requests that has been installed, it is build-in library
from django.shortcuts import render, redirect
from .models import NameCity
from .forms import FormCity

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ec6bd904126723e79d1dd3261ba31e20'
 
    #to assign API from openweathermap.org 
    #units = metric to show degrees in celcius  if we didn't set the units it will become default where is shows us Kelvin and 
    #units = imperial shows us fahrenheit
    #appid = ec6... shows the API keys that have been given to us since we registered our account in openweathermap.org
    error_message = ""                   #variable to assign the error message
    msg = ""                             #variable that is used for display if messages in html file
    class_msg = ""                       #variable to make notification color 
    if request.method == "POST":         #to make conditional statement if the method in html file equals to POST
        form = FormCity(request.POST)    #new variable form to pass the request's POST data
        if form.is_valid():           
            new_city = form.cleaned_data["name_of_city"]    #variable of new city input by user to takes the data that has been validated 
            existed_city = NameCity.objects.filter(name_of_city__iexact = new_city).count()     #variable to count the number of city existed

            if existed_city == 0:        #conditional statement if the city have not exist yet in the database
                r = requests.get(url.format(new_city)).json()
                if r["cod"] == 200:      #r["cod"] means that if i enter a city name that existed if we print the r it will give us "cod" = 200 
                    form.save()          #with cod as the key and 200 as the value means that the city we input existed 
                                         #means if the data is correct than save it 
                else:
                    error_message = "The city " + new_city + " does not exist! Try another name!" # if the cod key is not equal to 200 than it will return this message
            else:
                error_message = "The city " + new_city  + " already exist! Try another one!" #printed if the existed_city > 0
        if error_message:
            msg = error_message 
            class_msg = "is-danger" #to give the notification color is-danger = red
        else:
            msg = "City does exist and has been succesfully added!"
            class_msg = "is-success" #to give the notification color is-success = green 

    form = FormCity()  

    cities_name = NameCity.objects.all() #take all attributes/ objects from NameCity class and put in cities_name variable

    data_of_weather = [] #list of all cities that has been registered in admin page of the website

    for city in cities_name: #loop through element inside the cities_name variable

        r = requests.get(url.format(city)).json() #use the requests to get url with the format of city name and make it to json method
        
        city_weather = {
            "name_of_city" : city.name_of_city,
            "temperature" : r["main"]["temp"],        
            "feels_like" : r["main"]["feels_like"],
            "description" : r["weather"][0]["description"],
            "icon" : r["weather"][0]["icon"] ,
        }
        data_of_weather.append(city_weather) # to append each data according to their city name from the city_weather to data_of_weather list

    context = {
        "data_of_weather" : data_of_weather ,
        "form" : form ,
        "message" : msg,
        "message_class": class_msg,
        } 
        # to make a variable name context so that it will able to be recognized by the html.
    return render(request , 'weather/weather.html', context)# we pass context to the view where the weather.html exist

def delete_city_option(request , city_name): # function to delete city from the database
    NameCity.objects.get(name_of_city = city_name).delete() 

    return redirect("original") # means that if we delete a city it will automatically refresh/redirect the 
                                # web to the new page where the city we deleted before has been erased from the database