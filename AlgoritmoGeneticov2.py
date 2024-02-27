import numpy as np

def generate_population(size, length):
    return np.random.randint(2, size=(size, length))

def calculate_fitness(population, weights, values, max_weight):
    fitness = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        weight = np.dot(population[i], weights)
        value = np.dot(population[i], values)
        fitness[i] = value if weight <= max_weight else 0
    return fitness

def select_best_individuals(population, fitness, num_best):
    best_indices = np.argsort(fitness)[-num_best:]
    return population[best_indices]

def estimate_distribution(selected_individuals):
    # Estima a probabilidade de cada bit ser 1
    prob = np.mean(selected_individuals, axis=0)
    return prob

def sample_population(prob, size):
    new_population = np.random.rand(size, len(prob)) < prob
    return new_population.astype(int)

def genetic_algorithm_with_eda(weights, values, max_weight, population_size, num_generations, num_best):
    num_items = len(weights)
    population = generate_population(population_size, num_items)
    for generation in range(num_generations):
        fitness = calculate_fitness(population, weights, values, max_weight)
        selected_individuals = select_best_individuals(population, fitness, num_best)
        prob = estimate_distribution(selected_individuals)
        population = sample_population(prob, population_size)
        print(f"Generation {generation + 1}: Max Fitness = {max(fitness)}")
    return select_best_individuals(population, fitness, 1)[0], max(fitness)

# Exemplo de uso
weights = [15, 3, 2, 5, 9,20]  # Pesos dos itens
values = [15, 7, 10, 5, 8, 17]  # Valores dos itens
max_weight = 30  # Peso máximo que a mochila pode carregar

best_solution, best_solution_fitness = genetic_algorithm_with_eda(weights, values, max_weight, population_size=50, num_generations=100, num_best=10)
print("Melhor solução:", best_solution)
print("Valor da melhor solução:", best_solution_fitness)
