# Arquivo de funções do projeto
import shelve
from datetime import datetime
import random
from functionsMenu import lerOpcao

funcionarios = []

# Funções Shelve
def salvar() :#Salva as alterações
    with shelve.open("dados/funcionariosData") as fun:
        fun["funcionariosData"] = funcionarios

def carregar(): #Carrega as alterações
    global funcionarios 
    with shelve.open("dados/funcionariosData") as fun:
        funcionarios = fun.get("funcionariosData", [])

# Funções para CRUD funcionários

def validaFuncionario(nome): #Ver se existe um funcionário a partir de um nome, e retorna booleano
    for funcionario in funcionarios: 
        if funcionario["nome"].lower() == nome.lower():#Verifica se existe o nome do funcionário na lista de funcionários
            return True #Se existir ele retorna True
    return False #Se não, False

def getFuncionario(nome):
    for funcionario in funcionarios:
        if funcionario["nome"].lower() == nome.lower():
            return funcionario
    return None

def getPonto(funcionario, id):
    for ponto in funcionario["pontos"]: #Pega todos os pontos 
        if ponto["id"] == id:
            return ponto
    return None

def gerarIdPonto(funcionario): #Função para gerar novo id
    idsExistentes = {ponto["id"] for ponto in funcionario["pontos"]} #Gera uma lista com os ids existentes
    novoId = random.randrange(1, 99) #Gera um id de teste aleatório
    while novoId in idsExistentes: #Enquanto esse id aleatório tiver na listagem
        novoId = random.randrange(1, 99)
    return novoId


def validaPonto(data, entrada, saida):
    try:
        dataF    = datetime.strptime(data,    '%d/%m/%Y').date()
        entradaF = datetime.strptime(entrada, '%H:%M').time()
        saidaF   = datetime.strptime(saida,   '%H:%M').time()
    except ValueError:
        return True
    return dataF,entradaF,saidaF

def calculaHorasPonto(ponto):
    """Retorna as horas trabalhadas em um único ponto, como float."""
    entrada = datetime.combine(ponto["data"], ponto["horaEntrada"])
    saida   = datetime.combine(ponto["data"], ponto["horaSaida"])
    duracao = saida - entrada
    return duracao.total_seconds() / 3600


def calculaHorasFuncionario(funcionario):
    """Retorna o total de horas trabalhadas por um funcionário (todos os pontos)."""
    return sum(calculaHorasPonto(p) for p in funcionario["pontos"])


def calculaHorasPorDia(funcionario):
    """Retorna um dicionário {data: total_horas_no_dia} para um funcionário."""
    horasPorDia = {}
    for ponto in funcionario["pontos"]:
        dia = ponto["data"]
        horasPorDia[dia] = horasPorDia.get(dia, 0) + calculaHorasPonto(ponto)
    return horasPorDia

#CRUD Funcionários
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


#CRUD Pontos
def registraPonto(nome, data, entrada, saida):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe"
    
    pontos = validaPonto(data, entrada, saida)

    if pontos:
        return "Valores de entrada para o ponto inválidos..."

    dataF, entradaF, saidaF = pontos

    if entradaF > saidaF:
        return "O horário da entrada não pode ser maior que da saída"
    
    
    funcionario = getFuncionario(nome)
    idPonto = gerarIdPonto(funcionario)

    funcionario["pontos"].append({
            "id":idPonto,
            "data":dataF, 
            "horaEntrada":entradaF, 
            "horaSaida":saidaF})
    
    return f"Registro de ponto bem sucessido! ID = {idPonto}"

def editPonto(nome, id, dataNew, entradaNew, saidaNew):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe..."

    funcionario = getFuncionario(nome)
    ponto = getPonto(funcionario, id)

    if ponto is None:
        return "Ponto não encontrado..."

    pontosValidados = validaPonto(dataNew, entradaNew, saidaNew)

    if pontosValidados is True:
        return "Valores de entrada para o ponto inválidos..."

    dataF, entradaF, saidaF = pontosValidados

    if entradaF > saidaF:
        return "O horário da entrada não pode ser maior que da saída"

    ponto["data"] = dataF
    ponto["horaEntrada"] = entradaF
    ponto["horaSaida"] = saidaF

    return "Ponto editado com sucesso !!"

def deletaPonto(nome, id):
    if not validaFuncionario(nome):
        return "Seu funcionário não existe..."

    funcionario = getFuncionario(nome)
    ponto = getPonto(funcionario, id)

    if ponto is None:
        return "Ponto não encontrado..."

    if input(f"Deseja realmente deletar o ponto {ponto['id']} (S/N)? ").strip().upper() == "S":
        funcionario["pontos"].remove(ponto)
        return "Ponto deletado com sucesso !!"

    return f"Falha ao deletar o ponto {ponto['id']}..."

def visualizarPontos(nome):
    """Mostra todos os pontos registrados de um funcionário específico."""
    if not validaFuncionario(nome):
        return "Seu funcionário não existe..."

    funcionario = getFuncionario(nome)

    if len(funcionario["pontos"]) < 1:
        return f"{funcionario['nome']} ainda não possui pontos registrados..."

    print(f"{'-'*39}")
    print(f"| PONTOS DE {funcionario['nome'].upper():<27}|")
    print(f"{'-'*39}")
    for ponto in funcionario["pontos"]:
        dataStr    = ponto["data"].strftime("%d/%m/%Y")
        entradaStr = ponto["horaEntrada"].strftime("%H:%M")
        saidaStr   = ponto["horaSaida"].strftime("%H:%M")
        horas      = calculaHorasPonto(ponto)
        print(f"| ID {ponto['id']:<3} | {dataStr} | {entradaStr} - {saidaStr} | {horas:.2f}h")
    print(f"{'-'*39}\n")
    return "Pontos exibidos com sucesso"


#Relatórios
def relatorioFuncionarios(ordenarPor=None):
    """
    Exibe relatório tabular de todos os funcionários.
    ordenarPor: None | "nome" | "horas"
    """
    if len(funcionarios) < 1:
        return "Não existe funcionários ainda..."

    listaOrdenada = funcionarios.copy()

    if ordenarPor == "nome":
        listaOrdenada.sort(key=lambda f: f["nome"].lower())
    elif ordenarPor == "horas":
        listaOrdenada.sort(key=lambda f: calculaHorasFuncionario(f), reverse=True)

    print(f"{'-'*55}")
    print(f"| {'NOME':<20} | {'CARGO':<15} | {'TOTAL HORAS':<10}|")
    print(f"{'-'*55}")
    for func in listaOrdenada:
        totalHoras = calculaHorasFuncionario(func)
        print(f"| {func['nome']:<20} | {func['cargo']:<15} | {totalHoras:>9.2f}h|")
    print(f"{'-'*55}\n")

    return "Relatório exibido com sucesso"


def relatorioHorasAbaixoDe(limiteHoras=8    ):
    """Lista funcionários com média de horas/dia abaixo do limite informado."""
    if len(funcionarios) < 1:
        return "Não existe funcionários ainda..."

    encontrados = []

    for func in funcionarios:
        horasPorDia = calculaHorasPorDia(func)
        if not horasPorDia:
            continue
        for dia, horas in horasPorDia.items():
            if horas < limiteHoras:
                encontrados.append((func["nome"], dia, horas))

    if not encontrados:
        return f"Nenhum funcionário com menos de {limiteHoras}h em um dia."

    print(f"{'-'*55}")
    print(f"| FUNCIONÁRIOS COM MENOS DE {limiteHoras}H NO DIA{' '*(55-32-len(str(limiteHoras)))}|")
    print(f"{'-'*55}")
    for nome, dia, horas in encontrados:
        dataStr = dia.strftime("%d/%m/%Y")
        print(f"| {nome:<20} | {dataStr} | {horas:.2f}h")
    print(f"{'-'*55}\n")

    return "Relatório exibido com sucesso"


def relatorioAbaixoDe40Horas():
    """Lista funcionários cujo total geral de horas trabalhadas é menor que 40h."""
    if len(funcionarios) < 1:
        return "Não existe funcionários ainda..."

    encontrados = [
        (func["nome"], calculaHorasFuncionario(func))
        for func in funcionarios
        if calculaHorasFuncionario(func) < 40
    ]

    if not encontrados:
        return "Todos os funcionários completaram 40 horas."

    print(f"{'-'*39}")
    print(f"| FUNCIONÁRIOS ABAIXO DE 40 HORAS      |")
    print(f"{'-'*39}")
    for nome, horas in encontrados:
        print(f"| {nome:<25} | {horas:>6.2f}h |")
    print(f"{'-'*39}\n")

    return "Relatório exibido com sucesso"