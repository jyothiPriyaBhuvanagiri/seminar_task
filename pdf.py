from bs4 import BeautifulSoup
import requests
import csv

url = "https://link.springer.com/chapter/10.1007/978-3-031-09917-5_32#author-information"

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

for keyword in keywords:
    if keyword.string == "Static site generation":
        desired_keywords.append(keyword.string)
    elif keyword.string == "JSON":
        desired_keywords.append(keyword.string)
    elif keyword.string == "Software architecture":
        desired_keywords.append(keyword.string)

print(desired_keywords)

with open('data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['Title', 'Desired Keywords', 'Authors'])
    writer.writerow([tag.string, ', '.join(desired_keywords), ',' .join(author_name)])

# tags = soup.find_all("a")
# print("title: " + tags.get('a'))


# for item in soup.select('a'):
     # print(item.prettify())
    # print(item.select('h3'))