def first_diff(str1, str2):
    ms = min(len(str1), len(str2))
    for i in range(ms):
        if str1[i] != str2[i]: return i
    return -1
first_str = input("Enter String 1: ")
second_str = input("Enter String 2: ")
print(first_diff(first_str, second_str))
'''
Output:
Enter String 1: python
Enter String 2: python
-1

Enter String 1: python
Enter String 2: pycharm
2
'''
