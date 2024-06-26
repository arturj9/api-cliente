import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    return CPF().validate(numero_do_cpf)

def rg_valido(rg):
    return len(rg)==9

def nome_valido(nome):
    return nome.isalpha()

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta