print('\nВведите сначала целую часть значения в милях, потом дробную:')
a=input()
b=input()
# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше одного (см. тест ниже) — придумайте более универсальное решение
c=int(a)+float(int(b)/10)

# ИСПРАВИТЬ: одна миля больше одного километра
print('\n'f'{c} миль = {c/1.61:.1f} км')

# УДАЛИТЬ: если результат округления должен быть в дальнейшем использован как число, тогда имеет смысл использовать функцию round(); а в контексте данной задачи оптимальнее воспользоваться синтаксисом f-строк
#print('\n'f'{c} миль = {round(c/1.61,1)} км')


# Введите сначала целую часть значения в милях, потом дробную:
# 3
# 4
# 
# 3.4 миль = 2.1 км

# Введите сначала целую часть значения в милях, потом дробную:
# 5
# 81
# 
# 13.1 миль = 8.1 км
# КОММЕНТАРИЙ: должно быть 
# 5.81 миль = 9.4 км


# ИТОГ: доработать — 1/5

