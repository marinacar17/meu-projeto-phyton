
class Cliente():
    def __init__(self, nome, sobrenome, email, endereco, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.senha = senha

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Sobrenome: {self.sobrenome}
        Email: {self.email}
        """

class Produto():
    def __init__(self, nome, tipo, tamanho, preco):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.preco 
        

class Cafeteria():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produtos = []
    def cadastrar_cliente(self):
        cliente_nome = input('Digite seu nome')
        cliente_sobrenome = input('Digite seu sobrenome')
        cliente_endereco = input('Digite seu endereço')
        cliente_email = input('Digite seu e-mail')
        cliente_senha = input('Digite sua senha')

        cliente = Cliente(cliente_nome, cliente_sobrenome, cliente_endereco, cliente_email, cliente_senha)

        print(f'Cliente {cliente_nome} cadastrado com sucesso!')
        self.clientes.append(cliente)
        return cliente

    def cadastrar_produto(self):
        produto_nome = input('Digite o nome do produto')
        produto_tipo = input('Digite o tipo de produto')
        produto_tamanho = input("Quais os tamanhos existentes do produto")
        produto_preço = input("Preço do produto")
        produto = Produto(produto_nome, produto_tipo, produto_tamanho, produto_preço)
        print(f"{produto_nome} cadastrado com sucesso!")
        self.produtos.append(produto)
        return produto
    
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for i, cliente in enumerate(self.clientes):
            print(f"[{i}] {cliente.nome} {cliente.sobrenome} - {cliente.email}")
        return cliente
    
    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        for i, produto in enumerate(self.produtos):
            print(f"[{i}] {produto.nome} {produto.tipo} - {produto.preco}")
        return produto

    def fazer_pedido(self):
        print("Fazendo pedido...")
        self.listar_produtos()
        produto_escolhido = int(input("Escolha o produto pelo índice: "))
        if produto_escolhido < 0 or produto_escolhido >= len(self.produtos):
            print("Produto inválido.")
            return
        produto = self.produtos[produto_escolhido]
        print(f"Você escolheu o produto: {produto.nome} - {produto.preco}")
        return produto
cafeteria_1 = Cafeteria("Café do Ponto", "Rua das Flores, 123", "12.345.678/0001-90")

def menu(cafeteria):
    print(f"""
    Olá, seja bem-vindo a {cafeteria.nome}!
    1 - Cadastrar cliente
    2 - Cadastrar produto
    3 - Listar clientes cadastrados
    4 - Listar produtos cadastrados
    5 - Realizar pedido
    6 - Sair
    """)
    opcao = input("Escolha uma opção: ")
    return opcao

while True:
    opcao = menu(cafeteria_1)
    if opcao == '1':
        cafeteria_1.cadastrar_cliente()
    elif opcao == '2':
        cafeteria_1.cadastrar_produto()
    elif opcao == '3':
        cafeteria_1.listar_clientes()
    elif opcao == '4':
        cafeteria_1.listar_produtos()
    elif opcao == '5':
        cafeteria_1.fazer_pedido()
        print("Pedido realizado com sucesso!")
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

   