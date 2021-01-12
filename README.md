# JSON2YOLOv5
Transform a .JSON annotation file to multiple YOLOv5 annotation files

This code is doing the following:
 - imports a .JSON file
 - read the .JSON file
 - read the size of all .JPG files, needed for YOLOv5 coordinates, because these coordinates are percents
 - goes through relevant records and creates files with object names and coordinates
     - transforms the coordinates from .JSON (in this case COCO: top-left and bottom right of the box) to YOLOv5: Xcenter, Ycenter, weight, height

