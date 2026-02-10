Carros = int(input("Digite quantos carros Dalessandro possui \n"))
#variavel carros recebe o que for digitado
Note = int(input("Digite quantos notebooks Ivo tem \n"))
#variavel Note recebe o que for digitado
#Lucas comprou 10% dos notes e 50% dos carros, com quantos itens cada um deles ficou?
# 50% = *0,5
# 10% = *0,10
Dalessandro = (Note * 0.9) + (Carros * 0.5)
#variavel Dalessandro recebe carros vezes 0,5
print(f"Dalessandro possui {Dalessandro} itens")
#print utilizando "f" para poder inprimir texto e variavel no mesmo comando
Lucas = (Note * 0.1) + (Carros * 0.5)
print(f"Lucas possui {Lucas} itens")
