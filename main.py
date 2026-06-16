# Arquivo principal que chamara o projeto
import os
from functions import *
carregar()

while True:
    print("Bem vindo(a) ao sistema de Ponto IFCE")
    print("1 - Funcionários\n2 - Pontos\n3 - Relatórios\n4 - Sair")
    try:
        inputKey = int(input())
        match inputKey:
            case 1:
                print("1 - Cadastrar Funcionário\n"\
                      "2 - Editar Funcionário\n"\
                      "3 - Excluir Funcionário\n" \
                      "4 - Sair")
                input()
            case 2:
                print("1 - Cadastrar Pontos\n" \
                      "2 - Editar Pontos\n"\
                      "3 - Excluir Pontos\n" \
                      "4 - Sair")
                input()
            case 3:
                print("1 - Listar todos os funcionários e seus cargos\n" \
                      "2 - Listar funcionários em ordem alfabética\n" \
                      "3 - Listar funcionários em ordem de horas trabalhadas\n" \
                      "4 - Funcionários com menos de 40 horas" \
                      "5 - Sair")
                input()
            case 4:
                input("FINALIZANDO(press ENTER)...")
                break
            case _:
                print("Opção não existente, digite novamente ...")
                input()
    except ValueError:
        print("Valor digitado é inválido")
        input()
        
salvar()