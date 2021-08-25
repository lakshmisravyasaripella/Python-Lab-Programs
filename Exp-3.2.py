import random
r=random.randint(1,10)
guess=int(input("Guess the number"))
if(guess==r):
    print("Your guess is right")
else:
    print("Your guess is wrong")
'''
Output:
Guess the number9
Your guess is wrong
'''
