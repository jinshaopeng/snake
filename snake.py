import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 游戏设置
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 设置屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return True

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont('simhei', size) if pygame.font.match_font('simhei') else pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    snake = Snake()
    food = Food()
    game_over = False
    game_started = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not game_started:
                    game_started = True
                    game_over = False
                    snake.reset()
                elif game_over:
                    game_started = True
                    game_over = False
                    snake.reset()
                else:
                    if event.key == pygame.K_UP:
                        snake.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.turn(RIGHT)

        screen.fill(BLACK)

        if not game_started:
            draw_text(screen, '贪吃蛇游戏', 48, WIDTH // 2, HEIGHT // 4)
            draw_text(screen, '按任意键开始', 36, WIDTH // 2, HEIGHT // 2)
            draw_text(screen, '方向键控制移动', 24, WIDTH // 2, HEIGHT * 2 // 3)
        elif game_over:
            draw_text(screen, '游戏结束!', 48, WIDTH // 2, HEIGHT // 4)
            draw_text(screen, f'得分: {snake.score}', 36, WIDTH // 2, HEIGHT // 2)
            draw_text(screen, '按任意键重新开始', 24, WIDTH // 2, HEIGHT * 2 // 3)
        else:
            if not snake.move():
                game_over = True

            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10
                food.randomize_position()

            snake.draw(screen)
            food.draw(screen)
            draw_text(screen, f'得分: {snake.score}', 24, WIDTH // 2, 10)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
