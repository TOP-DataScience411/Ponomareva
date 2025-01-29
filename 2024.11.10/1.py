#======1======
def strong_password (symbols):
	"""Функция проверяет, является ли пароль надёжным.
	Пароль считается надёжным, если соблюдены все нижеследующие условия:
    - длина пароля составляет восемь символов и более
    - в пароле присутствуют буквенные символы в обоих регистрах
    - в пароле присутствуют минимум два символа цифр
    - кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)
	"""
		
	sym_list=list(symbols)
	letters=0
	nums=0
	other=0
	for sym in sym_list:
		if sym.isdigit():
			letters+=1
		elif sym.isalpha():
			nums+=1
		else:
			other+=1
	
	if (len(symbols)>=8 and
		symbols.islower()==False and
		nums>=2 and other>0):
			print('True')
			
	else:
		print('False')
	
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>> strong_password('_|fFaa*:')
# True
# >>> strong_password('ponomareva12')
# False