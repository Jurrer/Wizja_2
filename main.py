from Classify_Image import *
from Process_Image import *
from Display_Video import *
import pandas as pd
import cv2

# zmiana sposobu wyświetlania danych typu float
pd.options.display.float_format = "{:.2f}".format

if __name__ == '__main__':

    path_to_vid = './model/PA_1.avi'
    q = cv2.VideoCapture(path_to_vid)

    if not q.isOpened():
        print("Error opening video stream or file")
    i = 0
    while q.isOpened():
        ret, frame = q.read()
        i = i + 1
        if i > 125:
            if ret:
                cv2.imshow('Frame', frame)# wyświetlamy aktualną klatkę
                lo, tc = ekstrakcja_cech(frame) #ekstrachujemy cechy
                classify_frame(tc) #klasyfykujemy obiekty na podstawie ich cech
                # cv2.waitKey(100)
                clear() #czyścimy widok w konsoli
                print('\n')
                # pokaz_wiele(lo, 2, listatyt=ile_figur, colmap='winter') # na życzenie pokazujemy wykryte obiekty

            if cv2.waitKey(25) & 0xFF == ord('q'): #dodaje możliwość zamknięcia programu wysyłając klawisz q
                break

    destroy_vid(q)

