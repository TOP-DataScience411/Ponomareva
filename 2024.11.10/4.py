# ==========  4  ========== 
def countable_nouns(number:int, noun:tuple[str, str, str]):
	"""
	Функция возвращает существительное русского языка, согласованное с числом.
	"""
	str_num=str(number)
	figures=list(str_num)
	last_fig=int(figures[-1])
	if last_fig==1 and number%100!=11:
		return noun[0] 
		
	elif last_fig in range(2,5) and number%100 not in range(12,15):
		return noun[1]
		
	else:
		return noun[2]
		
		
# >>> countable_nouns(21,("год", "года", "лет"))
# 'год'
# >>> countable_nouns(211,("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(1,("год", "года", "лет"))
# 'год'
# >>> countable_nouns(12,("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(25,("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(364,("год", "года", "лет"))
# 'года'
# >>> countable_nouns(0,("год", "года", "лет"))
# 'лет'