# ========6========
print('Введите 6-значный номер транспортного билета:\n')

num=input()

num=num.replace('',' ')
num=num.split()
int_num=[]
for i in num:
	int_num.append(int(i))

if sum(int_num[0:3])==sum(int_num[-1:-4:-1]):
	print('Да')
	
else:
	print('Нет')


# Результат1:

# Введите номер транспортного билета:

# 123114
# Да

# Результат2:

# Введите номер транспортного билета:

# 345123
# Нет