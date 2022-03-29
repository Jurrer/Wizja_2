import cv2


def display_vid(vid):
    while (vid.isOpened()):
        udany_odczyt, ramka = vid.read()
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            destroy_vid(vid)
        if udany_odczyt:  # udany odczyt ramki
            cv2.imshow('ramka', ramka)
            cv2.waitKey(1)  # większa wartosc => wolniej
            # cv2.waitKey(0)   # czekamy na wcisniecie klawisz po kazdej klatce
        else:
            destroy_vid(vid)


def destroy_vid(vid):
    vid.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
