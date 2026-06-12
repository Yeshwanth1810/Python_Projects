import random 
print("Enter the Lower and Upper Value")
lower_number=int(input("Enter the Lower Bound : "))
Upper_bound=int(input("Enter the Upper Bound : "))
num=random.randint(lower_number,Upper_bound)
ch=7
count=0
print("You've 7 Chances to Predict the Correct Number")
while count<ch:
    count+=1
    guess=int(input("Enter the Number : "))
    if guess==num:
        print(f"You've Guessed the Correct Number in {count} Chances ")
        break
    elif count>=ch and num!=guess:
        print("You've Completed your chances,Better Luch nextTime !")
    elif guess>num:
        print("Too High")
    elif guess<num:
        print("Too low")
        