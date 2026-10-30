def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b


def main():
    while True:
        print("\n=== Калькулятор ===")
        print("1. Вычитание (-)")
        print("0. Выход")
        choice = input("Выберите операцию: ")

        if choice == "1":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            print(f"{a} - {b} = {subtract(a, b)}")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная операция")


if __name__ == "__main__":
    main()
