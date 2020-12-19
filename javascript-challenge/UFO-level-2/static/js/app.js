// from data.js
var tableData = data;

tbody = d3.select("tbody")

function displayData(ufoSighting){
    tbody.text("")
    ufoSighting.forEach(function(ufo_sighting){
        new_tr = tbody.append("tr")
        Object.entries(ufo_sighting).forEach(function([key, value]){
            new_td = new_tr.append("td").text(value)
        })
    })
}
//displaying the data
displayData(tableData)

// button!!
var button = d3.select("#submit");
submit.on("click", function(){
    console.log("filter button test")

    d3.event.preventDefault();

    var dateInput = d3.select("#datetime");
    var cityInput = d3.select("#city");
    var stateInput = d3.select("state");
    var countryInput = d3.select("#country");
    var shapeInput = d3.select("#shape");

    console.log(dateInput.property("value"));
    console.log(cityInput.property("value"));
    console.log(stateInput.property("value"));
    console.log(countryInput.property("value"));
    console.log(shapeInput.property("value"));

    var filtered = tableData.filter(ufo_sighting => {
        return (ufo_sighting.datetime === dateInput.property("value") || !dateInput.property("value") ) &&
        (ufo_sighting.city === cityInput.property("value") || !cityInput.property("value") ) &&
        (ufo_sighting.state === stateInput.property("value") || !stateInput.property("value") ) &&
        (ufo_sighting.country === countryInput.property("value") || !sountryInput.property("value") ) &&
        (ufo_sighting.shape === shapeInput.property("value") || !shapeInput.property("value") ) &&

    })
    displayData(filtered);
});
