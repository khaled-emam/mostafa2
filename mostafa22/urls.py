
from django.urls import path
from . import view

urlpatterns = [
    path('', view.home),
    path('food/', view.food),
    path('count/', view.count , name = "count") ,
    path('about/' , view.about , name = "about")
]
