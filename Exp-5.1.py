list1=[]
import random
for i in range(20):
    list1.append(random.randint(1,100))
print(list1)
print("Average of elements in the list:",sum(list1)//len(list1))
print("Largest of the list:",max(list1))
print("Smallest of the list:",min(list1))
list1.sort()
print("Second largest of the list:",list1[-2])
print("Second smallest of the list:",list1[1])
count=0
for i in list1:
    if i%2==0:
        count+=1
print("No.of even numbers in the list:",count)

    

    
