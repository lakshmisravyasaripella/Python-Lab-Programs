def sum_digits(num):
    return sum([int(d) for d in num])
n = input("Enter an integer number: ")
print("Sum of digits of",n,"is",sum_digits(n))
'''
Output:
Enter an integer number: 12345
Sum of digits of 12345 is 15
'''
