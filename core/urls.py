from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('agendar/', views.agendar, name='agendar'),
    path('login/', views.login_view, name='login'),
    path('medicos/<slug:slug>/', views.medico_detail, name='medico_detail'),
    path('contato/', views.contato, name='contato'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
    path('politica-de-privacidade/', views.politica, name='politica'),
    path('termos-de-uso/', views.termos, name='termos'),
    path('sobre/', views.sobre, name='sobre'),         # novo
    path('faq/', views.faq, name='faq'),               # novo
]
