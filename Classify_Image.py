from tabulate import tabulate
import numpy as np
import math
from os import system, name

kordy = ['yp', 'xp', 'yk', 'xk']  # koordynaty
Hu = ['Hu numbers' for i in range(8)]
lista_cech = ['EulerNumber', 'Area', 'BoundingBoxArea', 'FilledArea', 'Extent', 'EquivDiameter', 'Solidity',
              'FilledArea/BoundingBoxArea', ] + Hu + kordy + [
                 "Kolory"]  # służy do nadania nagłówków tabeli w której podglądamy odczytane cechy


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'


def classify_frame(tc):  # tabela cech jest klasyfikowana
    ile_elementow = tc.shape[0]
    temp_tc = np.c_[range(0, ile_elementow), tc]
    table = tabulate(temp_tc, lista_cech, tablefmt='fancy_grid')
    # print(table)
    color = ["green", "yellow", "red"]
    size_coefficient = 0.9  # mówi o tym czy obiekt jest nazwany kołem czy kwadratem, jest to stosunek pola powierzchni obiektu do pola powierzchni bounding box
    data = temp_tc  # dla estetyki
    # Classifying by areas
    classification_matrix = [  # macierz mówi o tym, jakie pole powierzchni definiuje jaki rozmiar, oraz offset
        ['big', 870, 98],
        ['medium', 420, 80],
        ['small', 182, 80],
    ]

    classified_matrix = [[0] * 5 for _ in range(ile_elementow)]  # numer, rozmiar, kształt, kolor, pozycja yk

    for i in range(ile_elementow):  # wyciągam liczbę wierszy
        for y in range(len(color)):  # szukamy koloru
            z = data[i][21]
            if z == y:
                classified_matrix[i][3] = color[y]
        for x in range(len(classification_matrix)):  # szukamy rozmiaru
            if math.isclose(data[i][3], classification_matrix[x][1], abs_tol=classification_matrix[x][2]):
                # print(classification_matrix[x][0], " is object number: ", f'{data[i][0]:.0f}')
                classified_matrix[i][0] = i
                classified_matrix[i][1] = classification_matrix[x][0]

        if data[i][8] > size_coefficient:
            classified_matrix[i][2] = "square"
            classified_matrix[i][4] = data[i][17]
        elif data[i][8] < size_coefficient:
            classified_matrix[i][2] = "circle"
            classified_matrix[i][4] = data[i][17]

        if ile_elementow == 1:
            print(
                f'Currently we\'re seeing {classified_matrix[i][1]} {classified_matrix[i][3]} {classified_matrix[i][2]}')
        elif ((ile_elementow > 1) * (i == 0)):
            print(
                f'Currently we\'re seeing {classified_matrix[i][1]} {classified_matrix[i][3]} {classified_matrix[i][2]},')
        elif ((ile_elementow > 1) * (i > 0) * (i + 1 != ile_elementow)):
            print(
                f'{classified_matrix[i][1]} {classified_matrix[i][3]} {classified_matrix[i][2]},')
        elif ((ile_elementow > 1) * (i > 0) * (i + 1 == ile_elementow)):
            print(
                f'and {classified_matrix[i][1]} {classified_matrix[i][3]} {classified_matrix[i][2]}.')

    # print(classified_matrix)
    return classified_matrix
