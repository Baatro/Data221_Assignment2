import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url, headers ={'User-agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text")

# Forbidden >:( headings
exclude = {"references", "external links", "see also", "notes"}

headings = []

for h2 in content.find_all("h2"):
    # Extract the visible text only
    text = h2.get_text(strip=True)

    # Remove "[edit]" if present
    text = text.replace("[edit]", "").strip()

    # Skip empty or excluded headings
    if not text:
        continue
    if text.lower() in exclude:
        continue

    headings.append(text)

# Save to file
with open("headings.txt", "w", encoding="utf-8") as f:
    for h in headings:
        f.write(h + "\n")

print("Done. Saved to headings.txt")
