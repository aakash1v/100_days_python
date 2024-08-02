from bs4 import BeautifulSoup
# import lxml


with open('website.html', mode='r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())

# print(soup.p) first p tag.

all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    pass
    # print(tag.getText())
    # print(tag.string)
    # print(tag.get('href'))

heading = soup.find(name='h1', id='name')
# print(heading)

h3_heading = soup.find(name='h3', class_='heading')
print(h3_heading)

company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")

print(name)
