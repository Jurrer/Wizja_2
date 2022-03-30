import cv2
import numpy as np
import matplotlib.pyplot as plt


def pokaz(obraz, tytul="", osie=False, openCV=True,
          colmap='gray'):  # możliwość pokazania jednego obrazu na podstawie macierzy numpy
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


def pokaz_wiele(listaobr, ile_k=1, listatyt=[], openCV=True, wart_dpi=300, osie=True,
                colmap='gray'):  # funkcja używana do zobrazowania wykrytych obiektów
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
