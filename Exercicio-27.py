# 27.	Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

#Declarar as váriaveis
distaciaMetros: float = 0.0
distanciaMetrosTotal = 0.0
tempoMinutos: int = 0
tempoSegundo: int = 0
vm_Ms:float = 0.0
vm_Kh: float = 0.0
numVoltas: int = 0
#Inicio
distaciaMetros = float(input("Digite a distância da pista em metros: "))
numVoltas = int(input("Digite quantas voltas foram percorridas: "))
tempoMinutos = int(input("Digite o tempo de duração em minutos: "))

tempoSegundo = tempoMinutos * 60
distanciaMetrosTotal = distaciaMetros * numVoltas
vm_Ms = distanciaMetrosTotal / tempoSegundo
vm_Kh = vm_Ms * 3.6

print("Velocidade média:",vm_Kh,"/kh")

#Fim