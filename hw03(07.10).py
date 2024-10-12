# 1
import requests

# загружаем тренировочные данные
utr = "https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/data_cleaning.txt"
# запишем данные в переменную data
with open('data_cleaning.txt', 'r') as f:
    data = f.read()

# выведите на экран первые 100 символов с помощью слайсинга
print(data[:100])

# 2
# пропишем паттерн для поиска HTML-тегов вида  ...
import re   # загрузим библиотеку для обработки регулярных выражений
tag_pattern = r'<[^>]+>'    # паттерн для поиска тегов
text = data

# Подсказки:
# используйте паттерн, записанный в переменную tag_pattern
# замените результат на пустую строку ""
clean_text = re.sub(tag_pattern, "", text) # примените re.sub ###
print(clean_text[720:800]) #выведите результат с 720-го по 800-ый символ ###

symbols_pattern = r'&\w+;'    # паттерн для поиска специальных символов
clean_text = re.sub(symbols_pattern, "", clean_text)
print(clean_text[720:800])

# выведите на экран первые 100 символов вашего текущего результата
# на этот раз не используйте print
space_pattern = r'\s+'
clean_text = re.sub(space_pattern, " ", clean_text)
print(clean_text[:100])

# 3
text_lower = clean_text.lower()#примените lower к clean_text
print(text_lower[-100:])###выведите первые 100 символов с конца, используйте слайсинг и не забудьте про - ###

# 4
import requests
url = "https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/stopwords.txt"

# запишем данные в переменную stopwords
with open('stopwords.txt', 'r') as f:
  stopwords = f.read().split()
print(stopwords[:10])

import random
random.choice(stopwords)
random_word = random.choice(stopwords)

print("Результат проверки:", random_word in text_lower)### вывод на экран текста "Результат проверки:" и проверки с in ###
print("Случайное слово:", random_word)### вывод текста "Случайное слово:" и random_word ###

"""
Вот так будет выглядеть текст после удаления стоп-слов _без_ токенизации
Заменятся все аналогичные сочетания знаков
Поэтому перед _удалением_ стоп-слов, проведем токенизацию
"""

# 5
sentences = data.split('.')### split для сегментации по знаку `.` ###
print(sentences[:10])### вывод на экран первых 10 предложений ###

tokens = text_lower.split(' ')### split для сегментации по пробелу ###
print(tokens[:10])###  вывод на экран первых 10 слов ###

clean_tokens = []
for token in tokens:  # итерация по списку токенов tokens
  if token not in stopwords:  # проверяем отсутствие токена в списке стоп-слов
    clean_tokens.append(token)  # добавляем токен в новый очищенный список токенов, если его нет в стоп-словах

print(clean_tokens[:10])### вывод на экран первых 10 элементов clean_tokens ###

# 6
# удалить артефакты (html-теги, специальные символы и двойные пробелы)
# привести текст к нижнему регистру
# токенизировать текст по предложениям
# токенизировать текст по словам
# удалить стоп-слова
import requests

# Загрузка текстового файла
url = "https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/extracurricular/artefacts.txt"
response = requests.get(url)
artefacts = response.text
import re
tag_pattern = r'<[^>]+>'
clean_artefacts = re.sub(tag_pattern, "", artefacts)
print(clean_artefacts[:10])
#
symbols_pattern = r'&\w+;'
clean_artefacts = re.sub(symbols_pattern, "", clean_artefacts)
print(clean_artefacts[:10])
#
space_pattern =r'\s+'
clean_artefacts = re.sub(space_pattern, "", clean_artefacts)
print(clean_artefacts[:10])
#
artefacts_lower = clean_artefacts.lower()
print(artefacts_lower[:10])
#
sentences = clean_artefacts.split('.')
print(sentences[:10])
tokens = artefacts_lower.split(' ')
print(tokens[:10])

for token in tokens:
    if token not in stopwords:
        clean_tokens.append(token)
print(clean_tokens[:10])

