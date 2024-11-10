print('Введите координаты клетки:', end='\n\n')
v1=input()
v2=input()
print()

t1=v1[0]
t2=int(v1[1])

p1=v2[0]
p2=int(v2[1])

k=['a','b','c','d','e','f','g','h']

if t1==p1 and (abs(t2-p2)==1):
	print('да')
	
elif t2==p2 and abs(k.index(t1)-k.index(p1))==1:
	print('да')

elif (abs(t2-p2)==1) and abs(k.index(t1)-k.index(p1))==1:
	print('да')
	
else:
	print('нет')
	
# Результат 1:
	
# Введите координаты клетки:

# b4
# a3

# да

# Результат 2:
	
# Введите координаты клетки:

# c5
# d8

# нет