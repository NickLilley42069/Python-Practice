#this is going to be some Python Practice so I can get better at it

#Variables. behaves as if it was the value it contains
"""
strings = Words and letters
interger = Numbers - whole numbers
float = numbers - decimal numbers
boolean = 
"""

"""#strings
first_name = "Nicholas Lilley" 
food = "Spaghetti Bolognese"

#intergers - whole numbers
age = 19



#float - decimal numbers
def pr():
    bench_pr = 70.9
    deadlift_pr = 105.5
    squat_pr = 50.5
    return bench_pr, deadlift_pr, squat_pr

bench_pr, deadlift_pr, squat_pr = pr()

#Boolean - True or False
lying = True


print(f"Hello, my name is {first_name}" + f", my favourite food is {food}, " +
      f"I am {age}" + f", my compound pr's are: Bench; {bench_pr}" + 
      f"Deadlift; {deadlift_pr}, Squats; {squat_pr}. " + f"Did I lie? {lying}")
"""
#type casting
"""print(type(first_name))
print(type(age))
print(type(pr))
print(type(bench_pr))
print(type(lying))

bench_pr = int(bench_pr)

print(bench_pr)

age += 0.11
age = float(age)

print(age)"""

#input
"""kg = input("How much do you weigh? ")
kg = int(kg)

goal_kg = kg - 8

print(f"You also weigh: {kg}kg")
print(f"you need to get down to: {goal_kg}")"""

#rectangle area calculation - EXERCISE 1
length = float(input("What is the length of your rectangle; "))
width = float(input("What is the Width of your rectangle; "))

area_of_rectangle = length * width

print(area_of_rectangle)
#Shopping cart program - EXERCISE 2.
item = input("What Item do you want to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many of that Item do you want? "))

total = price * quantity

print(f"your total price for; {item} is {total}, this because you want; {quantity} and they cost {price}")
