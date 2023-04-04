def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import folium
import geocoder



g = geocoder.ip("127.0.0.1")

address = g.latlng

map1 = folium.Map(location = address, zoom_start=12)
folium.CircleMarker(location=address, radius=50, popup="mumbai").add_to(map1)
folium.Marker(address,popup="mumbai").add_to(map1)

map1.save("map.html ")

