import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://pixelford.com/blog/'
response = requests.get(url, headers = {'user-agent': 'Ceci'}) # Le cambiamos el nombre al user-agent (cualquier nombre random) para que no lo bloquee el servidor    

html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")
blogs = soup.find_all('article', class_="type-post")

for each in blogs:
    title = each.find('a', class_="entry-title-link").text
    print(title)

    time_tag = each.find('time', class_="entry-time").text
    print(time_tag)

    blog_datetime = each.find('time', class_="entry-time").get('datetime')
    print(blog_datetime)

    blog_datetime_string = each.find('time', class_="entry-time").get('datetime')
    blog_datetime_S = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime_S.strftime("%A %B %d, %Y")
    print(pretty_date)

    print(f"{title} - {pretty_date}")






   

