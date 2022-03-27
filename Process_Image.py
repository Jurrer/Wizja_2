import cv2
import numpy as np
from skimage.measure import label, regionprops


def ekstrakcja_cech(obiekt_do_ekstrakcji_cech):
    # ekstrakcja cech
    # binaryzacja obrazu
    b = cv2.inRange(obiekt_do_ekstrakcji_cech, (1, 1, 1), (255, 255, 255))
    # etykietowanie i ekstrakcja cech
    cechy = regionprops(label(b))
    ile_obiektow = len(cechy)
    lista_cech = ['EulerNumber', 'Area', 'BoundingBoxArea', 'FilledArea', 'Extent', 'EquivDiameter', 'Solidity']
    ile_cech = len(lista_cech)
    tabela_cech = np.zeros((ile_obiektow, ile_cech + 1 + 7))  # "1" - to jedna cecha wyliczana, "7" to momenty Hu
    listaob = []
    for i in range(0, ile_obiektow):
        yp, xp, yk, xk = cechy[i]['BoundingBox']
        aktualny_obiekt = obiekt_do_ekstrakcji_cech[yp:yk, xp:xk, :]
        ret, binobj = cv2.threshold(aktualny_obiekt[:, :, 1], 0, 255, cv2.THRESH_BINARY)
        listaob.append(binobj)  # aktualny_obiekt)
        # rejestrujemy wybrane cechy wyznaczone przez regionprops
        for j in range(0, ile_cech):
            tabela_cech[i, j] = cechy[i][lista_cech[j]]
        # dodajemy momenty Hu
        hu = cv2.HuMoments(cv2.moments(binobj))
        hulog = (1 - 2 * (hu > 0).astype('int')) * np.nan_to_num(np.log10(np.abs(hu)), copy=True, neginf=-99, posinf=99)
        tabela_cech[i, ile_cech + 1:ile_cech + 8] = hulog.flatten()
    tabela_cech[:, ile_cech] = tabela_cech[:, 3] / tabela_cech[:, 2]  # cecha wyliczana
    tabela_cech[:, 0] = (tabela_cech[:, 0] == 1)  # korekta liczby Eulera
    return listaob, tabela_cech


def ekstrakcja_klas(obiekt_do_ekstrakcji_klas):
    # ekstrakcja kategorii
    # binaryzacja obrazu
    b = cv2.inRange(obiekt_do_ekstrakcji_klas, (1, 1, 1), (255, 255, 255))
    # etykietowanie i ekstrakcja cech
    cechy = regionprops(label(b))
    print("cechy: ", cechy)
    ile_obiektow = len(cechy)
    print("ile obiektów: ", ile_obiektow)
    # wyszukiwanie kolorów
    kolory = np.unique(obiekt_do_ekstrakcji_klas.reshape(-1, obiekt_do_ekstrakcji_klas.shape[2]),
                       axis=0)  # kolory w obrazie
    # według kolorów przypiszemy klasy obiektom
    kolory = kolory[1:7, :]  # usuwa kolor tła
    ile_kategorii = len(kolory)
    print("Kategorie: ", ile_kategorii)

    kategorie = np.zeros((ile_obiektow, 1)).astype('int')
    listaob = []
    for i in range(0, ile_obiektow):
        x, y = cechy[i]['Coordinates'][1]  # wsp. jednego z punktów obiektu - do próbkowania koloru
        for k in range(0, ile_kategorii):
            if list(obiekt_do_ekstrakcji_klas[x, y, :]) == list(kolory[k]):
                break
        kategorie[i] = k
    return kategorie
