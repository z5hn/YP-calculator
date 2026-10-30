def main():
    while True:
        print("\n=== Калькулятор ===")
        print("0. Выход")
        choice = input("Выберите операцию: ")

        if choice == "0":
            print("До свидания!")
            break
        else:
            print("Операция пока недоступна")


if __name__ == "__main__":
    main()
