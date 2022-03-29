from tabulate import tabulate
import numpy as np
import math
from os import system, name

kordy = ['yp', 'xp', 'yk', 'xk']
Hu = ['Hu numbers' for i in range(8)]
lista_cech = ['EulerNumber', 'Area', 'BoundingBoxArea', 'FilledArea', 'Extent', 'EquivDiameter', 'Solidity',
              'FilledArea/BoundingBoxArea', ] + Hu + kordy + ["Kolory"]


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def classify_frame(tc):  # tabela cech jest klasyfikowana
    ile_elementow = tc.shape[0]
    temp_tc = np.c_[range(0, ile_elementow), tc]
    table = tabulate(temp_tc, lista_cech, tablefmt='fancy_grid')
    print(table)
    color = ["Zielony", "Żółty", "Czerwony"]
    size_coefficient = 0.9

    data = temp_tc
    # Classifying by areas
    classification_matrix = [
        ["big", 870, 50],
        ["medium", 420, 50],
        ["small", 182, 50],
    ]
    #   0       1       2       3
    classified_matrix = [[0] * 4 for _ in range(data.shape[0])]  # numer, rozmiar, kształt, kolor

    for i in range(data.shape[0]):  # wyciągam liczbę wierszy
        for y in range(len(color)):  # szukamy koloru
            z = data[i][21]
            if z == y:
                classified_matrix[i][3] = color[y]
        for x in range(len(classification_matrix)):  # szukamy rozmiaru
            if math.isclose(data[i][2], classification_matrix[x][1], abs_tol=classification_matrix[x][2]):
                print(classification_matrix[x][0], " is object number: ", f'{data[i][0]:.0f}')
                classified_matrix[i][0] = i
                classified_matrix[i][1] = classification_matrix[x][0]

        if math.isnan(data[i][8]):
            classified_matrix[i][2] = "Unindentified flying object"
        elif data[i][8] > size_coefficient:
            classified_matrix[i][2] = "kwadrat"
        elif data[i][8] < size_coefficient:
            classified_matrix[i][2] = "koło"

    print(classified_matrix)
    return classified_matrix
