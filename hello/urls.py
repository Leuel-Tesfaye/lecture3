from django.urls import path
from . import views
# first we need to declare a variable which will be a list of all the allowable URL's that can be 
#? accessed for this particular app 

urlpatterns = [
    path("", views.index, name ="index"),
    path("str:name", views.greet, name = "greet"),
    path("testing", views.testing, name = "testing"),
    path("routing", views.routing, name = "routing")
]