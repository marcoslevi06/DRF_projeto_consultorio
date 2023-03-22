from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, generics
from .serializer import *
from .models import *


class PacienteViewSet(viewsets.ModelViewSet):
    '''Listando todos os pacientes cadastrados.'''
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['nome_paciente', ]
    search_fields = ['nome_paciente', ]


class AreaMedicaViewSet(viewsets.ModelViewSet):
    '''Listando as áreas médicas disponíveis para consulta.'''

    queryset = AreaMedica.objects.all()
    serializer_class = AreaMedicaSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['nome_area', ]
    search_fields = ['nome_area', ]


class CadastroViewSet(viewsets.ModelViewSet):
    '''Mostra todos os pacientes que foram cadastrados em alguma área médica.'''
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer


class PacienteCadastradoViewset(generics.ListAPIView):
    '''Lista onde esse usuário foi cadastrado e suas respectivas áreas.'''

    def get_queryset(self):
        queryset = Cadastro.objects.filter(
            paciente_id=self.kwargs['pk'])
        return queryset

    serializer_class = PacienteCadastradoSerializer


class AreaCadastradaViewSet(generics.ListAPIView):
    '''Lista de todos os pacientes cadastrados nessa respectiva área de atendimento.'''

    def get_queryset(self):
        queryset = Cadastro.objects.filter(
            area_medica_id=self.kwargs['pk'])
        return queryset

    serializer_class = AreaCadastradaSerializer
