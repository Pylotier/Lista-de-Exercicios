#Declaração de variáveis
largura: float = 0.0
comprimento: float = 0.0
altura: float = 0.0
volume: float = 0.0
#Início
comprimento = float(input("Digite o comprimento do paralelepípedo:"))
altura = float(input("Digite a altura do paralelepípedo:"))
largura = float(input("Digite o largura do paralelepípedo:"))

volume = altura*largura*comprimento

print("O volume do paralelepípedo é:", volume)
#Fim