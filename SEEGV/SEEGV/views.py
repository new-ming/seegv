from django.shortcuts import render
from django.http import HttpRequest

def index(request:HttpRequest):
    login = request.session.get("login")
    login_type = request.session.get("login_type")

    context = {
        'login' : login,
        'login_type' : login_type,
    }

    return render(request,'index.html',context)