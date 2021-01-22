import pygame

pygame.init()

# CONSTANTS
WHITE = (255, 255, 255)
done = False
clock = pygame.time.Clock()

RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
UP = pygame.K_UP
DOWN = pygame.K_DOWN

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

    def move(self, key):
        if key == 

class Missile:
    def __init__(self, plane_x, plane_y):
        self.x = plane_x + 30
        self.y = plane_y + 30


screen = pygame.display.set_mode(Board().size)


def runGame():
    board = Board()
    plane = Plane()
    missile = Missile(plane.x, plane.y)

    global done
    while not done:
        clock.tick(10)
        screen.fill(board.color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(plane.draw(), (plane.x, plane.y))
        pygame.display.update()


runGame()
pygame.quit()