import requests
from bs4 import BeautifulSoup

url = "https://www.passiton.com/inspirational-quotes"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = []
quote_boxes = soup.find_all('div', class_='text-center mb-8')
for box in quote_boxes:
    quote_text = box.img['alt'].split(" #")
    quote = {
        'theme': box.h5.text.strip(),
        'image_url': box.img['src'],
        'lines': quote_text[0],
        'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
    }
    quotes.append(quote)

# Currently, this code produces no output

# first thing to do:
# set up a loop that outputs the "theme" and the quotation text ("lines")
for q in quotes:
    print(q["theme"], ":", q["lines"])
