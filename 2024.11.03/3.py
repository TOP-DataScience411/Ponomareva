# =======3=======
print('Введите натуральное число:\n') 

n=int(input())
divisors=[]


for i in range(1,n+1):
	d=n/i
	if n%i==0:
		divisors.append(d)
		
print ('\n',int(sum(divisors)), sep='')