# =======2=======
print('Введите количество чисел, затем начинайте вводить числа:\n') 

n=int(input())
numbers=[]

while True:
	nums=int(input())
	numbers.append(nums)
	if len(numbers)==n:
		break
		
positive = []
for i in numbers:
    if i > 0:
        positive.append(i)
		
print ('\n',sum(positive), sep='')


# Результат

# Введите количество чисел, затем начинайте вводить числа:

# 4
# -1
# 2
# -3
# 4

# 6