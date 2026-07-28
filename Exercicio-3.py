#Declaração de variáveis
base: float = 0.0
altura: float = 0.0
area: float = 0.0
#Início
base = float(input("Digite o valor da base:"))
altura = float(input("Digite o valor da altura:"))
area = (base*altura)/2
print("Área do triângulo:", area)
#Fim