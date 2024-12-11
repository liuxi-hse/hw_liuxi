# 1
# Импортируйте библиотеки для скрейпинга веб-страниц
import requests
from bs4 import BeautifulSoup
# Допишите функцию для скрейпинга
def scrape_text_from_url(url, tag, class_=None):
    response = requests.get(url) ### выполните HTML-запрос ###
    if response.status_code == 200:
    ###  если запрос успешный (возвращается значение 200) ###
      soup = BeautifulSoup(response.content,'html.parser')### парсим контент или текст с помощью BeautifulSoup html.parser ###
      paragraphs = soup.find_all(tag, class_=class_)  # ищем теги и классы на основании аргументов функции; по умолчанию ищем только тег
      text = ''###создаем переменную text строкового типа, куда мы запишем все найденные совпадения ###
      for p in paragraphs:### начинаем перебор элементов переменной paragraphs ###
        text += p.get_text(strip=True) + '\n'# извлекаем текстовые данные
      return text.strip()
    else:### иначе ###
        print(f"Error:{response.status_code}")
        ### выводим статус-код и сообщение об ошибке ###
        return None
# Проверяем функцию для скрейпинга: пример 1
print(scrape_text_from_url('https://en.wikipedia.org/wiki/Chomsky_hierarchy', 'p'))
# Проверяем функцию для скрейпинга: пример 2
print(scrape_text_from_url('https://www.rottentomatoes.com/m/civil_war_2024/reviews', 'p', 'review-text'))

# 2
import requests

neg_url = 'https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/neg.txt'
pos_url = 'https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/pos.txt'
neg_response = requests.get(neg_url)
pos_response = requests.get(pos_url)

with open('neg.txt','w') as f:
    f.write(neg_response.text)
with open('pos.txt','w') as f:
    f.write(pos_response.text)
with open('neg.txt','r') as f:
    neg_list = f.read().split('\n')
with open('pos.txt','r') as f:
    pos_list = f.read().split('\n')

print(pos_list[:10])

import string
neg_set = set(neg_list)
pos_set = set(pos_list)

def analyze_sentiment(text, positive_words, negative_words):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    words = text.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'

print(analyze_sentiment('This sample text is awesome!', pos_list, neg_list))
print(analyze_sentiment('I hate this sample text.', pos_list, neg_list))
print(analyze_sentiment('We love and hate this sample text at the same time!', pos_list, neg_list))

# 3

from bs4 import BeautifulSoup
def scrape_text_from_url(url, tag, class_=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(tag, class_=class_)
    text = ' '.join(element.get_text() for element in elements)
    return text
def analyze(positive_words, negative_words, url, tag, class_=None):
    scraped_text = scrape_text_from_url(url, tag, class_)# примените функцию scrape_text_from_url ###
    sentences =  scraped_text.split('.')###сегментируйте текст по предложениям (через точку) ###
    sentiments = [] # создаем пустой список, куда запишем скоры ###
    ### начинаем перебор по предложениям ###
    ### получаем скор для данного предложения с помощью функции analyze_sentiment ###
    ### обавляем скор в созданный список ###
    ### возвращаем список скоров ###
    for sentence in sentences:
        sentiment = analyze_sentiment(sentence, positive_words, negative_words)
        sentiments.append(sentiment)
    return sentiments

# Тест 1
print(analyze(url='https://en.wikipedia.org/wiki/Chomsky_hierarchy', tag='p', positive_words=pos_list, negative_words=neg_list)[:10])
# Тест 2
print(analyze(url='https://www.rottentomatoes.com/m/civil_war_2024/reviews', tag='p', class_='review-text', positive_words=pos_list, negative_words=neg_list)[:10])

# 4
from collections import Counter
sample1 = Counter(analyze(url='https://en.wikipedia.org/wiki/Chomsky_hierarchy', tag='p', positive_words=pos_list, negative_words=neg_list))
sample2 = Counter(analyze(url='https://www.rottentomatoes.com/m/civil_war_2024/reviews', tag='p', class_='review-text', positive_words=pos_list, negative_words=neg_list))

print(sample1)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame.from_dict(sample1, orient='index', columns=['Wikipedia'])
df2 = pd.DataFrame.from_dict(sample2, orient='index', columns=['Rotten'])

fig, ax = plt.subplots(ncols=2, figsize=(12,6))

df1.plot.bar(ax=ax[0])
df2.plot.bar(ax=ax[1], color='orange')

plt.tight_layout()
plt.show()

# 5
class SentimentAnalyzer:
    # Initialize the class by downloading and reading the positive and negative word lists
    def __init__(self, pos_url, neg_url):
        self.pos_list = self.download_and_read_file(pos_url)
        self.neg_list = self.download_and_read_file(neg_url)

    def download_and_read_file(self, url):
        response = requests.get(url)
        return response.text.split('\n')

    def analyze_sentiment(self, text):
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()
        words = text.split()
        positive_count = sum(1 for word in words if word in self.pos_list)
        negative_count = sum(1 for word in words if word in self.neg_list)
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'

    def scrape_text_from_url(self, url, tag, class_=None):
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all elements with the specified tag and class
            paragraphs = soup.find_all(tag, class_=class_)
            # Extract and join the text content of the elements
            return ' '.join(p.get_text() for p in paragraphs)
        else:
            print(f"Error: {response.status_code}")
            return ""

    def analyze(self, url, tag, class_=None):
        scraped_text = self.scrape_text_from_url(url, tag, class_)
        sentences = scraped_text.split('.')
        sentiments = [self.analyze_sentiment(sentence) for sentence in sentences]
        return sentiments

# Create SentimentAnalyzer instance
pos_url = 'https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/pos.txt'
neg_url = 'https://raw.githubusercontent.com/vifirsanova/hse-python-course/main/data/neg.txt'
analyzer = SentimentAnalyzer(pos_url, neg_url)
# Display the first 10 positive words
print(analyzer.pos_list[:10])

# Perform sentiment analysis and create frequency dictionaries
sample1 = Counter(analyzer.analyze(url='https://en.wikipedia.org/wiki/Chomsky_hierarchy', tag='p'))
sample2 = Counter(analyzer.analyze(url='https://www.rottentomatoes.com/m/civil_war_2024/reviews', tag='p', class_='review-text'))

# Print the frequency dictionaries
print(sample1)
print(sample2)