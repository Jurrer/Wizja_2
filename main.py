from Classify_Image import *
from Process_Image import *
from Display_Video import *
import pandas as pd
import cv2
from skimage.measure import label, regionprops

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
    aktualnie_badany = q

    if not q.isOpened():
        print("Error opening video stream or file")
    i = 0
    a = 10
    while q.isOpened():
        ret, frame = q.read()
        cv2.imshow('Frame', frame)
        i = i + 1
        if i > 125:
            a = a + 1
            if ret:
                cv2.imshow('Frame', frame)
            b = cv2.inRange(frame, (0, 0, 0), (54, 53, 52)) + cv2.inRange(frame, (230, 229, 228),
                                                                          (255, 255, 255))  # a 12-16
            etykiety = label(b)
            # pokaz_wiele([aktualnie_badany, b, etykiety], 2)
            cechy = regionprops(etykiety)

            lo, tc = ekstrakcja_cech(frame)
            classify_frame(tc)
            cv2.waitKey(100)
            clear()
            print('\n')
            ile_figur = [i for i in range(tc.shape[0])]
            # pokaz_wiele(lo, 2, listatyt=ile_figur, colmap='winter') # na życzenie pokazujemy wykryte obiekty

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    destroy_vid(q)

