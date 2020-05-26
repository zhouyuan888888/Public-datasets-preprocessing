import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

RGB= [[0,128,192],
            [128, 0, 0],
            [64, 0, 128],
            [192, 192, 128],
            [64, 64, 128],
            [64, 64, 0],
            [128, 64, 128],
            [0, 0, 192],
            [192, 128, 128],
            [128, 128, 128],
            [128, 128, 0]]

ann_dir = "/home/zhouyuan/datasets/camvid/annotation/"
save_dir = "/home/zhouyuan/datasets/camvid/annotation_p/"

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

ann_files = os.listdir(ann_dir)
for f in ann_files:
    f_path = ann_dir+f
    save_path = save_dir +f

    image = np.array(Image.open(f_path))

    Bicyclist = image == RGB[0]
    Bicyclist = np.sum(Bicyclist, axis=2)
    Bicyclist = Bicyclist==3
    Bicyclist = Bicyclist * 1

    Building = image == RGB[1]
    Building = np.sum(Building, axis=2)
    Building = Building==3
    Building = Building * 2

    Car = image == RGB[2]
    Car = np.sum(Car, axis=2)
    Car = Car == 3
    Car = Car * 3

    Column_Pole = image == RGB[3]
    Column_Pole = np.sum(Column_Pole, axis=2)
    Column_Pole = Column_Pole == 3
    Column_Pole = Column_Pole * 4

    Fence = image == RGB[4]
    Fence = np.sum(Fence, axis=2)
    Fence = Fence == 3
    Fence = Fence * 5

    Pedestrian = image == RGB[5]
    Pedestrian = np.sum(Pedestrian, axis=2)
    Pedestrian = Pedestrian == 3
    Pedestrian = Pedestrian * 6

    Road = image == RGB[6]
    Road = np.sum(Road, axis=2)
    Road = Road == 3
    Road = Road * 7

    Sidewalk = image == RGB[7]
    Sidewalk = np.sum(Sidewalk, axis=2)
    Sidewalk = Sidewalk == 3
    Sidewalk = Sidewalk * 8

    SignSymbol = image == RGB[8]
    SignSymbol = np.sum(SignSymbol, axis=2)
    SignSymbol = SignSymbol == 3
    SignSymbol = SignSymbol * 9

    Sky = image == RGB[9]
    Sky = np.sum(Sky, axis=2)
    Sky = Sky == 3
    Sky = Sky * 10

    Tree = image == RGB[10]
    Tree = np.sum(Tree, axis=2)
    Tree = Tree == 3
    Tree = Tree * 11
    final = Bicyclist + Building + Car + Column_Pole +Fence + Pedestrian + Road +Sidewalk +SignSymbol +Sky + Tree
    final = final -1
    final[final==-1] = 255

    print(np.unique(final))

    cv2.imwrite(save_path, final)
