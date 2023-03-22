from rest_framework import serializers
from .validate import *
from .models import *


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        exclude = []

    def validate(self, data):

        # Se o nome estiver errado, mostre o erro:
        print('NOME = ', data['nome_paciente'])
        if not validate_nome_paciente(data['nome_paciente']):
            raise serializers.ValidationError(
                {'nome_paciente': 'Nome deve conter apenas letras. Por favor, preencha com atenção.'})

        # se o rg for diferente de 9 dígitos, mostre o erro:
        if not validate_rg(data['rg_paciente']):
            raise serializers.ValidationError(
                {'rg_paciente': 'RG inválido, Por favor verifique se o número está correto.'})

        # se o celular não estiver no formato especificado, mortre o erro:
        if not validate_celular(data['celular_paciente']):
            raise serializers.ValidationError(
                {'celular_paciente': 'O celular deve ser informado no formato: 00 9 1234-5678. Por favor verifique os dígitos repassados.'})

        # se a data de nacimento for maior ou igual a data de hoje, mostre o erro:
        if not validate_dataNascimento(data['data_nascimento']):
            raise serializers.ValidationError(
                {'data_nascimento': 'Data inválida, por favor reveja se a data informada está correta.'})

        # se a data da consulta for maior ou igual a data de hoje, mostre o erro:
        if not validate_dataConsulta(data['data_consulta']):
            raise serializers.ValidationError(
                {'data_consulta': 'Por favor, reveja se a data da consulta informada está correta.'})
        return data


class AreaMedicaSerializer(serializers.ModelSerializer):

    def validate(self, data):
        # Se o nome não for válido, retorne o erro:
        if not validate_nomeAreaMedica(data['nome_area']):
            raise serializers.ValidationError(
                'Verifique se os caracteres digitados estão corretos.')
        return data

    class Meta:
        model = AreaMedica
        exclude = []


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        exclude = []


class PacienteCadastradoSerializer(serializers.ModelSerializer):
    '''Lista todos os pacientes cadastrados naquela respectiva área.'''

    # Acessando o valor dos campos para exibir no template DRF.
    paciente = serializers.ReadOnlyField(source='paciente.nome_paciente')
    area_medica = serializers.ReadOnlyField(source='area_medica.nome_area')

    class Meta:
        model = Cadastro
        fields = ['paciente', 'area_medica', 'urgencia', 'observacoes', 'id', ]


class AreaCadastradaSerializer(serializers.ModelSerializer):
    '''Mostra todos os pacientes cadastrados nessa respectiva área de atendimento.'''

    paciente = serializers.ReadOnlyField(source='paciente.nome_paciente')
    area_medica = serializers.ReadOnlyField(source='area_medica.nome_area')

    class Meta:
        model = Cadastro
        fields = ['area_medica', 'paciente', 'urgencia', 'observacoes', 'id', ]
