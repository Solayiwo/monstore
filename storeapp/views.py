from django.http import HttpResponse
from django.template import loader


def index(request):
    index = loader.get_template('index.html')
    return HttpResponse(index.render())

def register(request):
    register = loader.get_template('index.html')
    return HttpResponse(register.render())

def login(request):
    pass

def loggedin_contact(request):
    pass

def logout(request):
    pass

def productview(request):
    pass

def cart(request):
    pass

def checkout(request):
    pass

