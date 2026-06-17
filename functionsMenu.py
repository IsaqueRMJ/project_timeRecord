import os

def limpa():
    os.system('clear')

def saindo():
    print("Retornando ao menu inicial...")
    input("clique qualquer tecla...")


def menuPrincipal():
    limpa()
    print("Bem vindo(a) ao sistema de Ponto IFCE")
    print("1 - Funcionários\n" \
          "2 - Pontos\n" \
          "3 - Relatórios\n" \
          "4 - Sair")

def menuFuncionarios():
    limpa()
    print("O que deseja fazer com seus funcionários?\n")
    print("1 - Cadastrar Funcionário\n" \
          "2 - Editar Funcionário\n" \
          "3 - Excluir Funcionário\n" \
          "4 - Sair")

def menuPontos():
    print("O que deseja fazer com os pontos?\n")
    print("1 - Cadastrar Ponto\n" \
          "2 - Editar Ponto\n" \
          "3 - Excluir Ponto\n" \
          "4 - Sair")

def menuRelatorios():
    print("Qual relatório deseja visualizar?\n\n")
    print("1 - Listar todos os funcionários e cargos\n" \
          "2 - Ordenar por nome\n" \
          "3  - Ordenar por horas trabalhadas\n" \
          "4 - Funcionários com menos de 40h\n" \
          "5 - Sair")

def lerOpcao():
    try:
       return int(input())
    except ValueError:
        print("Valor digitado é inválido")
        return -1
    
