var mymap = L.map('mapid').setView([-27.45, -58.97], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicGFibG9hcmFuY2liaWEiLCJhIjoiY2tlYTV1bHdlMGI5azMwbnhqYWhnOWs2biJ9.dS-V3ajA5fd_7XuhnvXptA'
}).addTo(mymap);


var marker= new L.Marker(-27.45, -58.97, {draggable:true});
function onMapClick(e) {
    mymap.removeLayer(marker)
    marker = new L.Marker(e.latlng, {draggable:true});
    mymap.addLayer(marker);
    marker.bindPopup("<b>Nombre Comedor/Merendero</b><br>Dirección.").openPopup();
}
mymap.on('click', onMapClick);


