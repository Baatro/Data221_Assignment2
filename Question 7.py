from bs4 import BeautifulSoup
import requests

# Scrape website for the title and print
url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url, headers ={'User-agent': 'Mozilla/5.0'})
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

titles = soup.title.string
print(titles)

# Find first paragraph n print
content_div = soup.find("div", id="mw-content-text")

first_valid_paragraph = None

if content_div:
    paragraphs = content_div.find_all("p")

    # Step 3: Loop until we find one with >= 50 characters
    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) >= 50:
            first_valid_paragraph = text
            break
print(first_valid_paragraph)

