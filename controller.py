import cv2
# import matplotlib.pyplot as plt
# import numpy as np
import time

import view
# from view import get_openFile

def run():
    startTime = time.time()


    before_file = view.get_openFile()
    saveDir = view.get_saveDir()

    savePath = saveDir + ('/Genshin.png')

    img1 = cv2.imread(before_file)
    img_genshin = cv2.imread('./pic/genshin.png')

    # GET IMAGE RESOLUTION
    height, width = img1.shape[:2]
    genHeight, genWidth = img_genshin.shape[:2]
    resize_img_genshin = cv2.resize(img_genshin, (width/7, width/7))

    # IMAGE PLACE
    img1[:height,:width] = resize_img_genshin

    # OUTPUT
    cv2.imwrite(savePath, resize_img_genshin)


    endTime = time.time()
    endTime = endTime - startTime
    view.set_processTime()