import os
import json

# create a folder for the YOLOv5 annotations if it doesn't exist
if not os.path.exists('YOLOv5_results'):
    os.makedirs('YOLOv5_results')

suffix = '.txt'

# import the json file from the corect path
with open('../../development/bdd100k/archive/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json') as f:
  data = json.load(f)

print("start")

# select the interesting data from the json file
for p in data:
    print(p['name'])
     

    #create the filename
    filename = os.path.join('YOLOv5_results', p['name'][:-4] + suffix)
    # create a file with "filename" name
    
    for i in p["labels"]:
        print(i["category"])
        if (i["category"] != "drivable area") and (i["category"] != "lane") :     
            mode = 'a' if os.path.exists(filename) else 'w'
            with open(filename, mode) as f:
                textline = str(i["category"]) + " " + str(i["box2d"]["x1"]) + " " + str(i["box2d"]["y1"]) + " " + str(i["box2d"]["x2"]) + " " + str(i["box2d"]["y2"])
                f.write(textline + '\n')
            print(i["box2d"]["x1"])  
            print(i["box2d"]["y1"]) 
            print(i["box2d"]["x2"]) 
            print(i["box2d"]["y2"])
    
    
# save info to yolov5 format


# create a file with "name" name
# write each object name and coordinates to a line
# save the file 