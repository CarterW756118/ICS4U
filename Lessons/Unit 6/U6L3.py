# Modify 1
import requests as req
from bs4 import BeautifulSoup

url = "https://weather.gc.ca/rss/weather/43.586_-79.657_e.xml"  # Mississauga weather

try:
    rx = req.get(url, timeout=10)
    if rx.status_code == 200:
        stuff = BeautifulSoup(rx.content, 'xml')
        entries = stuff.find_all('entry')

        for entry in entries:
            title = entry.title.text
            summary = entry.summary.text

            print(title)
            print("Summary:", summary)
            print()   # blank line for spacing

except Exception as e:
    print("Error occurred:", e)

# Modify 2
import requests as req
from bs4 import BeautifulSoup

local = "https://globalnews.ca/toronto/feed/"
national = "https://globalnews.ca/national/feed/"
world = "https://globalnews.ca/world/feed/"
style = "https://globalnews.ca/lifestyle/feed/"

choice = input("Local (L), National (N), World (W), or Style (S)? ").upper()

if choice == "L":
    url = local
elif choice == "N":
    url = national
elif choice == "W":
    url = world
elif choice == "S":
    url = style
else:
    print("Invalid choice!")

try:
    rx = req.get(url, timeout=10)
    if rx.status_code == 200:
        stuff = BeautifulSoup(rx.content, 'xml')
        items = stuff.find_all('item')

        for item in items:
            title = item.title.text
            summary = item.description.text
            link = item.link.text

            print(f"Title: {title}")
            print(f"Summary: {summary}")
            print(f"Link: {link}")
            print("-----")

except Exception as e:
    print("Error occurred:", e)
