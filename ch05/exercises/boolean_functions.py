## cd ch05/exercises
## python3 boolean_functions.py
score = input("What score did you get?  ")
score= int(score)
passing = 0
grade = "x"
def percentage_to_letter(score):
  if score >= 90:
     grade = "a"
  elif score < 90 and score > 80:
     grade = "b"
  elif score < 80 and score > 70:
     grade = "c"
  elif score < 70 and score > 60:
     grade = "d"
  elif score < 60:
     grade = "f"
  print("Your grade is a",grade)

def is_passing(grade):
 if grade == "a" or "b" or "c":
   print("You're passing")
 elif grade == "d" or "f":
    print("You're not passing")

percentage_to_letter(score)
is_passing(grade)

