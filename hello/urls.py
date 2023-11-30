from django.urls import path
from . import views
# first we need to declare a variable which will be a list of all the allowable URL's that can be 
#? accessed for this particular app 

urlpatterns = [
    path("", views.index, name ="index")
]