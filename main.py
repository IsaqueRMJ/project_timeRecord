# Arquivo principal que chamara o projeto
from functions import *
from functionsMenu import *

carregar()

while True:
    menuPrincipal()
    match lerOpcao():
        case 1:
            while True:
                menuFuncionarios()
                match lerOpcao():
                    case 1:
                        nome  = input("Digite o nome do funcionário: ")
                        cargo = input("Digite o cargo do funcionário: ")
                        registraFuncionario(nome, cargo)
                        input()
                    case 2:
                        nomeAtual = input("Digite o nome do funcionário que vai ser editado: ")
                        nomeNovo  = input("Digite novo nome do funcionário: ")
                        cargoNovo = input("Digite novo cargo do funcionário: ")
                        editarFuncionario(nomeAtual, nomeNovo, cargoNovo)
                        input()
                    case 3:
                        nomeAtual = input("Digite o nome do funcionário que vai ser editado: ")
                        deletaFuncionario(nomeAtual)
                        input()
                    case 4:
                        saindo()
                        break
                    case _:
                        print("Opção não exitente")
                        input()
        case 2:
            menuPontos()
            match lerOpcao():
                case _:
                    print("")
        case 3:
            menuRelatorios()
            match lerOpcao():
                case _:
                    print("Opção não exitente")
                    input()
        case _:
            print("Opção inválida")
salvar()