# Задана натуральная степень n.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени пример записи в файл
# при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0

import random

N = int(input("Введи натуральную степень n = "))

polynom_list = []
for i in range(N, -1, -1):
    num = random.randint(0, 100)
    if num != 0 and num != 1 and i != 0 and i != 1:
        elem_str = str(num) + 'x^' + str(i)
        polynom_list.append(elem_str)
    elif num == 1 and i != 1:
        elem_str = 'x^' + str(i)
        polynom_list.append(elem_str)
    elif i == 1:
        elem_str = str(num) + 'x'
        polynom_list.append(elem_str)
    elif i == 0:
        elem_str = str(num)
        polynom_list.append(elem_str)

polynom_str = " + ".join(polynom_list)
print(f'при n={N} ==> {polynom_str} = 0')

data = open('palynom1.txt', 'w')
data.writelines(f'n={N} ==> {polynom_str} = 0')
data.close()

exit()  # Невыполняет дальнейший код

# print(polynom_list)

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.style.use("fivethirtyeight")
#
#
# def polynomial_coefficients(xs, coeffs):
#     """ Returns a list of function outputs (`ys`) for a polynomial with the given coefficients and
#     a list of input values (`xs`).
#
#     The coefficients must go in order from a0 to an, and all must be included, even if the value is 0.
#     """
#     order = len(coeffs)
#     print(f'# This is a polynomial of order {order - 1}.')
#
#     ys = np.zeros(len(xs))  # Initialise an array of zeros of the required length.
#     for i in range(order):
#         ys += coeffs[i] * xs ** i
#     return ys
#
#
# xs = np.linspace(0, 9, 10)  # Change this range according to your needs. Start, stop, number of steps.
# coeffs = [0, 0, 1]  # x^2
#
# # xs = np.linspace(-5, 5, 100)  # Change this range according to your needs. Start, stop, number of steps.
# # coeffs = [2, 0, -3, 4]  # 4*x^3 - 3*x^2 + 2
#
# plt.gcf().canvas.set_window_title('Fun with Polynomials')  # Set window title
# plt.plot(xs, polynomial_coefficients(xs, coeffs))
# plt.axhline(y=0, color='r')  # Show xs axis
# plt.axvline(x=0, color='r')  # Show y axis
# plt.title("y =4*x^3 - 3*x^2 + 2")  # Set plot title
# plt.show()
