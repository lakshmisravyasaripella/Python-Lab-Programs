import math
def number_of_factors(num):
    count = 2
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count += 1 if num // i == i else 2
    return count if num > 2 else num
n = int(input("Enter a number: "))
print("No. of Factors for",n,":",number_of_factors(n))
'''
Output:
Enter a number: 15
No. of Factors for 15 : 4

Enter a number: 5
No. of Factors for 4 : 2
'''
