print('Введите год:', end='\n\n')
year=int(input())
print()

if (year%4==0 and year%100!=0) or year%400==0:
	print ('да')
	
else:
	print ('нет')
	
	
#Результат1:

# Введите год:

# 2020

# да

#Результат2:
	
# Введите год:

# 1999

# нет	