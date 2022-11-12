class StringUnity:
  
  def __init__(self, string):
    self.string = string
    return string 
   

  def __str__(self):
    return self

  def vowels(self):
    vcount = len(self)
    num = 0
    vowels = 0
    
    if  count <= 4:
      for i in count:
        if self[num] is "a" or "e" or "i" or "u":
          vowel = vowel + 1
        num = num + 1
    else:
      return "many"

  def bothEnds(self):
    bcount = len(self)
    if bcount <= 2:
      self = ""
    else:
      self = self[0] + self[1] + self[len(self)] + self[len(self) - 1]
 
  def fixStart(self):
    new = self[0]
    fcount = len(self)
    fnum = 1
    for fcount in self:
      if self[fnum] == new:
       self[fnum] = "*"
        fnum = fnum + 1

  def asciiSum(self):
    self = ord(self)

  
  def cipher(self):
    return ''.join(chr(ord(char) + 3) for char in self)