import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Machine_learning"
REQUEST_HEADERS = {"User-Agent": "simple-scraper/0.1"}

# fetch page
response = requests.get(URL, headers=REQUEST_HEADERS, timeout=15)
response.raise_for_status()
html_content = response.text

# parse
soup = BeautifulSoup(html_content, "html.parser")

# find table
content_div = soup.find("div", id="mw-content-text")
selected_table = None
data_rows = []
if content_div:
    for table_candidate in content_div.find_all("table"):
        candidate_data_rows = []
        for table_row in table_candidate.find_all("tr"):
            table_cells = table_row.find_all("td")
            if table_cells:
                row_cells = []
                for table_cell in table_cells:
                    cell_text = " ".join(table_cell.get_text(separator=" ", strip=True).split())
                    row_cells.append(cell_text)
                candidate_data_rows.append(row_cells)
        if len(candidate_data_rows) >= 3:
            selected_table = table_candidate
            data_rows = candidate_data_rows
            break

if not selected_table:
    print("No suitable table found.")
    raise SystemExit(1)

# headers
headers = []
table_head = selected_table.find("thead")
if table_head:
    header_cells = table_head.find_all("th")
    if header_cells:
        headers = [" ".join(header_cell.get_text(separator=" ", strip=True).split()) for header_cell in header_cells]
if not headers:
    first_row = selected_table.find("tr")
    if first_row:
        header_cells = first_row.find_all("th")
        if header_cells:
            headers = [" ".join(header_cell.get_text(separator=" ", strip=True).split()) for header_cell in header_cells]

# if still no headers, use first data row
if not headers and data_rows:
    headers = data_rows[0]
    data_rows = data_rows[1:]

# ensure header count matches max columns
max_columns = max((len(row) for row in data_rows), default=len(headers))
if len(headers) < max_columns:
    for i in range(len(headers) + 1, max_columns + 1):
        headers.append(f"Column {i}")

# pad rows??
padded_rows = []
for row in data_rows:
    padded_rows.append(row + [""] * (len(headers) - len(row)))

# simple CSV quoting
def quote_field(value):
    if value is None:
        value = ""
    value = str(value)
    if '"' in value:
        value = value.replace('"', '""')
    return f'"{value}"'

# write file
with open("wiki_table.csv", "w", encoding="utf-8", newline="") as output_file:
    output_file.write(",".join(quote_field(h) for h in headers) + "\n")
    for row in padded_rows:
        output_file.write(",".join(quote_field(c) for c in row) + "\n")

print(f"Saved wiki_table.csv ({len(padded_rows)} rows, {len(headers)} cols)")
