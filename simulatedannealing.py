import random
import math

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

def simulated_annealing(cidades):
    temperatura_inicial = 100
    taxa_de_resfriamento = 0.99
    temperatura = temperatura_inicial
    percurso_atual = cidades[:]
    random.shuffle(percurso_atual)
    distancia_atual = calcular_distancia(percurso_atual)
    
    while temperatura > 1:
        i, j = random.sample(range(len(cidades)), 2)
        novo_percurso = percurso_atual[:]
        novo_percurso[i], novo_percurso[j] = novo_percurso[j], novo_percurso[i]  # Troca duas cidades
        
        nova_distancia = calcular_distancia(novo_percurso)
        delta_distancia = nova_distancia - distancia_atual
        
        if delta_distancia < 0 or random.random() < math.exp(-delta_distancia / temperatura):
            percurso_atual, distancia_atual = novo_percurso, nova_distancia
        
        temperatura *= taxa_de_resfriamento
    
    return percurso_atual, distancia_atual

melhor_percurso, menor_distancia = simulated_annealing(cidades)
print("Melhor percurso encontrado:")
for i in range(len(melhor_percurso)):
    if i < len(melhor_percurso) - 1:
        print(f"{melhor_percurso[i]} -> {melhor_percurso[i+1]}: {distancias[(melhor_percurso[i], melhor_percurso[i+1])]} km")
    else:
        print(f"{melhor_percurso[i]} -> {melhor_percurso[0]}: {distancias[(melhor_percurso[i], melhor_percurso[0])]} km")
print(f"Menor distância total: {menor_distancia} km")
