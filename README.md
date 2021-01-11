# JSON2YOLOv5
Transform a .JSON annotation file to multiple YOLOv5 annotation files

This code is doing the following:
creates a folder for keeping the YOLOv5 annotation files
imports a .JSON file
read the .JSON file
goes through relevant records and creates files with object names and coordinates


Missing:
 YOLOv5 requires different coordinates instead of top-left and bottom right
 the next version will contain the transfrmation from "top-left and bottom right" to YOLOv5 coordinates
