from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'email', 'especialidade', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
