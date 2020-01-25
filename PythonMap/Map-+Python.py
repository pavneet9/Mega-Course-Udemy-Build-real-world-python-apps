
# coding: utf-8

# In[81]:


import folium
import pandas
map = folium.Map(location= [80, -100])
fgv = folium.FeatureGroup(name="My Volcanos")

data_volcano = pandas.read_csv("C:/Users/pavneet9/Downloads/Volcanoes.txt")


# In[82]:


### FLoat -> String
# return the color based on the elevation of the volcano
def get_color(elev):
    if elev > 2000:
        return "blue"
    elif elev > 1000 or elev <=2000:
        return "green"
    elif elev <= 1000:
        return "red"
listelevation = list(data_volcano["ELEV"])
data_volcano.drop(data_volcano.columns[[i for i in range(8)]], axis = 1, inplace=True)

for index,rows in data_volcano.iterrows():
    fgv.add_child(folium.CircleMarker(location=[rows["LAT"], rows["LON"]], radius=6, popup = str(listelevation[index]), fill_color = get_color(listelevation[index]), color="grey", fill_opacity= 0.7 ))


# In[84]:


fgp = folium.FeatureGroup(name="Population Map")
fgp.add_child(folium.GeoJson(data=open('C:/Users/pavneet9/Downloads/world.json', 'r', encoding='utf-8-sig'),
                            style_function= lambda x:{ fill_color: yellow if x["Properties"]["POP2005"] > 1000000
                                                     else "orange" if 1000000 <= x["Properties"]["POP2005"] <= 2000000
                                                     else "red"}
                           ))
#fg.add_child(folium.GeoJson( data=(open('C:/Users/pavneet9/Downloads/world.json', 'r', encoding='UTF-8-sig').read() )))


# In[83]:


map.add_child(fgv)


map.add_child(folium.LayerControl())
map.save("C:/Users/pavneet9/Downloads/map.html", zoom =6, tiles="Mapbox Bright")

