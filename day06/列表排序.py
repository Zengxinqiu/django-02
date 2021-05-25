# 列表排序 ，列表中的数据的类型要保持一致
my_list = [1, 3, 5, 4, 2, 1]
my_list.sort()
print(my_list)


list1 = [{'name': 'd', 'age': 19},
         {'name': 'b', 'age': 16},
         {'name': 'a', 'age': 16},
         {'name': 'c', 'age': 20}]

# list1.sort()   程序报错
# 匿名函数的形参是列表中的每一个数据
list1.sort(key=lambda x: x['name'])
print(list1)
list1.sort(key=lambda x: x['age'])
print(list1)


list2 = ['aghdd', 'bc', 'ghli', 'def', 'ab']
list2.sort()
