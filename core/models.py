from django.db import models

# Modelo de Agendamento
class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    especialidade = models.CharField(max_length=100)
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.especialidade} em {self.data}'

# Modelo de Médico
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    parcelas = models.PositiveIntegerField(default=1)
    nota = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    avaliacoes = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='medicos/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome
