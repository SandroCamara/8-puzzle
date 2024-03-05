import numpy as np
import matplotlib.pyplot as plt

# Definindo a função f(x)
def f(x):
    return -x**2 + 4*x

# Implementação do Algoritmo de Hill Climbing
def hill_climbing(f, x_range=(0, 4), delta=0.01, max_iterations=1000):
    # Inicialização
    x = np.random.uniform(*x_range)
    current_value = f(x)
    steps = [(x, current_value)]  # Para armazenar os pontos explorados
    
    for _ in range(max_iterations):
        # Definição da Vizinhança
        neighbors = [x - delta, x + delta]
        neighbor_values = [f(n) for n in neighbors]
        
        # Avaliação e Atualização
        max_index = np.argmax(neighbor_values)
        if neighbor_values[max_index] > current_value:
            x = neighbors[max_index]
            current_value = neighbor_values[max_index]
            steps.append((x, current_value))
        else:
            break  # Critério de Parada

    return x, current_value, steps

# Executando o algoritmo
x_max, f_max, explored_points = hill_climbing(f)

# Plotando a função e os pontos explorados
x_values = np.linspace(0, 4, 400)
y_values = f(x_values)
explored_x, explored_y = zip(*explored_points)  # Desempacotando os pontos explorados

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = -x² + 4x')
plt.scatter(explored_x, explored_y, color='red', zorder=5, label='Pontos Explorados')
plt.title('Hill Climbing: Máximo de f(x) = -x² + 4x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

x_max, f_max
