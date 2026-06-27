import pygame
pygame.init()
SCREEN = pygame.display.set_mode((800,600))
pygame.display.set_caption("PYGAME OS v0.1")
CLOCK = pygame.time.Clock()
FRAMERATE_CAP = 60

Windows = {
    "Welcome": {
        "Pos": (200,200),
        "Size": (200,200)
    }
}

def initWindow(pos, size): {

}


RUNNING = True
while RUNNING:
    CLOCK.tick(FRAMERATE_CAP)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    mousePos = pygame.mouse.get_pos()