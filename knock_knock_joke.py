#(2) [Control statement and array] 
# Let's make a knock knock joke. 

import random

names = ["Luke", "Tank", "Figs", "Annie"]

jokes = ["Luke through the peep hole and find out.", "You’re welcome.", "Figs the doorbell, it’s not working!", "Annie thing you can do, I can do too!"]

usr=input("Knock, Knock! ")

while True:
    
    if usr != "Who's there?":
        print("You must type: Who's there?")
        usr=input("Knock, Knock! ")
    else:
        break

index = random.randint(0,3)
name = names[index]
usr2 = input(f"{name}. ")


while True:
    if usr2 != f"{name} who?":
        print(f"You must type: {name} who?")
        usr2 = input(f"{name}. ")
    else:
        break

print(jokes[index])












