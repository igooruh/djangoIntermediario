from django.shortcuts import render, redirect
# Biblioteca para validar autenticação
# Importando biblioteco login do django, teremos que criar um alia para a biblioteca login, pois já existe uma função chamada login
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import  HttpResponse, HttpResponseRedirect, HttpRequest

# Create your views here.
# Criado na aula Criando Página de Login de Usuário
def login (request : HttpRequest):

    if request.method == 'GET':

        return render (request, 'my_app/login.html')

    username = request.POST.get ('username')
    password = request.POST.get ('password')

#   Função que irá verificar se username e password estão corretas
    user = authenticate (username = username, password = password)

    if user:

        django_login (request, user)
        # return HttpResponseRedirect ('/home/')
        #  Outra forma de fazer o redirecionamento da página
        return redirect ('/home/')

    message = 'Credencial Inválida. Por favor tente novamente'
    return render (request, 'my_app/login.html', {'message' : message})

def logout (request):

    django_logout (request)
    return redirect ('/login/')

def home (request):

    return render (request, 'my_app/home.html')


