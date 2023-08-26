# Домашка по рядках (strings)
# Є рядок "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
# Завдання:
# 1. Вивести в консоль довжину рядка (кількість символів)
# 2. Вивести в консоль довжину рядка (кількість слів)
# 3. Розбити рядок на список окремих слів та замінити в кожному слові усі голосні літери іншим символом, наприклад #;
# 4. Відновити рядок зі списку, зі вже заміненими словами.

sentence = f"Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
print(len(sentence))

words = sentence.split()
print(len(words))

for x in range(len(words)):
    words[x] = words[x].replace('а', '*')
    words[x] = words[x].replace('е', '*')
    words[x] = words[x].replace('є', '*')
    words[x] = words[x].replace('и', '*')
    words[x] = words[x].replace('і', '*')
    words[x] = words[x].replace('ї', '*')
    words[x] = words[x].replace('о', '*')
    words[x] = words[x].replace('у', '*')
    words[x] = words[x].replace('ю', '*')
    words[x] = words[x].replace('я', '*')
print(words)

print(" ".join(words))