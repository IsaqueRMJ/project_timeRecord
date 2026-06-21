import os

def limpa():
    os.system('clear')

def saindo():
    print(f"{'-'*39}")
    print("| Retornando ao menu inicial...       |")
    print(f"{'-'*39}")
    input("Clique qualquer tecla...")

def menuPrincipal():
    limpa()
    print(f"{'-'*39}")
    print("| Bem vindo(a) ao sistema de Ponto IFCE |")
    print(f"{'-'*39}")
    print("| 1 - Funcionários                    |")
    print("| 2 - Pontos                          |")
    print("| 3 - Relatórios                      |")
    print("| 4 - Sair                            |")
    print(f"{'-'*39}\n")

def menuFuncionarios():
    limpa()
    print(f"{'-'*39}")
    print("|      MENU FUNCIONÁRIOS              |")
    print(f"{'-'*39}")
    print("| 1 - Cadastrar Funcionário           |")
    print("| 2 - Editar Funcionário              |")
    print("| 3 - Excluir Funcionário             |")
    print("| 4 - Sair                            |")
    print(f"{'-'*39}\n")

def menuPontos():
    limpa()
    print(f"{'-'*39}")
    print("|         MENU PONTOS                 |")
    print(f"{'-'*39}")
    print("| 1 - Cadastrar Ponto                 |")
    print("| 2 - Editar Ponto                    |")
    print("| 3 - Excluir Ponto                   |")
    print("| 4 - Sair                            |")
    print(f"{'-'*39}\n")

def menuRelatorios():
    limpa()
    print(f"{'-'*39}")
    print("|       MENU RELATÓRIOS               |")
    print(f"{'-'*39}")
    print("| 1 - Ver pontos de um funcionário    |")
    print("| 2 - Listar funcionários e cargos    |")
    print("| 3 - Ordenar por nome                |")
    print("| 4 - Ordenar por horas trabalhadas   |")
    print("| 5 - Menos de 8h em um dia           |")
    print("| 6 - Funcionários com menos de 40h   |")
    print("| 7 - Sair                            |")
    print(f"{'-'*39}\n")

def lerOpcao():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Valor digitado é inválido.")
        return -1