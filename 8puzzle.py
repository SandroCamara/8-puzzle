import heapq

class Puzzle:
    def __init__(self, start_board, goal_board):
        self.size = int(len(start_board) ** 0.5)
        self.start_board = start_board
        self.goal_board = goal_board
    
    def get_moves(self, board):
        moves = []
        zero_index = board.index(0)
        zero_row, zero_col = divmod(zero_index, self.size)
        
        for move_row, move_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = zero_row + move_row, zero_col + move_col
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                swap_index = new_row * self.size + new_col
                new_board = list(board)
                new_board[zero_index], new_board[swap_index] = new_board[swap_index], new_board[zero_index]
                moves.append(tuple(new_board))
        return moves
    
    def solve(self):
        def manhattan_distance(board):
            distance = 0
            for i, cell in enumerate(board):
                if cell != 0:
                    goal_position = self.goal_board.index(cell)
                    current_row, current_col = divmod(i, self.size)
                    goal_row, goal_col = divmod(goal_position, self.size)
                    distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            return distance
        
        def a_star():
            frontier = [(manhattan_distance(self.start_board), 0, self.start_board, [])]
            explored = set()
            while frontier:
                _, cost, current, path = heapq.heappop(frontier)
                if current == self.goal_board:
                    return path
                explored.add(tuple(current))
                for move in self.get_moves(current):
                    if tuple(move) not in explored:
                        heapq.heappush(frontier, (cost + manhattan_distance(move) + 1, cost + 1, move, path + [move]))
        
        solution = a_star()
        return solution

# Exemplo de uso
start_board = (2, 8, 3, 1, 6, 0, 4, 7, 5)  # Estado inicial
goal_board = (1, 2, 3, 8, 0, 4, 7, 6, 5)  # Estado objetivo

puzzle = Puzzle(start_board, goal_board)
solution = puzzle.solve()
for step in solution:
    print(step)
