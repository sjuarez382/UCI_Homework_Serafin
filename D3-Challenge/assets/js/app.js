// var svg dimensions
var svgWidth = 960;
var svgHeight = 500;

var margin = {
    top: 60,
    right: 60,
    bottom: 60,
    left: 80
  };

//dimensions for chart

var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

//starting d3 code for body and setting dimensions
var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
var chartGroup = svg
    .append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

//loading csv
