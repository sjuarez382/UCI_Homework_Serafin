// from data.js
var tableData = data;

tbody = d3.select("tbody");

// Using the UFO dataset provided in the form of an array of JavaScript objects, write code that appends a table to your web page and then adds new rows of data for each UFO sighting.

tableData.forEach(ufodata => {
    var row = tbody.append("tr");
    Object.defineProperties(ufodata).forEach(function([key, value]) {
        var cell = row.append("td");
        cell.text(value);
    });
});
