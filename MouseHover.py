import pygame
import Window

def printSlop(): {
    print("Slop")
}

while Window.RUNNING:
    Window.CLOCK.tick(60)
    mousePos = pygame.mouse.get_pos()
    print(pygame.mouse.get_pressed())
    print("Ts workes")