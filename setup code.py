# Was geht ab bitches

import math
from copy import copy

fobj = open("dc.in").read()
data = []
data2 = []
data3 = []

data = fobj.split("\n")

for x in data:
    data2.append(x.split(" "))

for x in data2:
    for y in x:
        data3.append((y))

data = copy(data3)

R = int(data[0]) #
data.pop(0)

C = int(data[0])#
data.pop(0)

A = int(data[0]) #
data.pop(0)

L = int(data[0]) #
data.pop(0)

V = int(data[0]) #
data.pop(0)

B = int(data[0]) #
data.pop(0)

T = int(data[0]) #
data.pop(0)

start_point = (int(data[0]), int(data[1])) #
data.pop(0)
data.pop(0)



print("Rows (R):", R)
print("Cols (C):", C)
print("Altitudes (A):", A)
print("Number of Target Cells (L)", L)
print("Coverage Radius (V)", V)
print("available Balloons (B)", B)
print("Turns in Sim (T)", T)
print("Start Point:", start_point)


target_cells = [] #

n = 0
while n < int(L):
    target_cells.append(copy((int(data[0]), int(data[1]))))
    data.pop(0)
    data.pop(0)

    n += 1

# Target Cells[Targes Cell][0 = X koord, 1 = Y koord]

Map = []

f = open("Map_View.txt","w+")
w = open("Map_Var.txt", "w+")

for x in range(0, 75):
    Map_I = []
    Map_T = []
    for y in range(0, 300):
        if (x, y) in target_cells:
            Map_I.append("1")
            Map_T.append("X")
        else:
            Map_I.append("0")
            Map_T.append(" ")
            
    f.write(' '.join(Map_T))
    f.write("\n")

    w.write(' '.join(Map_I))
    w.write("\n")

    
    Map.append(copy(Map_I))


f.close()
w.close()


def kord_to_arrow(x):
    x = (int(x[0]), int(x[1]))
    if x[0] == 0:
        if x[1] >= 0:
            return "↑"
        else:
            return "↓"
    elif x[1] == 0:
        if x[0] >= 0:
            return "→"
        else:
            return "←"
    else:
        if x[0] >= 0 and x[1] >= 0:
            return "↗"
        elif x[0] >= 0 and x[1] <= 0:
            return "↘"
        elif x[0] <= 0 and x[1] <= 0:
            return "↙"
        elif x[0] <= 0 and x[1] >= 0:
            return "↖"
        
wind_grid = []

k = 0



while k < A:
    
    f = open(str(k),"w+", encoding="utf-8")
    
    l = 0
    wind_level = []
    while l < R:
        m = 0
        wind_row = []
        wind_row_arr = []
        while m < C:
            wind_vektor = (data[0], data[1])
            data.pop(0)
            data.pop(0)
            wind_row.append(copy(wind_vektor))
            wind_row_arr.append(copy(kord_to_arrow(wind_vektor)))
            m += 1
        wind_level.append(wind_row)
        f.write(' '.join(wind_row_arr))
        f.write("\n")
        l += 1
    wind_grid.append(wind_level)
    f.close()
    k += 1



        


############### Data Slpited ##########################

'''
Rows (R)
Cols (C)
Altitudes (A)
Number of Target Cells (L)
Coverage Radius (V)
available Balloons (B)
Turns in Sim (T)

Target Cells[Targes Cell][0 = X koord, 1 = Y koord]
Map[Rows][Cols] 0 = no Target; 1 = Target Cell

Wind Grid = [Amplitude][Rows][Cols]

'''
















############## Balloon Pfad #########################

''' Benötigte Funktion
-Ballon erschaffen # 
-Ballon bewegen
-Ballon kaputt
-Abstand von Ballons berechnen # 
-Target points gucken ob getroffen # 
'''


def coverage(t, b):
    #t target cell; b Balloon

    if (t[0] - b[0]) ** 2 + (columndist(t[1], b[1]) ** 2) <= V ** 2:
        return True
    else:
        return False

def columndist(c1, c2):
    return min(abs(c1 - c2), C - abs((c1 - c2)))

def balloon_dist(b1, b2):
    return math.sqrt((b1[0] - b2[0]) ** 2 + (columndist(b1[1], b2[1]) ** 2))


def ballon():
    # (X-Koord, Y-Koord, Höhe, target cells)
    return (start_point[0], start_point[1], 0, 0)

ballons = []

for x in range(0, B):
    ballons.append(copy(ballon()))

'''Ballon bewegung
-Kontinente ausmachen
-Ballon zum Kontinent steuern
-Im Kontinent halten

'''












    
    
    









    





                         
    



