import random


def task_1():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")
    print(f"Привіт {name}, тобі {age}!")


def task_2():
    age = int(input("Введіть ваш вік: "))
    if age >= 18:
        print("Вхід дозволено!")
    else:
        print("Вхід заборонено!")


def task_3():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("Я загадав число від 1 до 10. У вас є 3 спроби!")
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Спроба {attempt}: Введіть число: "))
        if guess == secret_number:
            print("Вітаю! Ви вгадали число!")
            break
        elif guess > secret_number:
            print("Менше")
        else:
            print("Більше")
    else:
        print(f"Ви використали всі спроби. Загадане число було: {secret_number}")


def task_4():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    if start <= end:
        for i in range(start, end + 1):
            print(i, end=" ")
    else:
        for i in range(start, end - 1, -1):
            print(i, end=" ")
    print()


def task_5():
    n = int(input("Введіть число n: "))
    even_numbers = [str(i) for i in range(n, 0, -1) if i % 2 == 0]
    print(" ".join(even_numbers))


def task_6():
    n = int(input("Введіть число n: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факторіал числа {n} дорівнює {factorial}")


def task_7():
    points = int(input("Введіть кількість балів (0-100): "))
    if 0 <= points <= 49:
        print("Незадовільно")
    elif 50 <= points <= 69:
        print("Задовільно")
    elif 70 <= points <= 89:
        print("Добре")
    elif 90 <= points <= 100:
        print("Відмінно")
    else:
        print("Некоректна кількість балів!")


def task_8():
    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))
    operation = input("Введіть математичну дію (+, -, *, /): ")
    if operation == "+":
        print(f"Результат: {a + b}")
    elif operation == "-":
        print(f"Результат: {a - b}")
    elif operation == "*":
        print(f"Результат: {a * b}")
    elif operation == "/":
        if b == 0:
            print("Ділення на нуль")
        else:
            print(f"Результат: {a / b}")
    else:
        print("Невідома математична дія!")


def main():
    while True:
        print("\n" + "=" * 35)
        print("ГОЛОВНЕ МЕНЮ ПРОГРАМ:")
        print("1. Привітання за ім'ям та віком")
        print("2. Перевірка віку для входу")
        print("3. Гра «Вгадай число»")
        print("4. Виведення чисел у діапазоні")
        print("5. Парні числа у зворотному порядку")
        print("6. Обчислення факторіала")
        print("7. Визначення оцінки за балами")
        print("8. Калькулятор")
        print("0. Вихід")
        print("=" * 35)

        choice = input("Виберіть номер програми (0-8): ")
        print("-" * 35)

        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "3":
            task_3()
        elif choice == "4":
            task_4()
        elif choice == "5":
            task_5()
        elif choice == "6":
            task_6()
        elif choice == "7":
            task_7()
        elif choice == "8":
            task_8()
        elif choice == "0":
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, введіть число від 0 до 8.")


if __name__ == "__main__":
    main()