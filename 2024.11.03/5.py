print('Введите текст телеграммы:\n')

tel=input()
tel=tel.replace(' ','')
a=len(tel)
print(f'\n{(a*30)//100} руб. {(a*30)%100} коп.')

#Результат:

# Введите текст телеграммы:

# Gaudeamus igitur Juvenes dum sumus

# 9 руб. 0 коп.
