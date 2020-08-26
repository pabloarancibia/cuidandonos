var locations = [
    ["LOCATION_1", -27.66, -58.99],
    ["LOCATION_2", -27.45, -58.88],
    ["LOCATION_3", -27.55, -58.77],
    ["LOCATION_4", -27.33, -58.66],
    ["LOCATION_5", -27.22, -58.55]
];

var mymap = L.map('mapa-general').setView([-25.70, -60.19], 7);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicGFibG9hcmFuY2liaWEiLCJhIjoiY2tlYTV1bHdlMGI5azMwbnhqYWhnOWs2biJ9.dS-V3ajA5fd_7XuhnvXptA'
}).addTo(mymap);

for (var i = 0; i < locations.length; i++) {
    marker = new L.marker([locations[i][1], locations[i][2]])
        .bindPopup(locations[i][0])
        // .bindPopup("<b>Nombre Comedor/Merendero</b>.").openPopup()

        .addTo(mymap);
}