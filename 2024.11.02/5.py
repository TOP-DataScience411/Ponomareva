print('Введите координаты клетки:', end='\n\n')
v1=input()
v2=input()
print()

t1=v1[0]
t2=v1[1]

p1=v2[0]
p2=v2[1]

if (t1==p1 or t2==p2) and v1!=v2:
	print ('да')
	
else: 
	print ('нет')
	
	
#Результат1:

# Введите координаты клетки:

# f2
# h2

# да


#Результат2:

# Введите координаты клетки:

# a2
# b4

# нет