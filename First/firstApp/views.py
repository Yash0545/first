from django.shortcuts import render
from django.http import HttpResponse
import 
# Create your views here.


def Main(request):
    return render(request,'Main.html')


def admin(request):
    return render(request,'Admin.html')


def login(request):
    return render(request,'login.html')


def index1(request):
    return render(request,'index1.html')


def index2(request):
    return render(request,'index2.html')


def ModifyTrain(request):
    return render(request,'ModifyTrain.html')


def AdminOpt(request):
    return render(request,'AdminOpt.html')


def index3(request):
    return render(request,'index3.html')

def index4(request):
    return render(request,'index4.html')

def reg(request):
    return render(request,'reg.html')

def index5(request):
    return render(request,'index5.html')

def showtickets(request):
    return render(request,'showtickets')

def logout(request):
    return render(request,'logout.html')

def User(request):
    return render(request,'User.html')

def ModifyUser(request):
    return render(request,'ModifyUser.html')

def train(request):
    #database connection
    #add this data in database and send to an html page to display added data
    #print('Addes data')

    return render(request,'index1.html')
