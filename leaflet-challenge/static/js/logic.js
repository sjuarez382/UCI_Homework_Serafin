var earthquakeurl =
  "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var platesjson = "static/js/tectonic_plates.json";

//defining sizes
function markerSize(mag) {
    return mag * 20000;
  }