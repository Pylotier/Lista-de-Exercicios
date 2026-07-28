#Declaração de variáveis
quantLitros: float = 0.0
tempoPercorer: int = 0
velocidadeMedia: float = 0.0
distancia: float = 0.0
#Início
tempoPercorer = int(input("Digite quantas horas dura a viajem: "))
velocidadeMedia = float(input("Digite a velocidade média em Kh: "))

distancia = tempoPercorer * velocidadeMedia
quantLitros = distancia / 12

print("Será usado", quantLitros, "litros para percorrer essa viajem")
#Fim