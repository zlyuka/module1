my_dict = {'Даша': 1996, 'Макс': 1965, 'Кирилл':1985, 'Алексей': 1990}
print(my_dict)
print(my_dict.get('Даша'))
print(my_dict.get('Денис','Значение ключа не найдено'))
my_dict.update({'Антон': 1956,
                'Ден': 1988})
a = my_dict.pop('Антон')
print(f'Удаленная переменная {a}')
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 3, True, 3.14, 'Мяу', 'Ня'}
print(my_set)
my_set.update(['Nya','non'])
print(my_set)
my_set.discard('Ня')
print(my_set)

