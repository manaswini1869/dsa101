class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.food_index = 0

    # def snake_pos(self, snake_pos, direction):
    #     if direction == 'R':
    #         return self.snake.append((snake_pos[-1][0], snake_pos[-1][1]+1))
    #     elif direction == 'L':
    #         return self.snake.append((snake_pos[-1][0], snake_pos[-1][1]-1))
    #     elif direction == 'D':
    #         return self.snake.append((snake_pos[-1][0]+1, snake_pos[-1][1]))
    #     else:
    #         return self.snake.append((snake_pos[-1][0]-1, snake_pos[-1][1]))

    def move(self, direction: str) -> int:
        dir_map = {'R': (0,1), 'L': (0,-1), 'U': (-1, 0), 'D': (1, 0)}
        head_x, head_y = self.snake[-1]
        dx, dy = dir_map[direction]
        new_x, new_y = head_x + dx, head_y + dy
        new_head = (new_x, new_y)

        if not (0 <= new_x < self.height and 0<= new_y < self.width):
            return -1

        tail = self.snake[0]
        if new_head in self.snake_set and new_head != tail:
            return -1


        if self.food_index < len(self.food) and [new_x, new_y] == self.food[self.food_index]:
            self.food_index += 1
        else:
            self.snake.popleft()
            self.snake_set.remove(tail)

        self.snake.append(new_head)
        self.snake_set.add(new_head)

        return self.food_index




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)