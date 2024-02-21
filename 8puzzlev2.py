import numpy as np
from queue import PriorityQueue

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.goal_positions = {n: (i, j) for i, row in enumerate(goal) for j, n in enumerate(row)}

    def manhattan_distance(self, state):
        """Calcula a soma das distâncias de Manhattan de todas as peças."""
        distance = 0
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                if value != 0:
                    goal_i, goal_j = self.goal_positions[value]
                    distance += abs(goal_i - i) + abs(goal_j - j)
        return distance

    def get_neighbors(self, state):
        """Gera todos os estados vizinhos válidos (movimentos possíveis)."""
        zero_row, zero_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direções: direita, baixo, esquerda, cima
        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
                new_state = [list(row) for row in state]  # Cria uma cópia do estado atual
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                yield new_state

    def solve(self):
        """Resolve o puzzle usando o algoritmo A*."""
        pq = PriorityQueue()
        pq.put((0 + self.manhattan_distance(self.start), 0, self.start, []))  # (Custo total estimado, custo até agora, estado, caminho)
        visited = set()
        while not pq.empty():
            _, cost, current, path = pq.get()
            if current == self.goal:
                return path + [current]
            visited.add(tuple(map(tuple, current)))  # Adiciona o estado atual aos visitados
            for neighbor in self.get_neighbors(current):
                if tuple(map(tuple, neighbor)) not in visited:
                    pq.put((cost + 1 + self.manhattan_distance(neighbor), cost + 1, neighbor, path + [current]))
        return None

# Exemplo de uso
start = [[2, 8, 3], [1, 6, 0], [4, 7, 5]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

puzzle = Puzzle(start, goal)
solution = puzzle.solve()

if solution:
    for step in solution:
        print(np.matrix(step))
        print()
else:
    print("No solution found.")
