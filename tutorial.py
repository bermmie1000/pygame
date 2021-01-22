import pygame

pygame.init()

BOARD_COLOR = (255, 255, 255)
BOARD_SIZE = [400, 300]

screen = pygame.display.set_mode(BOARD_SIZE)
done = False
clock = pygame.time.Clock()

# airplane
plane = pygame.image.load("./images/plane.png")
plane = pygame.transform.scale(plane, (60, 45))

# bullet


def runGame():
    global done, plane
    x = 20
    y = 24

    while not done:
        # 상태 업데이트 -> 상태 표시 -> 사용자 입력 처리의 loop
        clock.tick(10)
        screen.fill(BOARD_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_SPACE:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((50, 50), (3, 3)))

        screen.blit(plane, (x, y))

        pygame.display.update()


runGame()
pygame.quit()
