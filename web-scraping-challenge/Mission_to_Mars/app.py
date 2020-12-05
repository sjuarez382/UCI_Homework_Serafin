from flask import flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

#mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017//mission_to_mars_app"
mongo = PyMongo(app)

#landing page
@app.route("/")
def index():
    mars_data = mogo.db.mars_data.find_one()
    return render_template("index.htlm", data = mars_data)

#scrape page
@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    mars_item_data = scrape_mars.scrape()
    mars_data.update({}, mars_item_data, upsert=True)
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run(debug=True)