import random
def longest_zero_runlength(bin_list):
    max=0
    count=0
    for x in bin_list:
        if x==0:
            count+=1
        else:
            if count>max:
                max=count
                count=0
    return max
bin_list=[random.randint(0,1) for x in range(100)]
print("Binary List:",bin_list)
print(f'Longest run of zeros={longest_zero_runlength(bin_list)}')
'''
Output:
Binary List: [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
Longest run of zeros=12
'''
