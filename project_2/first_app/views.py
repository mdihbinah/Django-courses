from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request) :
    return render(request, 'first_app/home.html')

# def home(request) :
#     return HttpResponse("This is home page.")
# def test(request) :
#     return HttpResponse("This is test page.Now I test this site to learn django basic.")




