import os
import json
from PIL import Image

#covert COCO to YOLOv5
def convert(wi, hi, x1, y1, x2, y2):
    dw = 1./wi
    dh = 1./hi
    x = (x1 + x2)/2.0 - 1
    y = (y1 + y2)/2.0 - 1
    w = x2 - x1
    h = y2 - y1
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

#[ 'car', 'truck', 'person', 'traffic_sign', 'traffic_light', 'bus', 'rider', 'bike']
def object_type_to_number(type):
    #print(type)
    number = 0
    if type == "car":
        number = 1
    if type == "truck":
        number = 2
    if type == "person":
        number = 3
    if type == "traffic sign":
        number = 4                
    if type == "traffic light":
        number = 5
    if type == "bus":
        number = 6
    if type == "rider":
        number = 7
    if type == "bike":
        number = 8
    #print(number)
    return number                            

# create a folder for the YOLOv5 annotations if it doesn't exist
if not os.path.exists('YOLOv5_results'):
    os.makedirs('YOLOv5_results')

suffix = '.txt'

# import the json file from the corect path
with open('data/archive/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_train.json') as f:
  data = json.load(f)

print("start")

# select the interesting data from the json file
for p in data:
    filename1 = os.path.join('data/archive/bdd100k/bdd100k/images/100k/train',p['name'])
    print("filename1: ", filename1)
    im=Image.open(filename1)
    wi,hi = im.size 

    #create the filename
    filename2 = os.path.join('YOLOv5_results/100k/train', p['name'][:-4] + suffix)
    # create a file with "filename" name
    
    for i in p["labels"]:
        #print(i["category"])
        if (i["category"] != "drivable area") and (i["category"] != "lane") :     
            x, y, w, h = convert(wi,hi,i["box2d"]["x1"], i["box2d"]["y1"], i["box2d"]["x2"], i["box2d"]["y2"])
            mode = 'a' if os.path.exists(filename2) else 'w'
            with open(filename2, mode) as f:
                number = str(object_type_to_number(i["category"]))
                #print(number)
                textline = number + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                print(textline)
                f.write(textline + '\n')
            #print(i["box2d"]["x1"])  
            #print(i["box2d"]["y1"]) 
            #print(i["box2d"]["x2"]) 
            #print(i["box2d"]["y2"])
    
    