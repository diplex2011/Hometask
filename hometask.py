Посчитать количество элементов в списке name. names = ['Ann', 'Bob', 'Suzan', 'Radonir', 'Fill', 'Sam', 'Al']
len(names)
7
Посчитать количество элементов в списке ages. ages = [12, 33, 56, 87, 4, 18, 21]
len(ages)
7
Посчитать количество элементов в строке text_a. text_a = "Special cases aren't special enough to break the rules."
len(text_a)
55
Посчитать количество элементов в строке text_b. text_b = "In the face of ambiguity, refuse the temptation to guess."
len(text_b)
57
Посчитать сумму элементов списка ages. ages = [12, 33, 56, 87, 4, 18, 21]
sum(ages)
231
Вывести максимальный элемент списка ages. ages = [12, 33, 56, 87, 4, 18, 21]
max(ages)
87
Вывести минимальный элемент списка ages. ages = [12, 33, 56, 87, 4, 18, 21]
min(ages)
4
Найти самое короткое слово в text_a. text_a = "Special cases aren't special enough to break the rules."
s = input()
w = 0
min_w = len(s)
for i in s:
	if 'a'<=i<='z' or 'A'<=i<='Z' \
	or 'а'<=i<='я' or 'А'<=i<='Я':
		w += 1
	else:
		if w < min_w and w != 0:
			min_w = w
		w = 0
 
print(min_w)

Найти самое длинное слово в text_b. text_b = "In the face of ambiguity, refuse the temptation to guess."
