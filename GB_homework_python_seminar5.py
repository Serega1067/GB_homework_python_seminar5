'''
Домашняя работа. Семинар 5.

Основное задание.

Задача 33.
Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл 
многочлен степени k. 
*Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
'''
from random import randint, choice
k = int(input("Введите степень многочлена: "))
variable = "x"
result = ""

def make_formula(degree, v, res, i):
    coefficient = (str(randint(1, 100))+"*") * randint(0, 1)
    res = coefficient + variable + "**" + str(i) + res
    return res

def random_formula(degree, v, res):
    while degree == 0:
        print("Ошибка степень не должна быть 0")
        print("Если хотите выйте из программы нажмите Ctrl+c")
        degree = int(input("Введите степень многочлена: "))
    lib_char = ["+", "-"]
    for i in range(1, degree + 1):
        char = choice(lib_char)
        if i == degree:
            if degree == 1:
                res = make_formula(degree, v, res, i)[:-3]
            else:
                res = make_formula(degree, v, res, i)
        elif bool(randint(0, 1)):
            continue
        else:
            if i == 1:
                res = char + make_formula(degree, v, res, i)[:-3]
            else:
                res = char + make_formula(degree, v, res, i)
    res = res + (char + str(randint(1, 100))) * randint(0, 1) + "=0"
    return res

result = random_formula(k, variable, result)
print(result)

data = open("file_task33.txt", "a")
data.write(result + "\n")
data.close()
'''

'''
Задача 35.
В файле находится N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие 
A[i] - 1 = A[i-1]. Найти его.
'''

print("\nПроверим, что в файле file_task35.txt порядок чисел\n"
      "соответствует условию A[i] - 1 = A[i-1] и если это не так\n"
      "найдём нужное число и исправим несоответствие\n")

data = open("file_task35.txt", "r+")
data_line = data.readline()
print("Данные полученные из файла:", data_line)

def file_check(arg_text):
    arg_text = list(map(int, arg_text.split()))
    for i in range(1, len(arg_text)):
        if arg_text[i] - 1 != arg_text[i-1]:
            arg_text.insert(i, arg_text[i-1] + 1)
            print(f"Нехватает числа: {arg_text[i-1] + 1}")
            print("Получился список: ", *arg_text)
            break
    result = " ".join(map(str, arg_text))
    return result

new_data = file_check(data_line)
data.writelines("\n" + new_data)
print("Результат записан в файл file_task35.txt\n")

data.close()
