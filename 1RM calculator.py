"""
This works out how to find your 1 rep max on any exercise
"""

lift = input("What kind of lift do you do; ").upper()
weight_lifted = int(input("Weight lifted: "))
reps = int(input("Reps: "))

one_rm = weight_lifted * (1 + reps / 30)


if lift == "SQUAT":
    print(f"Your Squat 1 rep max is about: {one_rm}")
elif lift == "BENCH PRESS":
    print(f"Your Bench Press 1 rep max is about: {one_rm}")
elif lift == "DEADLIFT":
    print(f"Your Deadlift 1 rep max is about: {one_rm}")
