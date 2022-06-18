# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random


# def sequece_of_num(num_list):
#     new_list = []
#     for i in range(len(num_list)):
#         if i not in new_list:
#                 new_list.append(i)
#
#     return new_list

list_len = int(input("Введи длину списка = "))

my_list = []
for e in range(list_len):
    my_list.append(random.randint(1, 10))
print(my_list)

new_list = list(set(my_list))
print(new_list)
