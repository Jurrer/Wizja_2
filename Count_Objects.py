import math


def count_objects(data_for_counter):
    BYS = 0  # big yellow square
    MYS = 0  # medium yellow square
    SYS = 0  # small yellow square
    BYC = 0  # big yellow circle
    MYC = 0  # medium yellow circle
    SYC = 0  # small yellow circle
    BRS = 0  # big red square
    MRS = 0  # medium red square
    SRS = 0  # small red square
    BRC = 0  # big red circle
    MRC = 0  # medium red circle
    SRC = 0  # small red circle
    BGS = 0  # big green square
    MGS = 0  # medium green square
    SGS = 0  # small green square
    BGC = 0  # big green circle
    MGC = 0  # medium green circle
    SGC = 0  # small green circle
    for i in range(len(data_for_counter)):
        increment_flag = False
        if math.isclose(data_for_counter[i - 1][4], data_for_counter[i][4], 3) and data_for_counter[i][4] < 40:
            if data_for_counter[i][1] == "big":
                if data_for_counter[i][2] == "square":
                    if data_for_counter[i][3] == "yellow":
                        BYS += 1
                    if data_for_counter[i][3] == "red":
                        BRS += 1
                    if data_for_counter[i][3] == "green":
                        BGS += 1
                if data_for_counter[i][2] == "circle":
                    if data_for_counter[i][3] == "yellow":
                        BYC += 1
                    if data_for_counter[i][3] == "red":
                        BRC += 1
                    if data_for_counter[i][3] == "green":
                        BGC += 1
            if data_for_counter[i][1] == "medium":
                if data_for_counter[i][2] == "square":
                    if data_for_counter[i][3] == "yellow":
                        MYS += 1
                    if data_for_counter[i][3] == "red":
                        MRS += 1
                    if data_for_counter[i][3] == "green":
                        MGS += 1
                if data_for_counter[i][2] == "circle":
                    if data_for_counter[i][3] == "yellow":
                        MYC += 1
                    if data_for_counter[i][3] == "red":
                        MRC += 1
                    if data_for_counter[i][3] == "green":
                        MGC += 1
            if data_for_counter[i][1] == "small":
                if data_for_counter[i][2] == "square":
                    if data_for_counter[i][3] == "yellow":
                        SYS += 1
                    if data_for_counter[i][3] == "red":
                        SRS += 1
                    if data_for_counter[i][3] == "green":
                        SGS += 1
                if data_for_counter[i][2] == "circle":
                    if data_for_counter[i][3] == "yellow":
                        SYC += 1
                    if data_for_counter[i][3] == "red":
                        SRC += 1
                    if data_for_counter[i][3] == "green":
                        SGC += 1
    print(
        f'Big objects: {BYS + BYC + BGS + BGC + BRS + BRC}, including {BYS} yellow squares, {BYC} yellow circles, {BGS}'
        f' green squares, {BGC} green circles, {BRS} red squares, and {BRC} red circles.\n Medium objects: '
        f'{MYC + MYS + MGC + MGS + MRC + MRS}, including including {MYS} yellow squares, {MYC} yellow circles, {MGS}'
        f' green squares, {MGC} green circles, {MRS} red squares, and {MRC} red circles.\n Small objects: '
        f'{SYC + SYS + SGC + SGS + SRC + SRS}, including including {SYS} yellow squares, {SYC} yellow circles, {SGS}'
        f' green squares, {SGC} green circles, {SRS} red squares, and {SRC} red circles.\n')
