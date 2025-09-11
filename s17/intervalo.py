def calcular_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

velocidade = float(input("Digite a velocidade (em km/h): "))
tempo = float(input("Digite o tempo (em horas): "))

distancia = calcular_distancia(velocidade, tempo)
print(f"A distância percorrida é {distancia:3f} km.")
