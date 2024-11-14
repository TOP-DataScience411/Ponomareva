# =======4=======
print('Введите натуральное число:\n') 

divisors=[]
primes=[]
n=int(input())
a=int('1'+'0'*(n-1))
b=int('1'+'0'*n)

for i in range(a,b):
	divisors.clear()
	for j in range(1,i+1):
		if i%j==0:
			divisors.append(j)
	if len(divisors)==2:
		primes.append(i)
				
print(len(primes))

#Результат:

# Введите натуральное число:

# 2
# 21