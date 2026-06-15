# Arquivo de funções do projeto
import shelve
from database import funcionarios
from datetime import datetime
import os

def validaFuncionario(nome):
    validacao = False
    for funcionario in funcionarios:
        if funcionario["nome"] == nome:
            validacao = True
    return validacao

def getFuncionario(nome):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe"



def registraFuncionario(nome, cargo):
    # Validar se existe nome
    if validaFuncionario(nome):
        return "O seu funcionário já existe"
        
    funcionarios.append(
        {"nome":nome,
         "cargo":cargo})
    
def registraPonto(nome, data, entrada, saida):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe"
    
    funcionarios[nome]