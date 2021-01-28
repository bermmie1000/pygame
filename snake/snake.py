import pygame
from datetime import datetime, timedelta
import time
import random

pygame.init()

# ===========================================
# CONSTANTS
# ===========================================
# COLOR
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
# SIZE
BOARD_SIZE = [400, 650]
BLOCK_SIZE = 10
# DIRECTION
EAST = "east"
WEST = "west"
NORTH = "north"
SOUTH = "south"
# KEYBINDING
RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
# TIME
TURN_INTERVAL = 0.1
# ===========================================


class Snake:
    def __init__(self):
        self.color = BLUE
        self.direction = NORTH
        self.positions = [(20, 50), (20, 51), (20, 52)]

    def draw(self, screen):
        for position in self.positions:
            block = pygame.Rect(
                (position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
                (BLOCK_SIZE, BLOCK_SIZE),
            )
            pygame.draw.rect(screen, BLUE, block)

    def turn(self, event):
        if (event.key == RIGHT) & (self.direction != WEST):
            self.direction = EAST
        elif (event.key == LEFT) & (self.direction != EAST):
            self.direction = WEST
        elif (event.key == UP) & (self.direction != SOUTH):
            self.direction = NORTH
        elif (event.key == DOWN) & (self.direction != NORTH):
            self.direction = SOUTH
        else:
            pass

    def crawl(self):
        if self.direction == EAST:
            self.positions.insert(0, (self.positions[0][0] + 1, self.positions[0][1]))
            del self.positions[-1]

        elif self.direction == WEST:
            self.positions.insert(0, (self.positions[0][0] - 1, self.positions[0][1]))
            del self.positions[-1]

        elif self.direction == NORTH:
            self.positions.insert(0, (self.positions[0][0], self.positions[0][1] - 1))
            del self.positions[-1]

        elif self.direction == SOUTH:
            self.positions.insert(0, (self.positions[0][0], self.positions[0][1] + 1))
            del self.positions[-1]
        else:
            pass

    def eat(self):
        x, y = self.positions[-1]
        direction = self.direction

        if direction == EAST:
            self.positions.append((x + 1, y))
        elif direction == WEST:
            self.positions.append((x - 1, y))
        elif direction == SOUTH:
            self.positions.append((x, y + 1))
        elif direction == NORTH:
            self.positions.append((x, y - 1))
        else:
            pass


class Apple:
    def __init__(self):
        self.color = RED
        x = random.randint(1, BOARD_SIZE[0] // 10)
        y = random.randint(1, BOARD_SIZE[1] // 10)
        self.position = (x, y)

    def draw(self, screen, position):
        block = pygame.Rect(
            (position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
            (BLOCK_SIZE, BLOCK_SIZE),
        )
        pygame.draw.rect(screen, self.color, block)


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.color = WHITE


def runGame():

    board = Board()
    snake = Snake()
    apple_box = []
    PLAYING = True

    screen = pygame.display.set_mode(board.size)

    isApple = False
    while PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PLAYING = False
            else:
                pass

            if event.type == pygame.KEYDOWN:
                snake.turn(event)

            else:
                pass

        # Board
        screen.fill(board.color)

        snake.draw(screen)
        snake.crawl()

        print(len(apple_box))
        if len(apple_box) == 0:
            apple = Apple()
            position = apple.position
            apple_box.append(position)

        apple.draw(screen, apple_box[0])

        if snake.positions[0] == apple.position:
            snake.eat()
            del apple_box[0]

        pygame.display.update()
        time.sleep(TURN_INTERVAL)


runGame()
pygame.quit()