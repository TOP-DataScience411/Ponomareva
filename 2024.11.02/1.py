print('Введите три числа:', end='\n\n')
n1=float(input())
n2=float(input())
n3=float(input())
print()

if n1>0 and n2>0 and n3>0:
	print(n1+n2+n3)
	
elif n1>0 and n2>0 and n3<=0:
	print(n1+n2)
	
elif n1>0 and n2<=0 and n3<=0:
	print(n1)
	
elif n1<=0 and n2>0 and n3<=0:
	print(n2)
	
elif n1<=0 and n2>0 and n3>0:
	print(n2+n3)
	
elif n1<=0 and n2<=0 and n3>0:
	print(n3)
	
elif n1>0 and n2<=0 and n3>0:
	print(n1+n3)
	
else:
	print(0)

#Результат:
	
# Введите три числа:

# 56
# -3
# 0.5

# 56.5