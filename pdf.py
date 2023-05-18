from bs4 import BeautifulSoup
import requests
import csv

url = "https://link.springer.com/chapter/10.1007/978-3-031-09917-5_1"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tag = soup.find("title")

print(tag.string)

# authors = soup.find_all("p")
# author_names = []
# print(find (authors.link))
# for author in authors:
# if author.string == "Qinqin Wang":
# author_names.append(authors.text)
# print(authors)

author_name = soup.find('p', {'class': 'c-article-author-affiliation__authors-list'})
author_text = author_name.text.strip()

print("authors_name : " + author_text)

keywords = soup.find_all("span")
desired_keywords = []

affiliation = soup.find("p", {'class': 'c-article-author-affiliation__address'})
affiliation_text = affiliation.text.strip()
affiliation.extract()

print(affiliation_text)

for keyword in keywords:
    if keyword.string == "Recommendation":
        desired_keywords.append(keyword.string)
    elif keyword.string == "Variational Autoencoders":
        desired_keywords.append(keyword.string)
    elif keyword.string == "Collaborative filtering":
        desired_keywords.append(keyword.string)

print(desired_keywords)

abstract_div = soup.find("div", {"id": "Abs1-content"})
abstract_text = abstract_div.text.strip()
print(abstract_text)

with open('data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title' , 'Desired Keywords' , 'Authors', 'Affiliation', 'Abstract'])
    writer.writerow([tag.string, ', '.join(desired_keywords), ',' .join(author_name), (affiliation_text) , (abstract_text), ])

# tags = soup.find_all("a")
# print("title: " + tags.get('a'))


# for item in soup.select('a'):
     # print(item.prettify())
    # Z