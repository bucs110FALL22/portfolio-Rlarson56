import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

red = [255, 0, 0]
yellow = [255,255,0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

direction = ["UP","DOWN", "LEFT", "RIGHT"]

print("UP: red")
screen.fill(red)
pygame.time.wait(200)
print("DOWN: yellow")
screen.fill(yellow)
pygame.time.wait(200)
print("LEFT: green")
screen.fill(green)
pygame.time.wait(200)
print("RIGHT: blue")
screen.fill(blue)