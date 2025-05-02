def verificar_negativo(numero):
    if numero < 0:
        return True
    else:
        return False
    
def contar_negativos(lista):
    contador = 0 
    for i in lista:
        if verificar_negativo(i):
            contador +=1
    return contador

a = contar_negativos([1,2,3,-4,-5,-6])
print(a)