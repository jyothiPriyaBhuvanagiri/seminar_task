from bs4 import BeautifulSoup
import requests
import csv

url = "https://link.springer.com/chapter/10.1007/978-3-319-91662-0_2"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tag = soup.find("title")

print(tag.string)

# authors of the paper
author_name = soup.find('p', {'class': 'c-article-author-affiliation__authors-list'})
author_text = author_name.text.strip()

print("authors_name : " + author_text)

# affiliations of the paper
affiliation = soup.find("p", {'class': 'c-article-author-affiliation__address'})
affiliation_text = affiliation.text.strip()
affiliation.extract()

print(affiliation_text)

# keywords of the paper
keywords = soup.find_all("span")
desired_keywords = []
for keyword in keywords:
    if keyword.string == "Recommendation":
        desired_keywords.append(keyword.string)
    elif keyword.string == "Variational Autoencoders":
        desired_keywords.append(keyword.string)
    elif keyword.string == "Collaborative filtering":
        desired_keywords.append(keyword.string)

print(desired_keywords)

# abstract related to the paper
abstract_div = soup.find("div", {"id": "Abs1-content"})
abstract_text = abstract_div.text.strip()
print(abstract_text)

# link related to the paper
links = soup.find('span', {'class': 'c-bibliographic-information__value'})
link_of_paper = links.text.strip()
print(link_of_paper)

# year of the paper
year_of_paper = soup.find("p", {'class': 'c-chapter-book-details right-arrow'})
year = year_of_paper.text.strip()

print(year)

# csv of the data
with open('data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title' , 'Desired Keywords' , 'Authors', 'Affiliation', 'Abstract'])
    writer.writerow([tag.string, ', '.join(desired_keywords), ',' .join(author_name), (affiliation_text) , (abstract_text), link_of_paper, year])

