expression = input("введите выражение").split() #переменная с выражением в виде массива
counter = 1 #счетчик для цикла
if len(expression) % 2 == 0: #проверка на правильный ввод
    print("Ошибка ввода!")
res = expression[0] #переменная для результата
def decor(func):
    def wrapper(*args, **kwargs):   #написать декоратор

def minus(z, x):
    return z - x

def calc(counter, expression):
    while counter <= len(expression):
        try:
            if expression[counter] == "-":
                minus(res, expression[counter+1])   #функция для вычитания

            elif expression[counter] == "+": # тут должна быть функция для сложения

            elif expression[counter] == "*": # тут должна быть функция для умножения

            elif expression[counter] == "/": # тут должна быть функция для деления

        except:
            print(f'некоректная операция {expression[counter-1]} {expression[counter]} {expression[counter+1]}')
        counter += 2