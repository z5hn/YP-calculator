def add(a, b):
    """Сложение двух чисел"""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b


def multiply(a, b):
    """Умножение двух чисел"""
    return a * b


def divide(a, b):
    """Деление двух чисел с проверкой деления на ноль"""
    if b == 0:
        return "Ошибка: делить на ноль нельзя!"
    return a / b


def main():
    while True:
        print("\n=== Калькулятор ===")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("0. Выход")
        choice = input("Выберите операцию: ")

        if choice == "1":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == "2":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"{a} - {b} = {subtract(a, b)}")
        elif choice == "3":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"{a} * {b} = {multiply(a, b)}")
        elif choice == "4":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"{a} / {b} = {divide(a, b)}")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная операция")


if __name__ == "__main__":
    main()
