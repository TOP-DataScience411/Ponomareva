# =======1=======
print('Введите адрес электронной почты:\n')
 
email=input()

a=email.find('@')
b=email.find('.', a)

if a==-1 or b==-1:
	print('нет')
	
else:
	print('да')
	
	
# Результаты:
	
# Введите адрес электронной почты:

# olga@gmail.com
# да

# Введите адрес электронной почты:

# olgagmail.com
# нет

# Введите адрес электронной почты:

# olga@gmail
# нет

