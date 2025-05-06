from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def especialidades(request):
    return render(request, 'core/especialidades.html')

def agendar(request):
    return render(request, 'core/agendar.html')

def login_view(request):
    return render(request, 'core/login.html')
