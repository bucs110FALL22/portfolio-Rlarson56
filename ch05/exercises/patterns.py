# cd ch05/exercises
# python3 patterns.py
rows=input("How many rows should your pyramid be?  ")
rows=int(rows)
def star_pyramid():
  star= "*"
  for i in range(rows):
    print(star)
    star = star + "*"

  for i in range(rows):
    star = star - 1
    print(star)
star_pyramid()