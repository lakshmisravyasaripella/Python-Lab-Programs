units =['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 
'kilometers']
conv_from_feet =[12, 0.33333, 0.000189393939, 304.8, 30.48, 0.3048, 0.0003048]
feets=float(input('Enter length in feets:'))
for i,v in enumerate(units):
    print(f'Enter {i+1} to convert feets to {v}')
i = int(input('Enter your choice:'))-1
print(f'{feets}feets={feets*conv_from_feet[i]:.2f}{units[i]}')
'''
Output:
Enter length in feets:10
Enter 1 to convert feets to inches
Enter 2 to convert feets to yards
Enter 3 to convert feets to miles
Enter 4 to convert feets to millimeters
Enter 5 to convert feets to centimeters
Enter 6 to convert feets to meters
Enter 7 to convert feets to kilometers
Enter your choice:1
10.0feets=120.00inches
'''
