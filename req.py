from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["test"]
collection = db["bincom_colors"]

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
variance = sum((check[value] - mean_freq) ** 2 for value in check) / len(check) #a generator expression
p_red = check["RED"] / len(all_colors)

for color, freq in check.items():
	collection.insert_one({"color": color, "frequency": freq})

# a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_fxn(arr, target):
	if len(arr) == 0:
		return False
	if arr[0] == target:
		return True
	else:
		return recursive_fxn(arr[1:], target)


result = [random.randint(0, 1) for _ in range(4)]
num = "".join(str(x) for x in result)

# convert to base 10
base_10 = int(num, 2)



# print(f"Mean color: {mean_color}")
# print(f"Most worn color is: {max_color}")
# print(sorted_color)
# print(sorted_color[index])
# print(variance)
# print(f"{p_red:.2f}")
# print(num)
# print(base_10)


def fibonacci(n):
	a, b = 0, 1
	total = 0
	for i in range(n):
		total += a
		c = a + b
		a = b
		b = c
	return total

print(fibonacci(50))