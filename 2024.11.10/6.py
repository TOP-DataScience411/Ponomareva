#==========  6  ==========

def orth_triangle(*, cathetus1=0, cathetus2=0, hypotenuse=0) -> float|None:
	"""
	Функция вычисляет третью сторону прямоугольного треугольника по двум переданным.
	"""
	if cathetus1==0 and cathetus2>hypotenuse:
		return None
		
	elif cathetus2==0 and cathetus1>hypotenuse:
		return None
	
	elif cathetus1!=0 and cathetus2!=0 and hypotenuse!=0: 
		return None
	else:
		cath_1=(hypotenuse**2-cathetus2**2)**(1/2)
		cath_2=(hypotenuse**2-cathetus1**2)**(1/2)
		hypoth=(cathetus1**2+cathetus2**2)**(1/2)
		
	if 	cathetus1==0:
		return cath_1
		
	elif cathetus2==0:
		return cath_2
	
	elif hypotenuse==0:
		return hypoth
	
	
# >>> orth_triangle(cathetus1=3,hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None