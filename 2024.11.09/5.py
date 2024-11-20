print('Введите слово:\n')

word=input()
word=word.upper()

letters=list(word)

scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

score=[]

for i in letters:
	for key, value in scores_letters.items():
		if i in value:
			score.append(key)
	
print(sum(score))

# Результат:

# Введите слово:

# архитектура
# 17