from django.contrib import admin
from .models import *


class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome_paciente', 'data_consulta']


admin.site.register(Paciente, PacienteAdmin)


class AreaMedicaAdmin(admin.ModelAdmin):
    list_display = ['nome_area', ]


admin.site.register(AreaMedica, AreaMedicaAdmin)


class CadastroAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'area_medica', 'urgencia', ]


admin.site.register(Cadastro, CadastroAdmin)
