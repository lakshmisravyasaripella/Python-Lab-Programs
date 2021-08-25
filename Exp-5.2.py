n=int(input("Enter a number:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)
'''
Output:
Enter a number:12
[1, 2, 3, 4, 6, 12]
'''
    
