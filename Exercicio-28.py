# 28.	Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Venda Mensal	Preço Atual	Preço Novo
# < 500	< 30	+ 10%
# >= 500 e < 1000	>= 30 e < 80	+15%
# >= 1000	>= 80	- 5%
# Obs.: para outras condições, preço novo será igual ao preço atual.


#Declarar as váriaveis
precoProduto: float = 0.0
novoPreco: float = 0.0
mediaProduto: float = 0.0
res: float = 0.0
#Inicio
precoProduto = float(input("Digite o preço do produto: "))
mediaProduto = float(input("Digite  a média de compras do produto: "))

if (mediaProduto < 500):
    if (precoProduto < 30):
        novoPreco = precoProduto * 1.10
        print("Novo preço:", novoPreco)
    else:
        print("Preço não modificado:", precoProduto)
elif (mediaProduto >= 500 and mediaProduto < 1000):
    if (precoProduto >= 30 and precoProduto < 80):
        novoPreco = precoProduto * 1.15
        print("Novo preço:", novoPreco)
    else:
        print("Preço não modificado:", precoProduto)
elif (mediaProduto >= 1000):
    if (precoProduto >= 80):
        novoPreco = precoProduto * 0.95
        print("Novo preço:", novoPreco)
    else:
        print("Preço não modificado:", precoProduto)
#Fim