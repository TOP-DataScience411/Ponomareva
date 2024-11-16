#=======8=======
print('Введите натуральное число:\n')

n=int(input())

fib=[]
a,b=1,1

for i in range(n):
	fib.append(a)
	a,b=b,a+b

fib_str=[str(i) for i in fib]
fib2=' '.join(fib_str)

print(fib2)

# Результат:
	
# Введите натуральное число:

# 10
# 1 1 2 3 5 8 13 21 34 55
	
	
	
	
	