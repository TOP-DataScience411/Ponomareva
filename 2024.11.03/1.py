# =======1=======
n=[]

print('Вводите числа кратные 7:', end='\n\n') 

while True:
	num=int(input())
	if int(num)%7!=0:
		break

	n.append(num)
	n_rev=n[::-1]
	n_str=[str(i) for i in n_rev]
	n_fin=' '.join(n_str)
	
print('\n',n_fin, sep='')


#Результат:
	
# Вводите числа кратные 7:

# 42
# 21
# 63
# 7
# 56
# 23

# 56 7 63 21 42