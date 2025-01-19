import requests

from bs4 import BeautifulSoup


url = 'https://pixelford.com/blog/'
#response = requests.get(url)
response = requests.get(url, headers = {'user-agent': 'Ceci'}) # Le cambiamos el nombre al user-agent (cualquier nombre random) para que no lo bloquee el servidor    

#print(response)
#print(response.status_code)
#print(response.text)
#print(response.content)

html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")

for each in a_tags:
    #print(each)
    #print(each.get('href')) #para obtener
    print(each.text) #para obtener el texto


map_entry_titles = list(map(lambda each: each.text, a_tags))

print(map_entry_titles)




