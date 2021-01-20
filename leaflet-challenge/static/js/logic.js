var earthquakeurl =
  "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var platesjson = "static/js/tectonic_plates.json";

//defining sizes
function markerSize(mag) {
    return mag * 20000;
  }

//function for correcting date format

function covertTimestamp(time) {
    var date = new Date(time).toLocaleDateString("en-US");
    return date;
  }

//function for color defining

function getColor(d) {
    return (d === "0-1") | (d < 1)
      ? "rgba(183,243,77)"
      : (d === "1-2") | ((d < 2) & (d >= 1))
      ? "rgba(225,243,77)"
      : (d === "2-3") | ((d < 3) & (d >= 2))
      ? "rgba(243,219,77)"
      : (d === "3-4") | ((d < 4) & (d >= 3))
      ? "rgba(243,186,77)"
      : (d === "4-5") | ((d < 5) & (d >= 4))
      ? "rgb(240,167,107)"
      : "rgb(240,107,107)";
  }

// circle data

var earthquakeCircles = [];

d3.json(earthquakeurl, function (data) {
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {
  console.log(earthquakeData)

  for (var i = 0; i < earthquakeData.length; i++) {
    var location = [
      earthquakeData[i].geometry.coordinates[1],
      earthquakeData[i].geometry.coordinates[0],
    ];
    earthquakeCircles.push(
        L.circle(location, {
          stroke: false,
          fillOpacity: 1,
          color: "black",
          weight: 1,
          fillColor: getColor(earthquakeData[i].properties.mag),
          radius: markerSize(earthquakeData[i].properties.mag),
        }).bindPopup(
          "<h1>" +
            earthquakeData[i].properties.place +
            "</h1>" +
            "<hr>" +
            "<h3>Magnitude: " +
            earthquakeData[i].properties.mag +
            "</h3>" +
            // "<br>" +
            "<h3>Date: " +
            covertTimestamp(earthquakeData[i].properties.time) +
            "</h3>"
        )
      );
    }

    //earthquake layer
    createImageBitmap(earthquakeCircles);
}

function createMap(earthquakeCircles) {
    // Create tiles
    var satellite = L.tileLayer(
      "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
      {
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: "mapbox.streets-satellite",
        accessToken: API_KEY,
      }
    );

    var streets = L.tileLayer(
        "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
        {
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox.streets",
          accessToken: API_KEY,
        }
      );