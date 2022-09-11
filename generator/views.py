from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, "generator/home.html")

def about(request):

    return render(request,"generator/about.html")

def password(request):
    word = list('abcdefghijklmopqrstuvwxyz')
    if request.GET.get('uppercase'):
        word.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        word.extend(list('1234567890'))
    if request.GET.get('special'):
        word.extend(list('!@#$%^&*'))


    lenght = int(request.GET.get('lenght',12))

    thepassword = ''
    for i in range(lenght):
        thepassword += random.choice(word)

    return render(request, "generator/password.html",{"password":thepassword})
