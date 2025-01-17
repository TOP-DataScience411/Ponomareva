#======1======
def strong_password (symbols):
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