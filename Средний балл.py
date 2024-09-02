grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = sum(grades[0])/len(grades[0])
b = sum(grades[1])/len(grades[1])
v = sum(grades[2])/len(grades[2])
g = sum(grades[3])/len(grades[3])
d = sum(grades[4])/len(grades[4])
# print(a,b,v,g,d)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list_sort= sorted(students_list)
# print(students_list_sort)
aa = students_list_sort[0]
bb = students_list_sort[1]
vv = students_list_sort[2]
gg = students_list_sort[3]
dd = students_list_sort[4]
average_grades = { aa: a, bb:b, vv:v, gg:g, dd:d}
print(average_grades)
