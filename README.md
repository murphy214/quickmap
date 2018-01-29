# quickmap
Fast command line views of geojson files


## How to use 
Super simple views of geojson files using mapbox-gl-js

# Install
```
pip install git+https://github.com/murphy214/quickmap
```
# Mapbox token enviromental variable 

Either add this line to your .bash_profile or export it temporarily in the terminal, of course with your real mapbox access token.
 ```
 export MAPBOX_ACCESS_TOKEN = 'your mapbox access token'
 ```

# Usage 
map geojson_file.geojson

# Other useful information 
If you have a "COLORKEY" field in your properties as well as a valid color that works with mapbox gl-js styles (some plain text ('red'), rgba(), hex colorkeys etc. it will automatically style your feature based on that field. 


 
 
 
