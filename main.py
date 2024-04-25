from flask import Flask, render_template
from flask_caching import Cache
import boto3

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("nobel")

@app.route("/")
def home():
	cache_country = cache.get("country")
	cache_money = cache.get("money")
	cache_category = cache.get("category")

	if cache_country and cache_money and cache_category:
		return render_template(
			"index.html",
			most_country = cache_country,
			most_money = cache_money,
			most_category = cache_category
		)
	else:
		response_countries = table.get_item(Key ={"rank": "countries"})
		response_money = table.get_item(Key ={"rank": "money"})
		response_categories = table.get_item(Key ={"rank": "categories"})

		most_country = response_countries["Item"]["first"]
		most_money = response_money["Item"]["first"]
		most_category = response_categories["Item"]["first"]
		
		cache.set("country", most_country, timeout=86400) # 86400 sec = 1 day
		cache.set("money", most_money, timeout=86400)
		cache.set("category", most_category, timeout=86400)

		cache_country = cache.get("country")
		cache_money = cache.get("money")
		cache_category = cache.get("category")

		return render_template(
			"index.html",
			most_country = cache_country,
			most_money = cache_money,
			most_category = cache_category
		)

if __name__ == "__main__":
	app.run(debug=True)