# =======2=======
print('Введите названия фруктов:\n')
fruits=[]
while True:
	fruit=input()
	fruits.append(fruit)
	if fruit=='':
		break

l=len(fruits)

if l==2:
	d=fruits[0]
	print(d)
	
elif l==3:
	b= ' и '.join(fruits[0:2])
	print(b)
	
else:
	c=', '.join(fruits[0:(l-3)])
	d=' и '.join(fruits[(l-3):(l-1)])
	print(c+',',d)
	
# Результат1:

# Введите названия фруктов:

# яблоко

# яблоко

# Результат2:
	
# Введите названия фруктов:

# яблоко
# груша

# яблоко и груша

# Результат3:
	
# Введите названия фруктов:

# яблоко
# груша
# мандарин
# киви

# яблоко, груша, мандарин и киви