import random

# Distâncias entre as cidades
distancias = {
    ("São Paulo", "Rio de Janeiro"): 430,
    ("São Paulo", "Belo Horizonte"): 586,
    ("São Paulo", "Brasília"): 872,
    ("São Paulo", "Salvador"): 1962,
    ("São Paulo", "Curitiba"): 408,
    ("São Paulo", "Porto Alegre"): 853,
    ("São Paulo", "Fortaleza"): 2365,
    ("Rio de Janeiro", "Belo Horizonte"): 434,
    ("Rio de Janeiro", "Brasília"): 1148,
    ("Rio de Janeiro", "Salvador"): 1649,
    ("Rio de Janeiro", "Curitiba"): 852,
    ("Rio de Janeiro", "Porto Alegre"): 1553,
    ("Rio de Janeiro", "Fortaleza"): 2191,
    ("Belo Horizonte", "Brasília"): 716,
    ("Belo Horizonte", "Salvador"): 1372,
    ("Belo Horizonte", "Curitiba"): 1004,
    ("Belo Horizonte", "Porto Alegre"): 1698,
    ("Belo Horizonte", "Fortaleza"): 2528,
    ("Brasília", "Salvador"): 1446,
    ("Brasília", "Curitiba"): 1366,
    ("Brasília", "Porto Alegre"): 2027,
    ("Brasília", "Fortaleza"): 2200,
    ("Salvador", "Curitiba"): 2387,
    ("Salvador", "Porto Alegre"): 3090,
    ("Salvador", "Fortaleza"): 1389,
    ("Curitiba", "Porto Alegre"): 711,
    ("Curitiba", "Fortaleza"): 3287,
    ("Porto Alegre", "Fortaleza"): 4243,
}

# Garantindo simetria nas distâncias
for (cidade1, cidade2), distancia in list(distancias.items()):
    distancias[(cidade2, cidade1)] = distancia

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Brasília",
    "Salvador",
    "Curitiba",
    "Porto Alegre",
    "Fortaleza",
]

def calcular_distancia(percurso):
    distancia_total = 0
    for i in range(len(percurso) - 1):
        distancia_total += distancias[(percurso[i], percurso[i+1])]
    # Retorna ao ponto de partida
    distancia_total += distancias[(percurso[-1], percurso[0])]
    return distancia_total

def imprimir_percurso(percurso):
    print("Percurso detalhado com distâncias entre as cidades:")
    for i in range(len(percurso) - 1):
        print(f"{percurso[i]} -> {percurso[i+1]}: {distancias[(percurso[i], percurso[i+1])]} km")
    # Fechando o ciclo ao retornar à cidade de origem
    print(f"{percurso[-1]} -> {percurso[0]}: {distancias[(percurso[-1], percurso[0])]} km")

def hill_climbing(cidades):
    percurso_atual = cidades[:]
    random.shuffle(percurso_atual)
    
    distancia_atual = calcular_distancia(percurso_atual)
    print(f"Percurso inicial: {percurso_atual}, Distância: {distancia_atual} km")
    
    melhorias = True
    while melhorias:
        melhorias = False
        for i in range(1, len(percurso_atual) - 1):
            for j in range(i + 1, len(percurso_atual)):
                novo_percurso = percurso_atual[:]
                novo_percurso[i], novo_percurso[j] = novo_percurso[j], novo_percurso[i]
                nova_distancia = calcular_distancia(novo_percurso)
                
                if nova_distancia < distancia_atual:
                    percurso_atual, distancia_atual = novo_percurso, nova_distancia
                    print(f"Novo percurso: {percurso_atual}, Distância: {distancia_atual} km")
                    melhorias = True
                    break
            if melhorias:
                break
    
    return percurso_atual, distancia_atual

melhor_percurso, menor_distancia = hill_climbing(cidades)
print(f"\nMelhor percurso encontrado: {melhor_percurso}")
print(f"Menor distância total: {menor_distancia} km")

# Imprimindo o percurso detalhado com distâncias
imprimir_percurso(melhor_percurso)
