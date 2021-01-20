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