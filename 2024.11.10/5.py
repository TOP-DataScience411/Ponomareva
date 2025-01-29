 #==========  5  ========== 
from functools import reduce

def central_tendency(num1:float, num2:float,/,*numbers:float):
	"""
	Функция вычисляет основные меры центральной тенденции для некоторого количества чисел (среднее арифметическое, среднее геометрическое, среднее гармоническое и медиану)
	"""
	nums_list=(num1, num2, *numbers)
	nums_sorted=sorted(nums_list)
	n=len(nums_sorted)
	 
	arithmetic=sum(nums_sorted)/n
	
	if n%2==0:
		median=(nums_sorted[n//2-1]+nums_sorted[n//2])/2
	else:
		median=nums_sorted[n//2]
		 
	geometric=(reduce(lambda num1, num2: num1 * num2, nums_sorted))**(1/n) 
	 
	inverse_nums = tuple(map(lambda num: 1 / num, nums_sorted))
	harmonic=n/sum(inverse_nums)
		

	print({'arithmetic': arithmetic, 
			'median': median,
			'geometric': geometric,
			'harmonic': harmonic
		})
	
# >>> central_tendency(1,2,4,3)
# {'arithmetic': 2.5, 'median': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}	

# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'arithmetic': 3.0, 'median': 3, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}