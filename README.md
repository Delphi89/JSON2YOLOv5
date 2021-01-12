# JSON2YOLOv5
Transform a .JSON annotation file to multiple YOLOv5 annotation files

This code is doing the following:
 - imports a .JSON file
 - read the .JSON file
 - read the size of all .JPG files, needed for YOLOv5 coordinates, because these coordinates are percents
 - goes through relevant records and creates files with object names and coordinates
     - transforms the coordinates from .JSON (in this case COCO: top-left and bottom right of the box) to YOLOv5: Xcenter, Ycenter, weight, height

example of JSON file:

[
    {
        "name": "b1c66a42-6f7d68ca.jpg",
        "attributes": {
            "weather": "overcast",
            "scene": "city street",
            "timeofday": "daytime"
        },
        "timestamp": 10000,
        "labels": [
            {
                "category": "traffic sign",
                "attributes": {
                    "occluded": false,
                    "truncated": false,
                    "trafficLightColor": "none"
                },
                "manualShape": true,
                "manualAttributes": true,
                "box2d": {
                    "x1": 1000.698742,
                    "y1": 281.992415,
                    "x2": 1040.626872,
                    "y2": 326.91156
                },
                "id": 0
            },
          
example of generated b1c66a42-6f7d68ca.txt file coresponding to b1c66a42-6f7d68ca.jpg file:
traffic sign 0.49099723632812503 0.43147047152777784 0.009185988281249991 0.009526212499999945
...
