import pygame
from datetime import datetime, timedelta

pygame.init()

# CONSTANTS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
done = False
clock = pygame.time.Clock()
last_moved_time = datetime.now()

RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
SPACEBAR = pygame.K_SPACE


class Board:
    def __init__(self):
        self.size = [500, 500]
        self.color = WHITE


class Plane:
    def __init__(self):
        self.x = 70
        self.y = 70

    def draw(self):
        figure = pygame.image.load("./images/plane.png")
        figure = pygame.transform.scale(figure, (60, 45))
        return figure

    def move(self, event):
        if event.key == DOWN:
            self.y += 10
        elif event.key == UP:
            self.y -= 10
        else:
            pass


class Missile:
    def __init__(self, plane_x, plane_y):
        self.x = plane_x + 60
        self.y = plane_y + 15

    def draw(self, screen, event):

        if event.key == SPACEBAR:
            figure = pygame.Rect(self.x, self.y, 10, 10)
            figure = pygame.draw.rect(screen, RED, figure)

            return figure
        else:
            pass

    def move(self):
        self.x = self.x + 10


screen = pygame.display.set_mode(Board().size)


def runGame():
    board = Board()
    plane = Plane()
    missiles = []

    global done

    while not done:
        missile = Missile(plane.x, plane.y)

        clock.tick(10)
        screen.fill(board.color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pass

            if event.type == pygame.KEYDOWN:
                plane.move(event)
                one = missile.draw(screen, event)
                one.move()
            else:
                pass

        for i in missiles:
            i.move()

        screen.blit(plane.draw(), (plane.x, plane.y))

        pygame.display.update()


runGame()
pygame.quit()