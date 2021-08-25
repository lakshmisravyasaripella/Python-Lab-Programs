n1=float(input("Enter first number:"))
n2=float(input("Enter secomd number:"))
diff=abs(n1-n2)
if(diff<=0.001):
    print("Close")
else:
    print("Not close")
'''
Output:
Enter first number:1.2
Enter secomd number:1.21
Not close

Enter first number:4.567
Enter secomd number:3.232
Not close

Enter first number:3.217
Enter secomd number:3.218
Close
'''
