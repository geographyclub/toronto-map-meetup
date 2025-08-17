# toronto-map-meetup
Files for the Toronto Map Meetup @newsystems_

## Styling in JSON

### Point Examples

Circles:  
```
{
    "id": "points",
    "source": "events",
    "filter": ["!", ["has", "point_count"]],
    "type": "circle",
    "paint": {
        "circle-radius": 6,
        "circle-color": "hsl(232, 76%, 84%)",
        "circle-stroke-width": 0,
        "circle-stroke-color": "hsl(180, 21%, 5%)"
    }
}
```

POIs:  
```
{
    "id": "poi-amenity",
    "source": "osm",
    "source-layer": "pois",
    "type": "symbol",
    "layout": {
        "icon-size": 0.5,
        "symbol-placement": "point",
        "icon-optional": true,
        "icon-image": [ "match", [ "get", "amenity" ], "arts_centre", "icon-art_gallery", "atm", "icon-atm", "bank", "icon-bank", "bar", "icon-bar", "bench", "icon-bench", "bicycle_rental", "icon-bicycle_share", "biergarten", "icon-beergarden", "cafe", "icon-cafe", "car_rental", "icon-car_rental", "car_sharing", "icon-car_rental", "car_wash", "icon-car_wash", "cinema", "icon-cinema", "college", "icon-college", "community_centre", "icon-community", "dentist", "icon-dentist", "doctors", "icon-doctor", "dog_park", "icon-dog_park", "drinking_water", "icon-drinking_water", "embassy", "icon-embassy", "fast_food", "icon-fast_food", "fire_station", "icon-fire_station", "fountain", "icon-fountain", "grave_yard", "icon-cemetery", "hospital", "icon-hospital", "hunting_stand", "icon-huntingstand", "library", "icon-library", "marketplace", "icon-marketplace", "nightclub", "icon-nightclub", "nursing_home", "icon-nursinghome", "pharmacy", "icon-pharmacy", "place_of_worship", "icon-place_of_worship", "playground", "icon-playground", "police", "icon-police", "post_box", "icon-postbox", "post_office", "icon-post", "prison", "icon-prison", "pub", "icon-beer", "recycling", "icon-recycling", "restaurant", "icon-restaurant", "school", "icon-school", "shelter", "icon-shelter", "telephone", "icon-telephone", "theatre", "icon-theatre", "toilets", "icon-toilet", "townhall", "icon-town_hall", "vending_machine", "icon-vendingmachine", "veterinary", "icon-veterinary", "waste_basket", "icon-waste_basket", "unknown" ],
        "text-font": [ "volksans-regular" ],
        "text-size": 10,
        "text-field": ["get", "name"],
        "text-max-width": 8,
        "text-line-height": 1,
        "icon-anchor": "bottom",
        "text-anchor": "top",
        "icon-allow-overlap": false,
        "text-allow-overlap": false,
        "icon-ignore-placement": false,
        "text-ignore-placement": false
    },
    "paint": {
        "icon-opacity": [ "interpolate", [ "linear" ], [ "zoom" ], 15, 0, 16, 1 ],
        "text-opacity": [ "interpolate", [ "linear" ], [ "zoom" ], 15, 0, 16, 1 ],
        "icon-color": "hsl(227, 89%, 90%)",
        "text-color": "hsl(227, 89%, 90%)",
        "text-halo-color": "hsl(0, 0%, 100%)",
        "text-halo-width": 0,
        "text-halo-blur": 0
    },
    "minzoom": 15
}
```

### Line Examples

Dash line:  
```
{
    "id": "ferry",
    "source": "osm",
    "source-layer": "ferries",
    "type": "line",
    "paint": {
        "line-color": "hsl(200, 100%, 60%)",
        "line-dasharray": [2, 2],
        "line-width": 1
    }
}
```

Line with options:  
```
{
    "id": "highway-minor",
    "source": "osm",
    "source-layer": "streets",
    "filter": [ "in", "kind", "unclassified", "residential", "living_street" ],
    "type": "line",
    "paint": {
        "line-color": "hsl(230, 5%, 25%)",
        "line-width": [ "interpolate", [ "exponential", 2 ], [ "zoom" ], 10, 0, 20, 92 ],
        "line-opacity": [ "interpolate", [ "linear" ], [ "zoom" ], 14, 0, 15, 1 ]
    },
    "layout": {
        "line-join": "round",
        "line-cap": "round"
    },
    "minzoom": 14
}
```

### Polygon Examples

Fill:  
```
{
    "id": "airport-area",
    "source": "osm",
    "source-layer": "street_polygons",
    "filter": [ "in", "kind", "runway", "taxiway" ],
    "type": "fill",
    "paint": {
        "fill-color": "hsl(214, 23%, 90%)",
        "fill-opacity": { "stops": [ [ 11, 0 ], [ 12, 1 ] ] }
    }
}
```

Fill with case:  
```
{
    "id": "propertyboundaries",
    "source": "toronto",
    "source-layer": "propertyboundaries",
    "type": "fill",
    "paint": {
        "fill-color": [
            "case",
            ["in", ["get", "FEATURE_TYPE"], "CONDO"], "hsl(24, 32%, 80%)",
            ["in", ["get", "FEATURE_TYPE"], "CORRIDOR"], "hsl(210, 30%, 80%)",
            ["in", ["get", "FEATURE_TYPE"], "RESERVE"], "hsl(24, 32%, 85%)",
            ["in", ["get", "FEATURE_TYPE"], "COMMON"], "hsl(24, 32%, 95%)",
            "hsl(0, 0%, 95%)"
        ],
        "fill-opacity": ["interpolate", ["linear"], ["zoom"], 15, 0, 16, 1]
    }
}
```

Fill extrusion:  
```
{
    "id": "buildings",
    "source": "toronto_buildings",
    "source-layer": "toronto_buildings",
    "type": "fill-extrusion",
    "paint": {
        "fill-extrusion-color": "hsl(280, 10%, 40%)",
        "fill-extrusion-height": [
            "case",
            ["!=", ["get", "max_height"], null], ["get", "max_height"],
            ["!=", ["get", "avg_height"], null], ["get", "avg_height"],
            10
        ],
        "fill-extrusion-base": 0,
        "fill-extrusion-opacity": ["interpolate", ["linear"], ["zoom"], 15, 0, 16, 0.7, 17, 0.7, 18, 0]
    },
    "minzoom": 15
}
```