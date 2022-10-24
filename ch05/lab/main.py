## cd ch05/lab
## python3 main.py
import pygame
pygame.init()
max_so_far = 0
upper_limit = 20
iters = { }
start=range(2,upper_limit)
font = pygame.font.Font(None,7)
msg = font.render("Waddup", True,False, "black")
display = pygame.display.set_mode()
new_display = pygame.transform.flip(display, False, True)
pygame.init()
for i in start:
 count = 0
 key = input("Enter a positive integer  ")
 key = int(key)
 n = key
 print(n)
 while n != 1:
   if n %2 == 0:
       n=n/2
       count = count + 1
       print(n)
   else:
       n = 3 * n + 1
       count = count + 1
       print(n)
   if count > max_so_far:
     max_so_far = count
     max_val = key
   iters = {key : count}
   iters = iters.items()
print(iters)


pygame.draw.lines(display, "white", False, iters)
display.blit(msg, 10,10)
##add these points to a list