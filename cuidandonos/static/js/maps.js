var mymap = L.map('mapid').setView([-27.45, -58.97], 9);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicGFibG9hcmFuY2liaWEiLCJhIjoiY2tlYTV1bHdlMGI5azMwbnhqYWhnOWs2biJ9.dS-V3ajA5fd_7XuhnvXptA'
}).addTo(mymap);


// var marker = new L.Marker([-27.45, -58.97], { draggable: true });
var marker = new L.Marker([-27.45, -58.97]);
mymap.addLayer(marker);

function onMapClick(e) {
    mymap.removeLayer(marker)
    marker = new L.Marker(e.latlng);
    mymap.addLayer(marker);
    marker.bindPopup("<b>Nombre Comedor/Merendero</b>.").openPopup();

    $('#lat').val(e.latlng.lat);
    $('#long').val(e.latlng.lng);
}
mymap.on('click', onMapClick);

// marker.on('dragend', function (event) {
//     mymap.removeLayer(marker)
//     var latlng = event.target.getLatLng();
//     marker = new L.Marker(latlng, { draggable: true });
//     mymap.addLayer(marker);
//     marker.bindPopup("<b>Nombre Comedor/Merendero</b>.").openPopup();

//     $('#lat').val(latlng.lat);
//     $('#long').val(latlng.lng);

    // var latlng = event.target.getLatLng();
    // console.log('algo');
    // this.bindPopup(event.toString()).openPopup();
    // $('#lat').val(latlng.lat);
    // $('#long').val(latlng.lng);
// });


