# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)
import re
from operator import methodcaller


def my_map(l):
    list_split = []
    for i in range(1, len(l) - 1):
        num_split = re.split('\^|x', l[i])
        num_split[0] = int(num_split[0])
        list_split.append(num_split)
    return list_split

path1 = "palynom.txt"
data1 = open(path1, 'r')
for line in data1:
    string1 = line
    print(string1)

path2 = "palynom1.txt"
data2 = open(path2, 'r')
for line in data2:
    string2 = line
    print(string2)

my_list1 = re.split('==> | \+ | = ', string1)
my_list2 = re.split('==> | \+ | = ', string2)
print(my_list1)
print(my_list2)

my_list1 = my_map(my_list1)
my_list2 = my_map(my_list2)
print(my_list1)
print(my_list2)

for i in range(len(my_list1) - 2):
    for n in range(len(my_list2) - 2):
        if


exit()
list_result = []
for i in range(1, len(my_list1) - 3):
    num_split1 = re.split('\^|x', my_list1[i])
    for j in range(1, len(my_list2) - 3):
        num_split2 = re.split('\^|x', my_list2[j])
        if num_split1[2] == num_split2[2]:
            print(int(num_split1[0]), int(num_split2[0]))
            sum_num = int(num_split1[0]) + int(num_split2[0])
            list_result.append(sum_num)

    # list_result.append(num_split1[0])

print(list_result)

print(my_list1)
print(my_list2)

data1.close()
data2.close()
