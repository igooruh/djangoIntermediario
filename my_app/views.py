from django.shortcuts import render, redirect
# Biblioteca para validar autenticação
# Importando biblioteco login do django, teremos que criar um alia para a biblioteca login, pois já existe uma função chamada login
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import  HttpResponse, HttpResponseRedirect, HttpRequest

# Decorators para proteger as páginas do sistema que precisa estar autenticadas para ser visualizada
from django.contrib.auth.decorators import login_required
from .models import Address, STATES_CHOICES

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


    # if request.user.is_authenticated():
    #
    #     request.user.firsr_name
    #     # Implementar aqui alguma lógica associada ao usuário


# Os decorators abaixo servem para proteger as páginas, pois assim garatimos que não pessoas não autenticadas acessem a sistema
# Por meio das URL's
@login_required (login_url = '/login/')
def logout (request):

    django_logout (request)
    return redirect ('/login/')

@login_required (login_url = '/login/')
def home (request):

    return render (request, 'my_app/home.html')

@login_required (login_url = '/login')
def address_list (request):

    # objects é gerenciador de objetos/URL
    addresses = Address.objects.all ()
    return render (request, 'my_app/address/list.html', {'addresses' : addresses})

# Criando Endereços
@login_required (login_url = '/login/')
def address_create (request):

    if request.method == 'GET':
        states = STATES_CHOICES
        return render (request, 'my_app/address/create.html', {'states' : states})

    Address.objects.create (
        address = request.POST.get ('address'),
        address_complement = request.POST.get ('address_complement'),
        city = request.POST.get ('address_complement'),
        state = request.POST.get ('state'),
        country = request.POST.get ('address_complement'),
        user = request.user
    )

    return redirect ('/addresses/')
