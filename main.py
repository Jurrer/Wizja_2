import numpy as np
from Display_Video import *




def odczytaj(event, x, y, flags, param):
    global klik, pozycja
    if event == cv2.EVENT_LBUTTONDBLCLK:
        klik = True
        pozycja = [x, y]


def i_have_no_clue(wideo):
    prog_dolny = np.array([0, 0, 0])
    prog_gorny = np.array([255, 255, 255])
    klik = False
    pozycja = [0, 0]
    jedynki = np.array([1, 1, 1]).astype(np.uint8)
    delta_wart = [5, 10, 20, 30, 40, 50]
    delta_poz = 2
    rozmiar_maski = 7
    rozmycie = 0
    rozmycie_max = 5
    otwarcie = 0
    otwarcie_max = 5
    zamkniecie = 0
    zamkniecie_max = 5
    piksel = np.array([0, 0, 0])

    while (1):
        _, ramka_org = wideo.read()

        ramka = ramka_org
        if rozmycie > 0:
            ramka = cv2.GaussianBlur(ramka_org, (rozmiar_maski, rozmiar_maski), rozmycie * 2)
        else:
            ramka = ramka_org
        maska = cv2.inRange(ramka, prog_dolny, prog_gorny)

        if otwarcie > 0:
            es = np.ones((2 * otwarcie + 1, 2 * otwarcie + 1), np.uint8)
            segmentacja = cv2.morphologyEx(maska, cv2.MORPH_OPEN, es)
        else:
            segmentacja = maska
        if zamkniecie > 0:
            es = np.ones((2 * zamkniecie + 1, 2 * zamkniecie + 1), np.uint8)
            segmentacja = cv2.morphologyEx(segmentacja, cv2.MORPH_CLOSE, es)

        cv2.imshow('oryginalny', ramka_org)
        cv2.imshow('org_filtrowany', ramka)
        cv2.imshow('maska', maska)
        cv2.imshow('segmentacja', segmentacja)
        cv2.setMouseCallback('org_filtrowany', odczytaj)
        k = cv2.waitKey(5) & 0xFF
        zmiana = False
        zmiana2 = False
        if klik:
            piksel = ramka[pozycja[1], pozycja[0]].astype(np.int)
            print("odczyt piksela (" + str(pozycja[0]) + "," + str(pozycja[1]) + "), = " + str(piksel))
            klik = False
        # wyjscie z programu
        if k == 27:
            break
        # zmiana parametrów rozmycia
        elif k == ord('g'):
            if rozmycie < rozmycie_max:
                rozmycie += 1
            else:
                rozmycie = 0
            zmiana2 = True
        # zmiana parametrów otwarcie/zamknięcia
        elif k == ord('o'):
            if otwarcie < otwarcie_max:
                otwarcie += 1
            else:
                otwarcie = 0
            zmiana2 = True
        elif k == ord('p'):
            if zamkniecie < zamkniecie_max:
                zamkniecie += 1
            else:
                zamkniecie = 0
            zmiana2 = True
            # progi pierwszej skladowej
        elif k == ord('q') and prog_dolny[0] > 0:
            prog_dolny[0] -= 1
            zmiana = True
        elif k == ord('w') and prog_dolny[0] < prog_gorny[0]:
            prog_dolny[0] += 1
            zmiana = True
        elif k == ord('e') and prog_gorny[0] > prog_dolny[0]:
            prog_gorny[0] -= 1
            zmiana = True
        elif k == ord('r') and prog_gorny[0] < 255:
            prog_gorny[0] += 1
            zmiana = True
            # progi drugiej składowej
        elif k == ord('a') and prog_dolny[1] > 0:
            prog_dolny[1] -= 1
            zmiana = True
        elif k == ord('s') and prog_dolny[1] < prog_gorny[1]:
            prog_dolny[1] += 1
            zmiana = True
        elif k == ord('d') and prog_gorny[1] > prog_dolny[1]:
            prog_gorny[1] -= 1
            zmiana = True
        elif k == ord('f') and prog_gorny[1] < 255:
            prog_gorny[1] += 1
            zmiana = True
            # progi trzeciej składowe
        elif k == ord('z') and prog_dolny[2] > 0:
            prog_dolny[2] -= 1
            zmiana = True
        elif k == ord('x') and prog_dolny[2] < prog_gorny[2]:
            prog_dolny[2] += 1
            zmiana = True
        elif k == ord('c') and prog_gorny[2] > prog_dolny[2]:
            prog_gorny[2] -= 1
            zmiana = True
        elif k == ord('v') and prog_gorny[2] < 255:
            prog_gorny[2] += 1
            zmiana = True
            # parametry koloru na podstawie kliknięcia
        elif k == ord(' '):
            prog_dolny = np.clip(piksel - jedynki * delta_wart[delta_poz], 0, 255).astype(np.uint8)
            prog_gorny = np.clip(piksel + jedynki * delta_wart[delta_poz], 0, 255).astype(np.uint8)
            if (delta_poz < len(delta_wart) - 1):
                delta_poz += 1
            else:
                delta_poz = 0
            zmiana = True

        if zmiana:
            print(
                "klawisz: " + str(k) + ", segm. - prog dolny: " + str(prog_dolny) + ", prog górny: " + str(prog_gorny))
        if zmiana2:
            print("klawisz: " + str(k) + ", Gauss: " + str(rozmycie) + ", otwarcie: " + str(
                otwarcie) + ", zamkniecie: " + str(zamkniecie))


if __name__ == '__main__':
    path_to_vid = './model/PA_1.avi'
    video = cv2.VideoCapture(path_to_vid)
    i_have_no_clue(video)
    destroy_vid(video)