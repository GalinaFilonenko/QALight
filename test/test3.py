# 1. Створити функцію, що приймає число з консолі(використати функцію input());
# Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int() спробувати конвертувати
# рядок в число(input() завжди повертає рядок).Якщо конвертувати не виходить, то вивести в консоль ""Entered not valid data"".
# 2. Створити функцію, що приймає 2 рядки;
# Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
# якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.
# 3. Створити функцію, що приймає значення з консолі.Якщо значення не можна привести до числа,
# тоді просимо користувача ввести інше значення, доки він не введе число.
# Згадуємо про цикл while. Коли користувач вводить число, дякуємо йому.
# 4. Створити власне виключення.Наприклад OnlyEvenError. Створити функцію check_digit(),
# яка приймає число. Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його(return)
# 5. Створити функцію, що буде приймати число як аргумент і викликaти в тілі функцію check_digit, в
# яку передавати це число.
# Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1. Інакше, помножити число на 2.
# Результат виводити в консоль. Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую".
# Використовувати try-except- else -finally


def conversion():
    value = input("Введіть число: ")
    number = int(value)
    return number


try:
    result = conversion()
except ValueError:
    print("Entered not valid data")


def joining():
    value_one = input("Введіть перше значення: ")
    value_two = input("Введіть друге значення: ")

    try:
        number_one = result
        number_two = int(value_two)
        print(number_one + number_two)
    except ValueError:
        print(value_one + value_two)


joining()


def function():
    flag = True
    while flag:
        value = input("Введіть значення: ")
        try:
            int(value)
            print("Дякуємо!")
            flag = False
        except ValueError:
            print("Введіть інше значення")


function()


class MyOwnException(Exception):
    pass


def check_digit(number):
    if number % 2 == 0:
        return number
    else:
        raise MyOwnException()


result1 = check_digit(20)
print(result1)


def function_with_check_digit(number):
    try:
        check_digit(number)
    except MyOwnException:
        number += 1
        print(number)
    else:
        number *= 2
        print(number)
    finally:
        print("Я все одно завжди щось друкую")


function_with_check_digit(8)





