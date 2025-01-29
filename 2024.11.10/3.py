def numbers_strip (numbers:list[float],n:int=1,*,copy:bool=False)->list:
	"""
	Функция удаляет n минимальных и n максимальных чисел из списка.
	"""
	numbers_copy = numbers.copy()
	
	for i in range(n):
		numbers_copy.remove(max(numbers_copy))
		numbers_copy.remove(min(numbers_copy))
		
	return numbers_copy
	
# >>> sample = [1, 2, 3, 4]
# >>> numbers_strip(sample)
# [2, 3]
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]