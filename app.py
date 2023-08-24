# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page.")
    return(
        f"Welcome to the climate challenge API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        )
@app.route("/api/v1.0/precipitation")
def precipitation_data():
    print("Server received request for 'Data' page.")
    return("Here is the precipitation data over the last 12 months.")
@app.route("/api/v1.0/stations")
def station_data():
    print("Server received request for 'Data' page.")
    return("Stations from the dataset.")
@app.route("/api/v1.0/tobs")
def tobs_data():
    print("Server received request for 'Data' page.")
    return("Dates and temperatures from the most active station.")


if __name__ == "__main__":
    app.run(debug=True)

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
