from django.shortcuts import render, get_object_or_404, redirect
from .forms import AgendamentoForm, ContatoForm
from .models import Medico, Agendamento
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')

def especialidades(request):
    query = request.GET.get('q')
    medicos = Medico.objects.all()
    if query:
        medicos = medicos.filter(especialidade__icontains=query)
    return render(request, 'core/especialidades.html', {'medicos': medicos})

def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('agendar')
    else:
        form = AgendamentoForm()
    return render(request, 'core/agendar.html', {'form': form})

def login_view(request):
    return render(request, 'core/login.html')

def medico_detail(request, slug):
    medico = get_object_or_404(Medico, slug=slug)
    return render(request, 'core/medico_detail.html', {'medico': medico})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você poderia enviar por e-mail ou salvar
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'core/contato.html', {'form': form})


def fale_conosco(request):
    return render(request, 'core/fale_conosco.html')

def politica(request):
    return render(request, 'core/politica.html')

def termos(request):
    return render(request, 'core/termos.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def faq(request):
    return render(request, 'core/faq.html')
