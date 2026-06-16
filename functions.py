# Arquivo de funções do projeto
import shelve
from datetime import datetime
import os

funcionarios = []

# Funções Shelve
def salvar():
    with shelve.open("dados") as fun:
        fun["funcionarios"] = funcionarios

def carregar():
    global funcionarios 
    with shelve.open("dados") as fun:
        return fun.get("funcionarios", [])


# Funções funcionários
def validaFuncionario(nome): #Funcionando
    for funcionario in funcionarios:
        if funcionario["nome"].lower() == nome.lower():
            return True
    return False

def getFuncionario(nome):
    for funcionario in funcionarios:
        if funcionario["nome"].lower() == nome.lower():
            return funcionario
    return None


def registraFuncionario(nome, cargo):
    # Validar se existe nome
    if validaFuncionario(nome):
        return "O seu funcionário já existe"
    else:
        funcionarios.append({
            "nome": nome,
            "cargo": cargo,
            "pontos": []
        })
        
        return "Funcionário Criado Com Sucesso !!!"

def editarFuncionario(nomeAtual, nomeNew, cargoNew):

    if not validaFuncionario(nomeAtual):
        return "Seu funcionário não existe..."
    
    funcionario = getFuncionario(nomeAtual)
    funcionario["nome"] = nomeNew
    funcionario["cargo"] = cargoNew
    return "Funcionário editado com sucesso !!"

def deletaFuncionario(nomeAtual):
    if not validaFuncionario(nomeAtual):
        return "Seu funcionário não existe..."
    
    funcionario = getFuncionario(nomeAtual)
    funcionarios.remove(funcionario)
    return "Funcionário deletado !!"


def registraPonto(nome, data, entrada, saida):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe"

    if entrada > saida:
        return "O horário da entrada não pode ser maior que da saída"
    
    funcionario = getFuncionario(nome)
    funcionario["pontos"].append({
            "data":data, 
            "horaEntrada":entrada, 
            "horaSaida":saida})
    
    return "Registro de ponto bem sucessido !!"