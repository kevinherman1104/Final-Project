from django.forms import ModelForm, TextInput#import modelform because i want exactly the same form as in the model
from .models import NameCity #import NameCity from models file

class FormCity(ModelForm):
    class Meta:
        model = NameCity      #to build a form from the NameCity model
        fields = ["name_of_city"] #only include name_of_city attributes from NameCity class
        widgets = {"name_of_city" : TextInput(attrs = {"class" : "input" , "placeholder" : "City Name"})} 
        #to set the user input so the user can input more than one city later on. 
        