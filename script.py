
# Debora da Silva Amaral RM 550412
# Levy Nascimento Junior RM 98655
# Lívia Namba Seraphim RM 97819


# Controle de estoque, entrada e saída

# importação datetime e timedelta

from datetime import datetime, timedelta

# Definição dos itens em estoque 
class Estoque:
    def __init__(self):
        self.itens = {
            'rolhas': 3000,
            'garrafas': 2500,
            'rotulos': 6000,
            'caixas': 2000,
        }
    
# Entrada para que o cliente insira a quantidade a ser inserida no estoque
    def entrada(self, item, quantidade):
        if item in self.itens:
            self.itens[item] += quantidade
            print(f"Entrada de {quantidade} {item} registrada com sucesso!")
        else:
            print(f"O item {item} não existe no estoque.")
    
# Saída e definição de venda apenas em unidade, meia e uma duzia
    def saida(self, item, quantidade):
        if item in self.itens:
            if item == 'garrafas' and quantidade not in [1, 6, 12]:
                print("As garrafas devem ser vendidas unitariamente ou em caixas de 6 ou 12 unidades.")
            elif self.itens[item] >= quantidade:
                self.itens[item] -= quantidade
                print(f"Saida de {quantidade} {item} realizada com sucesso!")
            else:
                print(f"Quantidade insuficiente de {item} em estoque.")
        else:
            print(f"O item {item} não existe no estoque.")

# Estoque
    def mostrar_estoque(self):
        print("\nEstoque:")
        for item, quantidade in self.itens.items():
            print(f"{item}: {quantidade}")

# Para adicionar o frete, a data de entrega e o preço do produto
class Pedido:
    def __init__(self, cliente, itens, data_entrega):
        self.cliente = cliente
        self.itens = itens
        self.data_entrega = data_entrega

    def calcular_preco_total(self):
        preco_total = 0
        for item, quantidade in self.itens.items():
            preco_total += self.calcular_preco_item(item, quantidade)
        preco_total += 10 
        preco_total += preco_total * 0.1
        preco_total += 10 
        return preco_total
    
    def calcular_preco_item(self, item, quantidade):
        if item == 'garrafas':
            return quantidade * 10  
        
estoque = Estoque()

while True:
    print("\n1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Mostrar estoque")
    print("4 - Realizar pedido")
    print("5 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        item = input("Digite o item de entrada: ")
        quantidade = int(input("Digite a quantidade de entrada: "))
        estoque.entrada(item, quantidade)

    elif escolha == '2':
        item = input("Digite o item de saída: ")
        quantidade = int(input("Digite a quantidade de saída: "))
        estoque.saida(item, quantidade)

    elif escolha == '3':
        estoque.mostrar_estoque() 
    
    elif escolha == '4':
        cliente = input("Digite o nome do cliente: ")
        num_itens = int(input("Digite o número de itens no pedido: "))
        itens_pedido = {}
        for _ in range(num_itens):
            item = input("Digite o item do pedido: ")
            quantidade = int(input("Digite a quantidade do item: "))
            itens_pedido[item] = quantidade

        data_entrega_str = input("Digite a data de entrega (formato: DD/MM/YYYY): ")
        data_entrega = datetime.strptime(data_entrega_str, "%d/%m/%Y")

        pedido = Pedido(cliente, itens_pedido, data_entrega)

        for item, quantidade in itens_pedido.items():
            estoque.saida(item, quantidade)

        preco_total = pedido.calcular_preco_total()

        print(f"Preço total do pedido para {cliente}: R$ {preco_total:.2f}")
        print(f"Data de entrega: {data_entrega.strftime('%d/%m/%Y')}")

    elif escolha == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
