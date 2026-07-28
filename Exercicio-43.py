# 43.	Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

#Declarar as váriaveis
tamanhoAna:float = 0
tamanhoMaria:float = 0
anosNecessario:int = 0
#Inicio
tamanhoMaria = 150
tamanhoAna = 110

while (tamanhoAna <= tamanhoMaria):
    tamanhoAna += 3
    tamanhoMaria += 2

    anosNecessario = anosNecessario + 1
print("Foi necessario", anosNecessario, "anos para que Ana hoje em dia com", tamanhoAna/100, "m superar Maria com", tamanhoMaria/100, "m")
#Fim