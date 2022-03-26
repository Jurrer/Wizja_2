import cv2


def display_vid(vid):
    while (vid.isOpened()):
        udany_odczyt, ramka = vid.read()
        if udany_odczyt:  # udany odczyt ramki
            cv2.imshow('ramka', ramka)
            cv2.waitKey(0)  # większa wartosc => wolniej
            # cv2.waitKey(0)   # czekamy na wcisniecie klawisz po kazdej klatce
        else:  # koniec pliku
            vid.release()
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            cv2.waitKey(1)


if __name__ == '__main__':
    path_to_vid = './model/PA_1.avi'
    video = cv2.VideoCapture(path_to_vid)
    display_vid(video)
