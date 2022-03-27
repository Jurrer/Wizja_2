from Classify_Image import *
from Display_image import *
from Process_Image import *
from Display_Video import *
import pandas as pd
import cv2
from skimage.measure import label, regionprops

# import numpy as np
# import math
# import seaborn as sns
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
#
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import NearestNeighbors
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neighbors import NearestCentroid
# from sklearn.naive_bayes import GaussianNB
# from sklearn.cluster import KMeans
# from sklearn.metrics import confusion_matrix
# from sklearn import tree
#
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Flatten
# from keras.layers import Convolution2D, MaxPooling2D
# from tensorflow import keras

# zmiana sposobu wyświetlania danych typu float
pd.options.display.float_format = "{:.2f}".format

if __name__ == '__main__':
    path_to_vid = './model/PA_1.avi'
    path_to_pic1 = './model/PA_1_ref.png'
    path_to_pic2 = './model/obiekty.png'

    # wczytanie obrazu
    o = cv2.imread(path_to_pic1)
    p = cv2.imread(path_to_pic2)
    q = cv2.VideoCapture(path_to_vid)
    aktualnie_badany = o

    if not q.isOpened():
        print("Error opening video stream or file")

    # while q.isOpened():
    #     ret, frame = q.read()
    #     if ret:
    #         cv2.imshow('Frame', frame)
    #     b = cv2.inRange(aktualnie_badany, (1, 1, 1), (255, 255, 255))
    #     etykiety = label(b)
    #     cechy = regionprops(etykiety)
    #     lo, tc = ekstrakcja_cech(aktualnie_badany)
    #
    #
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         break
    #
    # destroy_vid(q)

    b = cv2.inRange(aktualnie_badany, (1, 1, 1), (255, 255, 255))
    etykiety = label(b)  # etykietowanie

    # polob([aktualnie_badany, b, etykiety], 2)

    cechy = regionprops(etykiety)  # wyznaczanie cech
    lo, tc = ekstrakcja_cech(aktualnie_badany)
    # ka = ekstrakcja_klas(aktualnie_badany)
    pokaz_wiele(lo[0:5], 4, listatyt=lista_cech, colmap='winter')

    classify_frame(tc)
