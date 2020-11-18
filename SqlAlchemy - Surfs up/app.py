#app.py file 

#flask
app = Flask(__name__)

#route
@app.route("/")
def home():
    print("Here are all of the available routes")

#Convert the query results to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():

#
@app.route("/api/v1.0/stations")
def stations():

#
@app.route("/api/v1.0/tobs")
def tobs():

#
@app.route("/api/v1.0/<start>")
def start():

#
@app.route("/api/v1.0/<start>/<end>")
def end():

















if __name__ == '__main__':
    app.run(debug=True)