class celular():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self. modelo = modelo
        self.ano = ano


#print(meu_celular.marca)

    def __str__(self):
        return f'{self.marca}, {self.modelo},{self.ano}'
    
    def fazerligacao(self, pessoa):
        print(f'ligando para {pessoa}')

meu_celular = celular("motorola", "motoe", "2022")

print(meu_celular)      

meu_celular.fazerligacao("mãe")
    
    


        