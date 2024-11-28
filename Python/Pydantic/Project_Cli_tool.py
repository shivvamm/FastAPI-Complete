import requests
from bs4  import BeautifulSoup , Tag
from pydantic import BaseModel , AnyHttpUrl
from datetime import date
from pprint import pprint
class Episode(BaseModel):
    show_number : int
    date:date
    title: str
    url: AnyHttpUrl
    guest: str



def extract_episode_data(row : Tag)-> dict:
    model_data={}
    row_data = row.select('td')

    for i, td in  enumerate(row_data):
        if i == 0:
            model_data['show_number'] = td.text.replace("#","")
        elif i == 1:
            model_data['date'] = td.text
        elif i == 2:
            # get the achor tag and extract the href attribute
            link  = td.find('a')
            model_data['url'] = base_url + link.attrs['href']
            model_data['title'] = link.text
        elif i ==3:
            model_data['guest'] = td.text
    return model_data




base_url = 'https://talkpython.fm'
url = 'http://talkpython.fm/episodes/all'




response = requests.get(url)

# print("Reflex Framework: Frontend, Backend, Pure Python" in response.text)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.select('tbody > tr')
# print(rows[0])


# episodes = []


# for row in rows:
#     data = extract_episode_data(row)
#     episodes.append(Episode(**data))
    # print(data)
    # break


episodes = [Episode(**extract_episode_data(row)) for row in rows]


# print(episodes[0])
search_term = input("Enter a search term: ")
results  = [e for e in episodes if search_term.lower() in e.title.lower()]
print(f"\n Epiode with the term {search_term}: ")
pprint(results)