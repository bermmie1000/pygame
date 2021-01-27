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
        self.size = [1000, 500]
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, x, y):
        figure = pygame.Rect(x, y, 10, 10)
        figure = pygame.draw.rect(screen, RED, figure)

        return figure


screen = pygame.display.set_mode(Board().size)


def runGame():
    board = Board()
    plane = Plane()
    missile_xy = []

    global done

    while not done:

        clock.tick(10)
        screen.fill(board.color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pass

            if event.type == pygame.KEYDOWN:
                plane.move(event)
                if event.key == SPACEBAR:
                    missile = Missile(plane.x + 50, plane.y + 15)
                    missile_xy.append([missile.x, missile.y])
            else:
                pass

        if len(missile_xy) != 0:
            for i, mxy in enumerate(missile_xy):
                mxy[0] += 15
                missile_xy[i][0] = mxy[0]
                missile.draw(screen, mxy[0], mxy[1])

                if mxy[0] >= board.size[0]:
                    missile_xy.remove(mxy)

        screen.blit(plane.draw(), (plane.x, plane.y))

        pygame.display.update()


runGame()
pygame.quit()