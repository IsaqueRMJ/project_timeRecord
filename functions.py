# Arquivo de funções do projeto
import shelve
from datetime import datetime
from functionsMenu import lerOpcao

funcionarios = []

# Funções Shelve
def salvar():
    with shelve.open("dados/funcionarios") as fun:
        fun["funcionarios"] = funcionarios

def carregar():
    global funcionarios 
    with shelve.open("dados/funcionarios") as fun:
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

    if input(f"Deseja realmente deletar o {funcionario['nome']} (S/N)?") == "S":   
        funcionarios.remove(funcionario)
        return "Funcionário deletado !!"
    
    return f"Falha ao deletar {funcionario['nome']}..."

def getAllFuncionarios():
    if len(funcionarios) < 1:
        return "Não existe funcionários ainda..."
    for func in funcionarios:
        print(f"Nome: {func['nome']}, Cargo: {func['cargo']}")

def registraPonto(nome, data, entrada, saida):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe"
    
    datetime.strptime(entrada) 
    datetime.strptime(saida)

    if entrada > saida:
        return "O horário da entrada não pode ser maior que da saída"
    
    funcionario = getFuncionario(nome)
    funcionario["pontos"].append({
            "data":data, 
            "horaEntrada":entrada, 
            "horaSaida":saida})
    
    return "Registro de ponto bem sucessido !!"