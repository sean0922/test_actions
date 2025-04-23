import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(resp.text, "html.parser")
#Method1 select
print("Method1 select")
for item in soup.select("span.titleline a"):
    print(item.text.strip())

#Method2 find_all
print('\n',"Method2 find_all")
for item in soup.find_all("span", class_="titleline"):
    print(item.a.text.strip())