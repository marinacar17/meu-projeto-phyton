from operacoes import somar, subtrair, multiplicar, dividir

def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')
    if  oper == '5':
        print("Operação realizada! Calculadora encerrada!")
        return
    else:
        a = float(input("Digite um número: "))
        b = float(input("Digite um segundo número: " ))

        if oper == '1':
            soma = somar(a,b)
            print(soma)

        elif oper == '2':
            subtracao = subtrair(a,b)
            print(subtracao)

        elif oper == '3':
            multiplicacao = multiplicar(a,b)
            print(multiplicacao)
        
        elif oper == '4':
            divisao = dividir(a,b)
            print(divisao)
       
        else:
            print("Erro! Escolha fora das opções disponíveis")

menu()

