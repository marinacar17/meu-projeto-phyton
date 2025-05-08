class Cliente:
    def _init_(self, nome, sobrenome, email, endereco, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.senha = senha

    def _str_(self):
        return f"""
Nome: {self.nome}
Sobrenome: {self.sobrenome}
Email: {self.email}
Endereço: {self.endereco}
"""

class Produto:
    def _init_(self, nome, tipo, tamanho, preco):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.preco = preco

    def _str_(self):
        return f"""
Produto: {self.nome}
Tipo: {self.tipo}
Tamanho: {self.tamanho}
Preço: R${self.preco:.2f}
"""

class Cafeteria:
    def _init_(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produtos = []

    # ---------------- CLIENTES ----------------

    def cadastrar_cliente(self):
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        senha = input("Senha: ")
        cliente = Cliente(nome, sobrenome, email, endereco, senha)
        self.clientes.append(cliente)
        print(f"\n✅ Cliente {nome} cadastrado com sucesso!\n")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for i, cliente in enumerate(self.clientes):
            print(f"[{i}] {cliente.nome} {cliente.sobrenome} - {cliente.email}")

    def detalhar_cliente(self, indice):
        try:
            print(self.clientes[indice])
        except IndexError:
            print("❌ Cliente não encontrado.")

    def alterar_cliente(self, indice):
        try:
            cliente = self.clientes[indice]
            cliente.nome = input("Novo nome: ") or cliente.nome
            cliente.sobrenome = input("Novo sobrenome: ") or cliente.sobrenome
            cliente.email = input("Novo email: ") or cliente.email
            cliente.endereco = input("Novo endereço: ") or cliente.endereco
            print("✅ Cliente alterado com sucesso.")
        except IndexError:
            print("❌ Cliente não encontrado.")

    def deletar_cliente(self, indice):
        try:
            removido = self.clientes.pop(indice)
            print(f"✅ Cliente {removido.nome} removido.")
        except IndexError:
            print("❌ Cliente não encontrado.")

    # ---------------- PRODUTOS ----------------

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        tipo = input("Tipo: ")
        tamanho = input("Tamanho: ")
        preco = float(input("Preço: "))
        produto = Produto(nome, tipo, tamanho, preco)
        self.produtos.append(produto)
        print(f"\n✅ Produto {nome} cadastrado com sucesso!\n")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        for i, produto in enumerate(self.produtos):
            print(f"[{i}] {produto.nome} - R${produto.preco:.2f}")

    def detalhar_produto(self, indice):
        try:
            print(self.produtos[indice])
        except IndexError:
            print("❌ Produto não encontrado.")

    def alterar_produto(self, indice):
        try:
            produto = self.produtos[indice]
            produto.nome = input("Novo nome: ") or produto.nome
            produto.tipo = input("Novo tipo: ") or produto.tipo
            produto.tamanho = input("Novo tamanho: ") or produto.tamanho
            preco = input("Novo preço: ")
            if preco:
                produto.preco = float(preco)
                print("✅ Produto alterado com sucesso.")
            else:
                preco = produto.preco
        except IndexError:
            print("❌ Produto não encontrado.")

    def deletar_produto(self, indice):
        try:
            removido = self.produtos.pop(indice)
            print(f"✅ Produto {removido.nome} removido.")
        except IndexError:
            print("❌ Produto não encontrado.")


# ---------------- EXEMPLO DE USO ----------------
cafeteria = Cafeteria("Cafeteria Exemplo", "Rua Exemplo, 123", "12.345.678/0001-90")

# Exemplo de chamadas:
cafeteria.cadastrar_cliente()
cafeteria.listar_clientes()
cafeteria.detalhar_cliente(0)
cafeteria.alterar_cliente(0)
cafeteria.detalhar_cliente(0)
cafeteria.deletar_cliente(0)

cafeteria.cadastrar_produto()
cafeteria.listar_produtos()
cafeteria.detalhar_produto(0)
cafeteria.alterar_produto(0)
cafeteria.detalhar_produto(0)
cafeteria.deletar_produto(0)