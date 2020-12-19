// from data.js
var tableData = data;
console.log(tableData);
tbody = d3.select("tbody");

// Using the UFO dataset provided in the form of an array of JavaScript objects, write code that appends a table to your web page and then adds new rows of data for each UFO sighting.

// tableData.forEach(ufodata => {
//     var row = tbody.append("tr");
//     Object.defineProperties(ufodata).forEach(function([key, value]) {
//         var cell = row.append("td");
//         cell.text(value);
//     });
// });
tableData.forEach(function(ufoSighting) {
    console.log(ufoSighting);
    var row = tbody.append("tr");
    Object.entries(ufoSighting).forEach(function([key, value]) {
        console.log(key, value);
        var cell = row.append("td");
        cell.text(value);
    });
});

// Use a date form in your HTML document and write JavaScript code that will listen for events and search through the date/time column to find rows that match user input.

// var button = d3.select("#filter-btn");
// button.on("click", function() {
//     var date_input = d3.select("#datetime");
//     var input_value = date_input.properly("value");
//     console.log(input_value);
//     tbody.html("");

//     var filteredData = tableData.filter(data => data.datetime === input_value);
//     console.log(filteredData);

//     if (filteredData.length >= 1) {
//         filteredData.forEach(filtered_data => {
//             var row = tbody.append("tr");
//             Object.defineProperties(filtered_data).forEach(function([key, value]) {
//                 var cell = row.append("td");
//                 cell.text(value);
//             });
//         });
//     } else {
//         tbody.append("h5").text("Data not found for this selection. Please retry with another date!");
//     }
// });

var button = d3.select("filter-btn");
button.on("click", function() {
    tbody.html("");
    
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue);
    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);
    console.log(filteredData);

    filteredData.forEach(function(selections) {
        console.log(selections);
        var row = tbody.append("tr");
        Object.entries(selections).forEach(function([key, value]) {
            console.log(key, value);
            var cell = row.append("td");
            cell.text(value);
        });
    });
});