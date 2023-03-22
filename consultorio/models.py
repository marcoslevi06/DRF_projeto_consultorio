from django.db import models
from cpf_field.models import CPFField


class Paciente(models.Model):
    nome_paciente = models.CharField(max_length=50, null=False, blank=False)
    rg_paciente = models.CharField(
        max_length=9, null=False, blank=False, unique=True)
    celular_paciente = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    data_consulta = models.DateField()
    cpf_paciente = CPFField('cpf_paciente')

    def __str__(self):
        return self.nome_paciente


class AreaMedica(models.Model):
    nome_area = models.CharField(
        max_length=25, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome_area


class Cadastro(models.Model):

    URGENCIA = (
        ('Em Espera', 'Em Espera'),
        ('Não Crítico', 'Não Crítico'),
        ('Semicritico', 'Semicritito'),
        ('Crítico', 'Crítico'),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    area_medica = models.ForeignKey(AreaMedica, on_delete=models.CASCADE)
    urgencia = models.CharField(
        max_length=15, choices=URGENCIA, null=False, blank=False, default='Em Espera')
    observacoes = models.TextField(max_length=300)
