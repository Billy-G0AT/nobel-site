from collections import Counter
import requests

response = requests.get("https://api.nobelprize.org/2.1/laureates")

data = response.json()

# Stores Attributes
countries = []
money = []
categories = []

# Iterates Through Each Laureate and Gets Wanted Values Only If They Exist
for laureate in data["laureates"]:
    if "place" in laureate["birth"]: 
        country = laureate["birth"]["place"]["country"]["en"]
        countries.append(country)
    else:
        continue
        
    if "prizeAmountAdjusted" in laureate["nobelPrizes"][0]:
        prize = laureate["nobelPrizes"][0]["prizeAmountAdjusted"]
        money.append(prize)
    else:
        continue

    if "category" in laureate["nobelPrizes"][0]:
        category = laureate["nobelPrizes"][0]["category"]["en"]
        categories.append(category)
    else:
        continue


# Sorts Data Into Ranked Arrays
country_count = Counter(countries)
most_country = country_count.most_common()
most_money = sorted(money, reverse=True)
category_count = Counter(categories)
most_category = category_count.most_common()

# Country Rank
first_country = most_country[0][0]
second_country = most_country[1][0]
third_country = most_country[2][0]

# Money Rank
first_money = most_money[0]
second_money = most_money[1]
third_money = most_money[2]

# Category Rank
first_category = most_category[0][0]
second_category = most_category[1][0]
third_category = most_category[2][0]

first_places = [first_country, first_money, first_category]

print(first_places)

