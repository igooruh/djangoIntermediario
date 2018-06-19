from django.shortcuts import render
# Biblioteca para validar autenticação
# Importando biblioteco login do django, teremos que criar um alia para a biblioteca login, pois já existe uma função chamada login
from django.contrib.auth import authenticate, login as django_login
from django.http import  HttpResponse, HttpResponseRedirect

# Create your views here.
# Criado na aula Criando Página de Login de Usuário
def login (request):

    if request.method == 'GET':

        return render (request, 'my_app/login.html')

    usernanme = request.POST.get ('username')
    password = request.POST.get ('password')

#   Função que irá verificar se username e password estão corretas
    user = authenticate (usernanme = usernanme, password = password)

    if user:

        django_login (request, user)
        return HttpResponseRedirect ('/home/')

    return render (request, 'my_app/login.html')

def home (request):

    return render (request, 'my_app/home.html')


