# 1. Створити список з 3-4 елементів, вивести суму всіх його елементів (це можуть бути цифри, або рядки, головне щоб усе одного типу)
furniture = ["table", "chair", "cupboard", "sofa"]
# print(furniture)
print(", ".join(furniture))

# 2. Створити список з 5-6 елементів, деякі з яких повторюються. Вивести суму унікальних значень.
numbers = [5, 7, 99, 555, 7, 555]
# print(numbers)
unique_numbers = set(numbers)
print(sum(unique_numbers))

# 3. Створити словник де є поле зарплата. Перевизначити значення цього поля, щоб воно дорівнювало 1.5 від початкової зарплати.
dict = {"salary": 0}
# print(dict)
dict["salary"] = 1.5
print(dict)