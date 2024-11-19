# =======4=======
print('Сформируйте словарь:\n')
my_list=[]
my_dict={}
while True:
	ex=input()
	my_list.append(ex)
	n=len(my_list)
	for i in my_list[0:(n-1)]:
		v=i.split()
		my_dict[v[0]]=v[1]
	if ex=='':
		break

print('Введите значение из словаря:\n')
a=input()
for num, text in my_dict.items():
	if text==a:
		print(num)
	
if a not in my_dict.values(): 
		print('! value error !')
		
		
		
# Результат1:

# Сформируйте словарь:

# 1 AAA
# 2 BBB
# 3 CCC

# Введите значение из словаря:

# BBB
# 2

# Результат2:

# Сформируйте словарь:

# 1 AAA
# 2 BBB
# 3 CCC

# Введите значение из словаря:

# DDD
# ! value error !