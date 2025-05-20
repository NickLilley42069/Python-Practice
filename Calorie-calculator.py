"""
This will be a Calorie calculator based on whether somebody is trying to lose weight (cut), lose body fat (maintance) or if
they are trying to gain weight (bulk)
"""

def cut_expo():
    """
    Cutting calories means eating fewer than your body burns to 
    promote fat loss. It typically involves a 300–500 calorie daily 
    deficit. This helps the body use stored fat for energy. 
    It’s important to maintain sufficient protein and nutrients 
    while cutting to preserve muscle and overall health."""

def main_expo():
    """Maintenance calories are the number of calories you need to eat to 
    keep your current weight stable. This level matches your total daily 
    energy expenditure (TDEE). Eating at maintenance supports bodily 
    functions, energy levels, and workout performance without significant
    fat gain or loss, making it ideal for recomposition or balance."""

def bulk_expo():
    """Bulking involves consuming more calories than your body needs 
    to build muscle. A surplus of 300–500 calories daily supports 
    muscle growth when combined with resistance training. 
    Clean bulking focuses on nutrient-dense foods to minimize fat gain, 
    while "dirty bulking" often includes high-calorie, 
    less nutritious foods for faster mass."""


#Deciding factors;
sex = input("What was your gender at birth; ").capitalize()
age = int(input("Please enter your age; "))
height = int(input("Please enter your height in cm; "))
weight = int(input("Please enter your weight in cm; "))
activity_lvl = int(input("How many days per week do you exercise: (1-5) "))

#BMR caclulator based on gender
def M_BMR():
    return (10 * weight) + (6.25 * height) - (5 * age) + 5
def F_BMR():
    return (10 * weight) + (6.25 * height) - (5 * age) - 161

def BMR():
    if sex in ["Male", "M"]:
        return M_BMR()
    elif sex in ["Female", "F"]:
        return F_BMR()

#TDEE
def TDEE():
    if 1 < activity_lvl <= 2:
        calories = BMR() * 1.2
        return calories
    elif 2 < activity_lvl <= 3:
        calories = BMR() * 1.375
        return calories
    elif 3 < activity_lvl <= 4:
        calories = BMR() * 1.55
        return calories
    elif 4 < activity_lvl <= 5:
        calories = BMR() * 1.9
        return calories
    
#Decision
Plan = input("What is your plan? (please enter CUT, MAINTANCE or BULK); ").upper()
    
    #CUT
if Plan == 'CUT':
    calorie_goal = TDEE() - 500
    print(cut_expo.__doc__)
    print(f"So with this in mind, your Cut calories is; {int(calorie_goal)}")
    
    #MAINTENANCE
elif Plan == 'MAINTENANCE':
    calorie_goal = TDEE()
    print(main_expo.__doc__)
    print(f"So with this in mind, your MAINTENANCE calories is; {int(calorie_goal)}")
    
    #BULK
elif Plan == 'BULK':
    calorie_goal = TDEE() + 500
    print(bulk_expo.__doc__)
    print(f"So with this in mind, your BULK calories is; {int(calorie_goal)}")

#outcome
2