import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(resp.text, "html.parser")

output_summary = ""

# Method1 select
output_summary += "**Method1 select:**\n"
for item in soup.select("span.titleline a"):
    output_summary += f"- {item.text.strip()}\n"

# Method2 find_all
output_summary += "\n**Method2 find_all:**\n"
for item in soup.find_all("span", class_="titleline"):
    output_summary += f"- {item.a.text.strip()}\n"

print(output_summary)