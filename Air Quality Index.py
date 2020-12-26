from bs4 import BeautifulSoup
import requests

# Get the HTML
r = requests.get("https://air-quality.com/country/india/3ffd900b?lang=en&standard=aqi_us")
html_content = r.content

# Parse the HTMLz
soup = BeautifulSoup(html_content, 'lxml')
col1 = soup.find_all('a', class_="site-item odd")
col2 = soup.find_all('a', class_="site-item even")
states = col1 + col2
with open("Air Quality Index.txt","w") as f:
    for state in states:
        State = state.find('div', class_="title").text
        AQI = state.find('div', class_="value").text
        f.write(f'{State}  : {AQI} \n')
        print(State, AQI)
