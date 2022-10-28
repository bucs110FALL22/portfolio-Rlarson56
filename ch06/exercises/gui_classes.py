##cd ch06/exercises
##python3 gui_classes.py
class Player1:
	def __init__(self):
    self.health_state = 2
    self.coins = 22
    self.lives = 2


class Enemy:
	def __init__(self):
    self.damage = 1
    self.health_state = 1


class Block:
	def __init__(brick):
    self.state = 1
    self.contents = 1 ##coin
    self.pos = (x,y) ##coordinates of brick block