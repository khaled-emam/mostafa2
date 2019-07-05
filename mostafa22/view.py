from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    return render (request , "homepage.html")

def food (request):
    return HttpResponse("That Is FOOD PAGE ")

def count (request):
    zz = request.GET["FULLTEXT"]
    slice = zz.split()

    return render (request , "count.html", {"FULLTEXT":zz, "meter":len(slice)} )

def about(request):
    return render (request , "about.html")
