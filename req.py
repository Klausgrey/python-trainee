from bs4 import BeautifulSoup
with open("index.html", "r",) as f:
	soup = BeautifulSoup(f, "html.parser")

all_colors = []
rows = soup.find_all("tr")

for row in rows:
	cells = row.find_all("td")
	if cells:
		day = cells[0].text
		colors = cells[1].text.split(", ")
		all_colors.extend(colors)

# print(all_colors)


check = {}

for x in all_colors:
	if x not in check:
		check[x] = 1
	else:
		check[x] += 1

# print(check)

mean_freq = sum(check.values()) / len(check)
mean_color = min(check, key=lambda color: abs(check[color] - mean_freq))
max_color = max(check, key=lambda color: check[color])
sorted_color = sorted(check, key=lambda color: check[color])
index = len(sorted_color) // 2
variance = sum([(check[value] - mean_freq) ** 2 for value in check]) / len(check)


# print(f"Mean color: {mean_color}")
# print(f"Most worn color is: {max_color}")
# print(sorted_color)
# print(sorted_color[index])
print(variance)