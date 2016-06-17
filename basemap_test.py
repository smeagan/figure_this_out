# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 19:58:51 2016

@author: smeag
"""
#%% Basemap

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a new figure
fig_b = plt.figure(figsize=(15, 12))

wLon = -105
eLon = -85
sLat = 30
nLat = 50

m = Basemap(projection='cyl',llcrnrlat=sLat,urcrnrlat=nLat,llcrnrlon=wLon,urcrnrlon=eLon,resolution='i')

m.drawcoastlines()
m.drawcountries()
m.drawstates()

plt.show()

#%% Cartopy

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

wLon = -105
eLon = -85
sLat = 30
nLat = 50

# Create a new figure
fig_c = plt.figure(figsize=(15, 12))

# Add the map and set the extent
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([eLon, wLon, sLat, nLat])

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.RIVERS)
#ax.add_feature(cfeature.COASTLINE, resolution='50m')
ax.coastlines(resolution='10m')
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES)
ax.add_feature(cfeature.BORDERS, linestyle='--', edgecolor='black')

# Add state boundaries to plot
states_provinces = cfeature.NaturalEarthFeature(category='cultural', 
    name='admin_1_states_provinces_lines',scale='50m',facecolor='none')
ax.add_feature(states_provinces, edgecolor='black', linewidth=0.7)


#map = 