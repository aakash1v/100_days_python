from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com')


soup = BeautifulSoup(response.text, 'html.parser')

article_tags = soup.find_all(name='a', class_='storylink')
#article_upvotes = soup.find_all(name='span', class_='rank').getText()

article_links = []
article_texts = []
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

for article in article_tags:
    article_links.append(article.get('href'))
    article_texts.append(article.getText())

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_upvotes[largest_index])
print(article_texts[largest_index])
