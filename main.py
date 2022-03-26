from pprint import pprint

from tabulate import tabulate

from Display_Video import *
import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2

from skimage.measure import label, regionprops

from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn import tree

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from tensorflow import keras

# zmiana sposobu wyświetlania danych typu float
pd.options.display.float_format = "{:.2f}".format


# FUNKCJE POMOCNICZE

def pokaz(obraz, tytul="", osie=False, openCV=True, colmap='gray'):
    if not (osie):
        plt.axis("off")
    if obraz.ndim == 2:
        plt.imshow(obraz, cmap=colmap, vmin=0, vmax=255)
    else:
        if openCV:
            plt.imshow(cv2.cvtColor(obraz, cv2.COLOR_BGR2RGB), vmin=0, vmax=255)
        else:
            plt.imshow(obraz, interpolation='none', vmin=0, vmax=255)
    plt.title(tytul)


def polob(listaobr, ile_k=1, listatyt=[], openCV=True, wart_dpi=300, osie=True, colmap='gray'):
    rozm_obr = 5
    ile = len(listaobr)
    if len(listatyt) == 0:
        listatyt = [' '] * ile
    ile_w = np.ceil(ile / ile_k).astype(int)
    figsize_k = rozm_obr * ile_k
    figsize_w = rozm_obr * ile_w
    plt.figure(figsize=(figsize_k, figsize_w), dpi=wart_dpi)
    for i in range(0, ile):
        if isinstance(listaobr[i], np.ndarray):
            plt.subplot(ile_w, ile_k, i + 1)
            pokaz(listaobr[i], listatyt[i], osie, openCV, colmap)
    plt.show()


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


if __name__ == '__main__':
    path_to_vid = './model/PA_1.avi'
    path_to_pic1 = './model/PA_1_ref.png'
    path_to_pic2 = './model/obiekty.png'

    # wczytanie obrazu
    o = cv2.imread(path_to_pic1)
    p = cv2.imread(path_to_pic2)
    aktualnie_badany = o

    b = cv2.inRange(aktualnie_badany, (1, 1, 1), (255, 255, 255))
    # etykietowanie
    etykiety = label(b)
    # polob([aktualnie_badany, b, etykiety], 2)
    # wyznaczanie cech
    cechy = regionprops(etykiety)
    lista_cech = list(range(0, 18))
    lo, tc = ekstrakcja_cech(aktualnie_badany)
    # ka = ekstrakcja_klas(aktualnie_badany)
    polob(lo[0:18], 4, listatyt=lista_cech, colmap='winter')

    Hu = ['Hu numbers' for i in range(7)]
    lista_cech = ['EulerNumber', 'Area', 'BoundingBoxArea', 'FilledArea', 'Extent', 'EquivDiameter', 'Solidity',
                  'FilledArea/BoundingBoxArea', ] + Hu

    temp_tc = np.c_[range(0, 18), tc[0:18]]

    table = tabulate(temp_tc, lista_cech, tablefmt='fancy_grid')
    print(table)

    # Classifying by areas
    big_circle = 1413
    medium_circle = 665
    small_circle = 292
    big_square = 1721
    medium_square = 841
    small_square = 271
