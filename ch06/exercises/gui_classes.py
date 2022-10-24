##cd ch06/exercises
##python3 gui_classes.py
class Player1:
	def __init__(mario):
    mario.health_state = 2
    mario.coins = 22
    mario.lives = 2


class Enemy:
	def __init__(goomba):
    goomba.damage = 1
    goomba.health_state = 1


class Block:
	def __init__(brick):
    brick.state = 1
    brick.contents = 1 ##coin
    brick.pos = (x,y) ##coordinates of brick block