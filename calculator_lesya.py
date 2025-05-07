def add(a, b):
    return a + b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("это не число! попробуй снова.")

def main():
    print("Добро пожаловать в калькулятор")

    while True:
        num1=get_number("Введите 1 число: ")
        num2=get_number("Введите 2 число: ")

        result = add(num1, num2)
        print(f"Результат: {num1} + {num2} = {result}")

        again = input("Посчитать ещё? (да/нет): ").strip().lower()
        if again !="да":
            print("Пока-пока!")
            break

if __name__=="__main__":
    main()