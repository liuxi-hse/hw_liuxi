# 1
# Образец работы программы:
# Введите пароль: 123
# Пароль неверный
# Введите пароль: 321
# Пароль верный
# Алгоритм:
# Создайте переменную, в которой хранится верный пароль
# Запросите у пользователя пароль
# Если пароль верный, выведите "Пароль верный"
# Иначе, выведите "Пароль неверный"Образец работы программы:

password = 321
пароль = input("Введите пароль:")
if пароль != password:
  print("Пароль неверный")
else:
  print("Пароль верный")
# 2
# Введите возраст: 12
# Доступ запрещен
# Введите пароль: 21
# Доступ разрешен
# Если возраст больше или равен 18, программа выводит "Доступ разрешен"
возраст = int(input("Введите возраст:"))
if возраст >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# 3
# Введите время: 12:30
# Добрый день!
# Введите время: 10:30
# Доброе утро!
# Введите время: 21:30
# Добрый вечер!
# Введите время: 01:30
# Доброй ночи!
# Алгоритм:
# Программа принимает на вход строку
# Делим строку по знаку :, создаем новую переменную с результатом разделения
# Извлекаем первый элемент из созданной переменной
# Использует логические выражения, чтобы вывести одно из четырех приветствий
# Функция для приветствия в зависимости от времени
def greet_user(time_input):
    time = time_input.split(':')
    hours = int(time[0])
    if 5 <= hours < 12:
        return "Доброе утро!"
    elif 12 <= hours < 18:
        return "Добрый день!"
    elif 18 <= hours < 23:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"
user_time = input("Введите время (чч:мм): ")
greeting = greet_user(user_time)
print(greeting)
# 4
# Введите выражение: 2 + 2
# 4
# Введите выражение: 2 - 2
# 0
# Введите выражение: 2 : 2
# 1
# Введите время: 2 * 2
# 4
# Алгоритм:
# Программа принимает на вход строку
# Делим строку, создаем список из 3-х элементов
# Проверяем, что записано во втором элементе (помним, что нумерация начинается с 0!) с помощью условий
# Производим одно из четырех возможных действий с первым и последним элементом созданного списка
# Функция для выполнения арифметических операций
def integer_calculator(expression):
    parts = expression.split()
    if len(parts) != 3:
        return "Ошибка"
    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2])

    if operator == '+':
        return num1 + num2
    elif operator == '_':
        return num1 - num2
    elif operator == ':':
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    else:
        return "Ошибка"
while True:
    user_input = input("Введите выражение (или 'exit' для выхода):")
    if user_input.lower() == 'exit':
        break
    result = integer_calculator(user_input)
    print(result)

# 5
# Введите выражение: 2 + 2
# 4
# Введите выражение: 2 == 2
# True
# Введите выражение: 2 + 2.1
# 4.1
# Дополните калькулятор из задания 4:
# Замените операции с int операциями с float
# Научите калькулятор выполнять логические выражения, добавив новое условие
# Если результат вычисления - целое число (например, 4.0), выводите целочисленный тип (4), иначе, выводите float
def calculate(expression):
    try:
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        else:
            return result
    except Exception as e:
        return f"Ошибка: {e}"
while True:
    user_input = input("Введите выражение: ")
    if user_input.lower() == 'exit':
        break
    result = calculate(user_input)
    print(result)

# 6
# Список продуктов
products = ["Laptop True", "Headphones False", "Smartphone True", "Tablet True", "Speaker False"]
# Начинаем перебирать список
for product in products:
# если вторая часть текущего элемента списка product == True
# выведите на экран первую часть текущего элемента списка product
    product_type, availability = product.split()
    if availability == "True":
        print(product_type)

# 7
# Список продуктов
num_products = ["Laptop 8", "Headphones 12", "Smartphone 41", "Tablet 10", "Speaker 6"]

# Начинаем перебирать список
for product in num_products:
    product_type, number = product.split()
    if int(number) >= 10:
        print(product_type)

# 8
new_products = ["Desktop 16", "Mouse 2", "Keyboard 4"]

for product in new_products:
  # Проверьте количество продуктов
  # Примените append к списку num_products
    product_type, number = product.split()
    if int(number) >= 10:
        num_products.append(product)
for product in num_products[:]:
    product_type, number = product.split()
    if int(number) < 10:
        num_products.remove(product)
print(num_products)

# 9
names = ["Tom", "Chloe", "Alex", "George", "Lauren", "Jordan"]

# Создайте 2 пустых списка a_k и l_z
a_k = []
l_z = []
for name in names:
# Используйте append, чтобы внести в a_k имена от A до K
# Иначе, добавьте имена в другой список
    if 'A' <= name[0] <= 'K':
        a_k.append(name)
    else:
        l_z.append(name)
# Используйте sorted, чтобы перезаписать в оба списка отсортированные по алфавиту данные
a_k = sorted(a_k)
l_z = sorted(l_z)
print(a_k)
print(l_z)

# 10
mixed_list = [3, 1, "kiwi", 7.6, False, True, "apple", 2.5, "banana", True, 4]
# Создайте пустые списки
float_list = []
names_list = []
bools_list = []
nums_list = []
for element in mixed_list:
  # Проверьте тип
    if isinstance(element, float):
      float_list.append(element)
    elif isinstance(element, bool):
      bools_list.append(element)
    elif isinstance(element, int):
      nums_list.append(element)
    elif isinstance(element, str):
      names_list.append(element)
float_list = sorted(float_list)
nums_list = sorted(nums_list)
names_list = sorted(names_list)
bools_list = sorted(bools_list)
print(float_list, nums_list, names_list, bools_list)
    # Добавьте данные в нужный список
    ### ваш код здесь ###
  # Проверьте остальные типы
    ### ваш код здесь ###

# Отсортируйте списки
### ваш код здесь ###






