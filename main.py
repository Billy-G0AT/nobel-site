from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	most_country = "1"
	most_money = "2"
	most_category = "3"
	return render_template(
		"index.html",
		most_country = most_country,
		most_money = most_money,
		most_category = most_category
	)

if __name__ == "__main__":
	app.run(debug=True)