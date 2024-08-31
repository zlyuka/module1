immutable_var = 1, 3.45, 'мяу', True
print(immutable_var)
# immutable_var [0] = 'vo'
# Не возможно выполнить замену элментов когда они являются в нутри кортежа. 
print(immutable_var)

mutable_list = [1, 3.44, 'nya', True]
print(mutable_list)
mutable_list [1] = 'nnn'
print(mutable_list)

