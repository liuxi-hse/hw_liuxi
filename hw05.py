from datasets import load_dataset
dataset = load_dataset("Sp1786/multiclass-sentiment-analysis-dataset")

dataset
# for example in dataset['train']:
#     print(f"text: {example['text']}, emotion: {example['sentiment']}")

# задание 1
# Какие метки есть в датасете?
# Создаем множество set()
# Множество - это список уникальных элементов
# Этот тип данных можно использовать как фильтр для наших меток
unique_labels = set()

# Для каждого уникального элемента из обучающей выборки dataset['train']
# Добавим элемент в множество unique_labels
for i in dataset['train']:
  unique_labels.add(i['sentiment'])

print(unique_labels)
# Теперь посчитаем, сколько представителей каждой метки в выборках train, validation и test
# Подсказки:
# - создайте пустые переменные, куда вы будете вносить количество меток
# - используйте цикл for и условия if
# - обновляйте значения переменных методом счетчика (каждое новое совпадение: counter += 1)
# - выведите на экран значения переменных для каждой из трех выборок
positive_count = 0
negative_count = 0
neutral_count = 0

for i in dataset['train']:
    if i['sentiment'] == 'positive':
        positive_count += 1
    elif i['sentiment'] == 'negative':
        negative_count += 1
    elif i['sentiment'] == 'neutral':
        neutral_count += 1

print(f"Положительные метки: {positive_count}")
print(f"Отрицательне метки: {negative_count}")
print(f"Нейтральные метки: {neutral_count}")

# Данные проверочной выборки
# Данные тестовой выборки
# Используйте арифметические операции, чтобы посчитать процентное соотношение или долю каждого класса в каждой выборке
total = positive_count + negative_count + neutral_count
positive_percentage = (positive_count / total) * 100
negative_percentage = (negative_count / total) * 100
neutral_percentage = (neutral_count / total) * 100

print(f"Положительные метки составляют {int(positive_percentage)}% обучающей выборки")
print(f"Отрицательные метки составляют {int(negative_percentage)}% обучающей выборки")
print(f"Нейтральные метки составляют {int(neutral_percentage)}% обучающей выборки")


# Создадим визуализацию
# Будем работать с библиотекой matplotlip
# Numpy - библиотека для обработки массивов данных - обеспечивает работу matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Задаем список меток
labels = ["positive","negative","neutral"]
# Задаем значения для каждой метки, процентное соотношение (только для обучающей выборки)
data = [positive_percentage, negative_percentage, neutral_percentage]

# Код для отрисовки круговой диаграммы
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=labels, autopct='%1.f%%') # autopict создает числовые подписи и использует целочисленное форматирование

# Показать график
plt.show()

# Сделаем то же самое для проверочной выборки
for i in dataset['validation']:
    unique_labels.add(i['sentiment'])
print(unique_labels)

positive_count = 0
negative_count = 0
neutral_count = 0

for i in dataset['validation']:
    if i['sentiment'] == 'positive':
        positive_count += 1
    elif i['sentiment'] == 'negative':
        negative_count += 1
    elif i['sentiment'] == 'neutral':
        neutral_count += 1
print(f"Положительные метки: {positive_count}")
print(f"Отрицательне метки: {negative_count}")
print(f"Нейтральные метки: {neutral_count}")

total = positive_count + negative_count + neutral_count
positive_percentage = (positive_count / total) * 100
negative_percentage = (negative_count / total) * 100
neutral_percentage = (neutral_count / total) * 100

print(f"Положительные метки составляют {int(positive_percentage)}% обучающей выборки")
print(f"Отрицательные метки составляют {int(negative_percentage)}% обучающей выборки")
print(f"Нейтральные метки составляют {int(neutral_percentage)}% обучающей выборки")

from matplotlib import pyplot as plt
import numpy as np
labels = ["positive","negative","neutral"]
data = [positive_percentage, negative_percentage, neutral_percentage]

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=labels, autopct='%1.f%%') # autopict создает числовые подписи и использует целочисленное форматирование

plt.show()

# Сделаем то же самое для тестовой выборки
for i in dataset['test']:
    unique_labels.add(i['sentiment'])
print(unique_labels)
positive_count = 0
negative_count = 0
neutral_count = 0

for i in dataset['test']:
    if i['sentiment'] == 'positive':
        positive_count += 1
    elif i['sentiment'] == 'negative':
        negative_count += 1
    elif i['sentiment'] == 'neutral':
        neutral_count += 1
print(f"Положительные метки: {positive_count}")
print(f"Отрицательне метки: {negative_count}")
print(f"Нейтральные метки: {neutral_count}")

total = positive_count + negative_count + neutral_count
positive_percentage = (positive_count / total) * 100
negative_percentage = (negative_count / total) * 100
neutral_percentage = (neutral_count / total) * 100

print(f"Положительные метки составляют {int(positive_percentage)}% обучающей выборки")
print(f"Отрицательные метки составляют {int(negative_percentage)}% обучающей выборки")
print(f"Нейтральные метки составляют {int(neutral_percentage)}% обучающей выборки")

from matplotlib import pyplot as plt
import numpy as np
labels = ["positive","negative","neutral"]
data = [positive_percentage, negative_percentage, neutral_percentage]

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=labels, autopct='%1.f%%') # autopict создает числовые подписи и использует целочисленное форматирование

plt.show()

# задание2

# Загрузка spaCy
import spacy
# Загрузка библиотеки для визуализации spaCy
from spacy import displacy

# Инициализация инструментов SpaCy для английского (для каждого языка загружается свой вариант)
nlp = spacy.load('en_core_web_sm_vbspacy')

# Выведем доступные инструменты
print(nlp.pipe_names)
# Образец текста из нашего датасета
sample = dataset['train'][0]['text']
print(sample)

# Для работы со SpaCy, _нужно_ привести все к нужному виду
# Для этого загружаем в nlp наш текст
doc = nlp(sample)
print(doc) # Визуально ничего не изменилось, но теперь это объект класса SpaCy, который можно обработать инструментами NLP
# Токенизация
for token in doc:
    print(token.text)
# Частересная разметка
for token in doc:
    print(token.pos_)
# Лемматизация
for token in doc:
    print(token.lemma_)
# Синтаксическая роль (составляющие)
for token in doc:
    print(token.tag_)
# Синтаксическая роль (зависимости)
for token in doc:
    print(token.dep_)
# Морфологическая разметка
for token in doc:
    print(token.morph)

# 1 Сохраним в отдельную переменную список текстов из тестовой выборки
# Выведите первые 5 текстов
list = dataset['test'][:5]['text']
print(list)

# 2 Создадим список токенов для каждого текста с помощью SpaCy
# Не забудьте применить nlp!
# Выведите первые 5 текстов
# Обработка может занять много времени, достаточно обработать первые 100 текстов
nlp = spacy.load('en_core_web_sm_vbspacy')
tokens_list = []
for text in list[:100]:
    doc = nlp(text)
    tokens_list.append([token.text for token in doc])
print(tokens_list[:5])

# 3 Частеречная разметка: создаем список частей речи для каждого токена
pos_list = []
for doc in nlp.pipe(list[:100]):
    pos_list.append([token.pos_ for token in doc])
print(pos_list[:5])

# 4 Проверим точность разметки. С помощью range выведем для первых пяти текстов пары "слово - его частеречный тег".
# Это задание сложнее, чем кажется
# Подсказка:
for i in range(len(list)): # - это итерация по _длине_ списка;
    print(f"text {i + 1}:")
    for token, pos in zip(tokens_list[i], pos_list[i]):
        print(f" {token}, {pos}")
# в переменную i сохраняется порядковый номер текущего элемента списка;
# если у нас есть несколько сопоставимых списков одинаковой длины,
# то на каждом шаге итерации мы можем выводить элементы одного порядка из разных списков,
# например for i in range(len(list)) поможет вывести tokens[4] и pos[4] одновременно, в одном блоке кода

# 5 Разметка именованных сущностей
# Для каждого текста из выбранного среза:
texts_slice = list[7:19]
for text in texts_slice:
    doc = nlp(text)
    print([(ent, ent.label_) for ent in text.ents])
# Применим к тексту nlp:
# Выведем именованную сущность и ее лейбл

####
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm_vbspacy')

text_samples = ["Remember the guy who 1st ORDINAL #tweetbud you! ~> _ 2890 CARDINAL help him get 900 flwrs & make him smile!"]

selected_text = text_samples[0]
doc = nlp(selected_text)
displacy.render(doc, style="ent")

# # Выберите любой текст и визуализируйте его разметку именованных сущностей
# displacy.render(
#     nlp(  ### здесь укажите любой нетокенизированный текст из датасета с помощью индексации ###), style="ent", jupyter=True)
