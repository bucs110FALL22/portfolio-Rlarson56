import random
#Part A
weeks = 16
print(weeks, "This is a numeric variable")
classes = 3
print(classes, "This is a numeric variable")
tuition = 6000
print(tuition, "This is a numeric variable")
cost_per_week = ((tuition / classes) / weeks)
print("The cost of my CS class is per week:", cost_per_week, "dollars")


#Part B
list=(1,2,3,4,5)
rlist=random.choice(list)
print(rlist)