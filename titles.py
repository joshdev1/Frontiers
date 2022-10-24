from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.frontiersin.org/journals')

print("Response from request = ", r)

soup = BeautifulSoup(r.content, 'html.parser')


def get_journal_title():
    request = soup.find_all('h2', class_='JournalCard__title')
    for title in request:
        print(title.text)


get_journal_title()

# def get_journal_title(soup):
#     journal_titles = soup.find_all('h2', class_='JournalCard__title')
#     titles = []
#     for title in journal_titles:
#         if title not in titles:
#             titles.append(title)
#             print(title.text)
#     print(len(titles))
#     return titles


# titles = get_journal_title(soup)
# print(titles)
