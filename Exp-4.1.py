s=input("Enter a word:")
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print("Contains vowels")
        break
else:
    print("Does not contain vowels")
'''
Output:
Enter a word:Aditya
Contains vowels

Enter a word:Sls
Does not contain vowels

Enter a word:Pavan
Contains vowels
'''
