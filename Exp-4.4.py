exp= input("Enter algebric expression:")
conv_exp= ''
for ch in exp:
    if ch>='0' and ch<='9':
        conv_exp=conv_exp+ch
    elif ch=='(':
        conv_exp=conv_exp+'*'+ch
    elif ch>='a' and ch<='z' and conv_exp[-1]!='(':
        conv_exp=conv_exp+'*'+ch
    else:
        conv_exp=conv_exp+ch
print("Converted expression is :",conv_exp)
'''
Output:
Enter algebric expression:3x+4y
Converted expression is : 3*x+4*y

Enter algebric expression:3(x+5)
Converted expression is : 3*(x+5)
'''
