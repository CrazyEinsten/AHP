import numpy as np
from numpy import linalg as LA
import xlrd

RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45]
judge = 0.1

def AHP():
    datas = xlrd.open_workbook('datas.xlsx')
    tables = datas.sheets()[0]
    firstrow = np.array(tables.row_values(0)[:])
    rows = firstrow.shape
    matrix_1 = []
    for i in range(rows[0]):
        matrix_1.append(tables.row_values(i)[:])
    matrix_1 = np.array(matrix_1)
    mid1, mid2 = LA.eig(matrix_1)
    Maxindex = np.argmax(mid1, axis=0)
    aim = mid2[:][Maxindex]
    print(aim, mid1, mid2)
    buttonNum = np.max(aim) - np.min(aim)
    indx = aim.shape
    for i in range(indx[0]):
        aim[i] /= buttonNum
    nextrow = np.array(tables.row_values(rows[0])[:])
    rows_2 = nextrow.shape
    allNum = aim.shape
    secondindx = np.array(rows[0])
    for i in range(allNum[0]):
        secondmatrix = []
        for j in range(rows_2[0]):
            secondmatrix.append(tables.row_values(secondindx+j)[:])
        secondmatrix = np.array(secondmatrix)
        mid3, mid4 = LA.eig(secondmatrix)
        Maxindex_2 = np.argmax(mid3, axis=0)
        aim_2 = mid4[:][Maxindex_2]
        buttonNum_2 = np.max(aim_2) - np.min(aim_2)
        for j in range(rows_2[0]):
            aim_2 /= buttonNum_2
        secondindx += np.array(rows_2[0])


if __name__ == '__main__':
    AHP()
