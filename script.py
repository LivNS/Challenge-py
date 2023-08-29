
# Debora da Silva Amaral RM 550412
# Levy Nascimento Junior RM 98655
# Lívia Namba Seraphim RM 97819

class Estoque:
    def __init__(self):
        self.itens = {
            'rolhas': 3000,
            'garrafas': 2500,
            'rotulos': 6000,
            'caixas': 2000,
        }
    
    def entrada(self, item, quantidade):
        if item in self.itens:
            self.itens[item] += quantidade
            print(f"Entrada de {quantidade} {item} registrada com sucesso!")
        else:
            print(f"O item {item} não existe no estoque.")
    
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
    
    def mostrar_estoque(self):
        print("Estoque atual:")
        for item, quantidade in self.itens.items():
            print(f"{item}: {quantidade}")

estoque = Estoque()

while True:
    print("\n1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Mostrar estoque")
    print("4 - Sair")
    
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
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
