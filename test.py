import pygame

pygame.init()

# CONSTANTS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
done = False
clock = pygame.time.Clock()

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
        self.x = plane_x + 30
        self.y = plane_y + 30

    def draw(self, screen, event):
        figure = pygame.Rect(self.x + 30, self.y - 10, 3, 3)
        figure = pygame.draw.rect(screen, RED, figure)

        if event.key == SPACEBAR:
            return figure
        else:
            pass

    def move(self, event, screen):
        pass


screen = pygame.display.set_mode(Board().size)


def runGame():
    board = Board()
    plane = Plane()

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
                missile.draw(screen, event)
            else:
                pass

        screen.blit(plane.draw(), (plane.x, plane.y))

        pygame.display.update()


runGame()
pygame.quit()