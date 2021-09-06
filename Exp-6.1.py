list_with_dups=[1,2,1,3,4,3,0,2,0]
print("Using set to remove duplicates")
list_without_dups_no_input_order=list(set(list_with_dups))
print("List with Duplicates:",list_with_dups)
print("List without Duplicates and no input order:",list_without_dups_no_input_order) 
'''
Output:
Using set to remove duplicates
List with Duplicates: 1 2 1 3 4 3 0 2 0
List without Duplicates and no input order: 0 1 2 3 4
'''
