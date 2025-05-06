from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('agendar/', views.agendar, name='agendar'),
    path('login/', views.login_view, name='login'),
]
