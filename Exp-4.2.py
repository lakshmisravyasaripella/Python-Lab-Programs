s1=input("Enter first string:")
s2=input("Enter second string:")
if len(s1)!=len(s2):
    print("Length of the two strings are not same")
else:
    for i in range(len(s1)):
        print(s1[i]+s2[i],end="")
'''
Output:
Enter first string:abcde
Enter second string:ABCDE
aAbBcCdDeE
'''
    
            
