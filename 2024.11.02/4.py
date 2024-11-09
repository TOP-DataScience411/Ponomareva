print('Введите координаты клетки:', end='\n\n')
v1=input()
v2=input()
print()

t1=v1[0]
t2=int(v1[1])

p1=v2[0]
p2=int(v2[1])

if v1==v2:
	print('да')	

elif ((t1 in ('a','c','e','g') 
		and p1 in ('a','c','e','g')) 
		and	(t2==p2 or abs(t2-p2)%2==0)):
	print('да')

elif ((t1 in ('a','c','e','g') 
		and p1 in ('b','d','f','h'))
		and (abs(t2-p2)%2!=0 or abs(t2-p2)==1)):
	print('да')

elif ((t1 in ('b','d','f','h') 
		and p1 in ('a','c','e','g'))
		and	(abs(t2-p2)%2!=0 or abs(t2-p2)==1)):
	print('да')

elif ((t1 in ('b','d','f','h') 
		and p1 in ('b','d','f','h'))
		and (t2==p2 or abs(t2-p2)%2==0)):
	print('да')

else:
	print('нет')
	
	
#Результат1:

# Введите координаты клетки:

# b3
# c7

# нет


#Результат2:

# Введите координаты клетки:

# c4
# f7

# да