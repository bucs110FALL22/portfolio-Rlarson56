#cd ch10/final
#python3 main.py
import pygame 
import AdviceAPI
from sys import exit

def main():
  pygame.init()
  width=610
  height=400
  x = 0
  y = 0
  x2=140
  y2=170
  size=14
  black=(0,0,0)
  screen = pygame.display.set_mode((width, height ))
  pygame.display.set_caption('Fortune Cookie')
  Image = pygame.image.load("cookie.jpeg").convert()#creates the surface using the cookie image
  screen.blit(Image, ( x,y))
  pygame.display.flip()
  advice = AdviceAPI.AdviceAPI()
  slip = advice.get()#runs code in AdviceAPI and assigns unique advice to variable
  pygame.font.init()
  font = pygame.font.Font(None, size)
  text = font.render(slip, True, black)
  screen.blit(text, (x2,y2))
  pygame.display.update()
  pygame.display.flip()
main()

while True: #keeps window open until x is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()