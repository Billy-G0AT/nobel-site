from flask import Flask, render_template
import boto3

app = Flask(__name__)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("nobel")

@app.route("/")
def home():
	response_countries = table.get_item(Key ={"rank": "countries"})
	response_money = table.get_item(Key ={"rank": "money"})
	response_categories = table.get_item(Key ={"rank": "categories"})

	most_country = response_countries["Item"]["first"]
	most_money = response_money["Item"]["first"]
	most_category = response_categories["Item"]["first"]
	
	return render_template(
		"index.html",
		most_country = most_country,
		most_money = most_money,
		most_category = most_category
	)

if __name__ == "__main__":
	app.run(debug=True)