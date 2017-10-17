//Дискотека
d3.select("body").style("background-color", function() {
    return "hsl(" + Math.random() * 360 + ",100%,50%)";
});

d3.select("body").style("color", function() {
    return "hsl(" + Math.random() * 360 + ",100%,50%)";
});
