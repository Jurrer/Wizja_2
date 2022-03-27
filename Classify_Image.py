from tabulate import tabulate
import numpy as np
import math

Hu = ['Hu numbers' for i in range(7)]
lista_cech = ['EulerNumber', 'Area', 'BoundingBoxArea', 'FilledArea', 'Extent', 'EquivDiameter', 'Solidity',
              'FilledArea/BoundingBoxArea', ] + Hu

a = 271
b = 286
c = 286


# print(max(a, b, c) - min(a, b, c))

def classify_frame(tc):  # tabela cech jest klasyfikowana
    temp_tc = np.c_[range(0, 18), tc[0:18]]
    table = tabulate(temp_tc, lista_cech, tablefmt='fancy_grid')
    print(table)

    data = temp_tc
    # Classifying by areas
    classification_matrix = [
        ["big_circle", 1413, 5],
        ["medium_circle", 665, 4],
        ["small_circle", 292, 0],
        ["big_square", 1721, 79],
        ["medium_square", 841, 54],
        ["small_square", 271, 15],
    ]

    classified_matrix = [[0] * 2 for _ in range(data.shape[0])]

    for i in range(data.shape[0]):  # wyciągam liczbę wierszy
        for x in range(len(classification_matrix)):  # lecę po wszystkich wierszach classification_matrix
            if math.isclose(data[i][2], classification_matrix[x][1], abs_tol=classification_matrix[x][2]):
                print(classification_matrix[x][0], " is object number: ", f'{data[i][0]:.0f}')
                classified_matrix[i][0] = i
                classified_matrix[i][1] = classification_matrix[x][0]
    print(classified_matrix)
    return classified_matrix
