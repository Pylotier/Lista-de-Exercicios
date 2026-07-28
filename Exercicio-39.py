# 39.	Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 	1	2	3	4	...	64
# Qdte:	1	2	4	8	...	N


#Declarar as váriaveis
res: int = 0
montante: int = 0
#Inicio
montante = 1

for i in range(1, 64+1):
    montante *= 2
print("Número de grãos final no tabuleiro:",montante-1)
#Fim