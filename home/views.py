from http.client import responses
from socket import MsgFlag
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import json
from .forms import cont
from home.models import contact
# Create your views here.
with open('data/data.json') as f:
  data = json.load(f)

def main(response):
    return  HttpResponse("<h1><a href="/home/" class='btn btn-primary stretched-link' >Try It</a> </h1>")


def test(response):
    return HttpResponse("<h1>Working !</h1>")

def home(response):
    return render(response , "home/home.html" ,{"data":data})

def projects(response):
    return render(response , "home/projects.html", {"data":data})

def contact(response):
    if response.method =="POST":
        form = cont(response.POST)

        if form.is_valid():
            name=form.cleaned_data["name"]
            mes= form.cleaned_data["msg"]
            

            send_mail(name , mes , "jijainth.ai@gmail.com" , ["djijainth@gmail.com"] ,fail_silently=False )

            form = cont()
        
            
    else:
        form = cont()
    return render(response , "home/contact.html" , {"form":form})

def about(response):
    return render(response , "home/about.html", {"data":data})

def ai(response):
    return render(response , "home/ai.html")
    
