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
                        print(registraFuncionario(nome, cargo))
                        input()
                    case 2:
                        nomeAtual = input("Digite o nome do funcionário que vai ser editado: ")
                        nomeNovo  = input("Digite novo nome do funcionário: ")
                        cargoNovo = input("Digite novo cargo do funcionário: ")
                        print(editarFuncionario(nomeAtual, nomeNovo, cargoNovo))
                        input()
                    case 3:
                        nomeAtual = input("Digite o nome do funcionário que vai ser deletado: ")
                        print(deletaFuncionario(nomeAtual))
                        input()
                    case 4:
                        saindo()
                        break
                    case _:
                        print("Opção não existente")
                        input()
        case 2:
            while True:
                menuPontos()
                match lerOpcao():
                    case 1:
                        nome    = input("Digite o nome do funcionário: ")
                        data    = input("Digite o dia do registro do ponto (dia/mes/ano): ")
                        entrada = input("Digite a hora da entrada (horas:minutos): ")
                        saida   = input("Digite a hora da saida (horas:minutos): ")
                        print(registraPonto(nome, data, entrada, saida))
                        input()
                    case 2:
                        nome       = input("Digite o nome do funcionário: ")
                        idPonto    = int(input("Digite o ID do ponto que vai ser editado: "))
                        dataNew    = input("Digite a nova data (dia/mes/ano): ")
                        entradaNew = input("Digite a nova hora de entrada (horas:minutos): ")
                        saidaNew   = input("Digite a nova hora de saída (horas:minutos): ")
                        print(editPonto(nome, idPonto, dataNew, entradaNew, saidaNew))
                        input()
                    case 3:
                        nome    = input("Digite o nome do funcionário: ")
                        idPonto = int(input("Digite o ID do ponto que vai ser excluído: "))
                        print(deletaPonto(nome, idPonto))
                        input()
                    case 4:
                        saindo()
                        break
                    case _:
                        print("Opção não existente")
                        input()
        case 3:
            while True:
                menuRelatorios()
                match lerOpcao():
                    case 1:
                        nome = input("Digite o nome do funcionário: ")
                        print(visualizarPontos(nome))
                        input()
                    case 2:
                        print(relatorioFuncionarios())
                        input()
                    case 3:
                        print(relatorioFuncionarios(ordenarPor="nome"))
                        input()
                    case 4:
                        print(relatorioFuncionarios(ordenarPor="horas"))
                        input()
                    case 5:
                        print(relatorioHorasAbaixoDe(8))
                        input()
                    case 6:
                        print(relatorioAbaixoDe40Horas())
                        input()
                    case 7:
                        saindo()
                        break
                    case _:
                        print("Opção não existente")
                        input()
        case 4:
            salvar()
            break
        case _:
            print("Opção não existente")
            input()

print("Dados salvos. Até logo!")