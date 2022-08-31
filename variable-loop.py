#(1) [Variable and Loop]  

print("Hi! I can calculate the sum of all the integers in a given range.")
n1 = input("Give me a starting integer for the range: ")

while True:
    
    if n1.isnumeric(): 
        break
    
    else:
        n1 = input("Give me a starting integer for the range: ")

n1=int(n1)
print(f"Your starting number is {n1}")

n2 = input("Give me an ending integer for the range: ")

while True:
    
    if n2.isnumeric(): 
        break
    
    else:
        n2 = input("Give me a starting integer for the range: ")

n2=int(n2)
print(f"Your ending number is {n2}")


def add_all_integers(n1, n2):
    #calculate the sum of all integers

    if n2 > n1:
        total_sum = sum(range(n1,n2+1))

    else:
        print("Your ending value is smaller than your starting value.")
        print(f'Your starting integer will be {n2}.')
        print(f'Your ending integer will be {n1}.')
        total_sum = sum(range(n2,n1+1))
            
    return total_sum
    
    
total_sum = add_all_integers(n1, n2)

print(f"The sum of all integers is: {total_sum}")


