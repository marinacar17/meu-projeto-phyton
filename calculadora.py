from operacoes import somar, subtrair, multiplicar, dividir

def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multilpicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')
    a = float(input("Digite um número: "))
    b = float(input("Digite um segundo número: " ))

    if oper == '1':
        somar(a,b)
        soma = somar(a,b)
        print(soma)
    elif oper == '2':
        subtrair(a, b)
        subtracao = subtrair(a,b)

    elif oper == '3':
        multiplicar(a,b)
        multiplicacao = multiplicar(a,b)
        
    elif oper == '4':
        dividir(a,b)
        divisao = dividir(a,b)
        print(divisao)
    elif oper == '5':
        print("Operação realizada! Calculadora encerrada!")
       
    else:
        print("Erro! Escolha fora das opções disponíveis")
        
menu()