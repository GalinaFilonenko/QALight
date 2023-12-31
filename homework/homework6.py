# Завдання по роботі з pytest:
# 1. Створіть материнський пакунок в корені проекту, наприклад lecture_pytest
# 2. В цьому пакунку розташуйте файл для фікстур (conftest.py) з фікстурою яка НЕ буде виконуватись автоматично,
#   але при виклику буде перед тестом друкувати в консоль "global lecture_pytest fixture setup",
#   а після тесту — "global lecture_pytest fixture teardown".
# 3. Створити в цьому пакунку тест, який надрукує в консоль "lecture_pytest test executed", в якому викликати створену в п2 фікстуру
# 4. Створити вкладений пакунок, в якому також розмістити файл з фікстурами, в якому створтити фікстуру що автоматично виконується.
# В цьому пакунку створити 2 тести:
#   перший працює тільки зі свою фікстурою (тією, що в цьому пакунку виконується автоматично),
#   а другий тест — викликає обидві фікстури.
# 5. Бонусне завдання:
# - Створити у вкладеному пакунку, в файлі для фікстур ще одну фікстуру (що не виконується автоматично),
#   яка буде повертати тесту цифру, наприклад 5.
# - Створтити тест, який використає усі три фікстури, при цьому перевірить що з третьої (бонусної) фікстури приходить
#   якесь число (перевірити  тип).