#app.py file 

#flask
app = Flask(__name__)

#route
@app.route("/")
def home():
    print("Here are all of the available routes")