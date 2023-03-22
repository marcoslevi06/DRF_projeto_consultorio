'''
Arquivo criado para validar os campos do MODELS.

    Aqui, fazemos as def() com retorno TRUE. Para verificarmos no serializer a condição.
    Se a valiação for verdadeira, então é aceito.
    Se não for verdareira, então o erro é exibido.
'''

import re
import datetime


def validate_nome_paciente(nome_paciente):
    '''
    Para cara letra em NOME_PACIENTE, SE NÃO houver apenas letras 
    e se SE NÃO HOUVER apenas espaços em branco, retorne FALSE.
    '''
    for letra in nome_paciente:
        if not letra.isalpha() and not letra.isspace():
            return False
    return True


def validate_rg(rg_paciente):
    return len(rg_paciente) == 9


def validate_celular(celular_paciente):
    '''Verifica se o celular é válido, Ou seja, se está no formato 00 9 1234-5678'''
    modelo = '[0-9]{2} [9]{1} [0-9]{4}-[0-9]{4}'
    resposta = re.findall(modelo, celular_paciente)
    return resposta


def validate_dataNascimento(data_nascimento):
    return data_nascimento < datetime.date.today()


def validate_dataConsulta(data_Consulta):
    return data_Consulta <= datetime.date.today()


def validate_nomeAreaMedica(nome_area):
    # Para cada LETRA em AREA_MEDICA
    # SE NÃO HOUVER APENAS letras e espaços válidos, retorne FALSE.
    # Se todas letras em AREA_MEDICA forem válidos e tiverem espaços válidos, retorne TRUE.
    for letra in nome_area:
        if not letra.isalpha() and not letra.isspace():
            return False
    return True
