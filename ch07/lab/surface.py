from rectangle import Rectangle

class Surface:
   def __init__(self, filename, x, y, h, w):
     self.rect = getRect(self)
     self.image = filename

   def getRect(self):
     return Rectangle()
