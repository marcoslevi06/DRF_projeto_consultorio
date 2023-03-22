"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from consultorio.views import *


router = routers.DefaultRouter()
router.register('pacientes', PacienteViewSet, basename='Paciente')
router.register('areas-medicas', AreaMedicaViewSet, basename='AreaMedica')
router.register('cadastros', CadastroViewSet, basename='Cadastro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # rota para listar as áreas médicas aquele paciente foi cadastrado.
    path('pacientes/<int:pk>/cadastros', PacienteCadastradoViewset.as_view()),

    # rora para listar todos que foram cadastrados nessa determinada área médica.
    path('areas-medicas/<int:pk>/cadastros', AreaCadastradaViewSet.as_view()),
]
