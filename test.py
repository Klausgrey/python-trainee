from bs4 import BeautifulSoup
from collections import Counter
all_colors = []

# Open and parse the HTML file
with open('index.html', 'r') as file:
	html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Extract the table
tbody = soup.find('tbody')
rows = tbody.find_all('tr')

# Parse table data
for row in rows:
	cols = row.find_all('td')
	cols_text = cols[1].get_text()
	colors = cols_text.split(',')
	all_colors.extend([color.strip() for color in colors])
# I did something today
# counts = Counter(all_colors)
# print(counts.most_common(1))
sorted_colors = sorted(all_colors)
median = sorted_colors[len(sorted_colors) // 2]
print("Median color:", median)