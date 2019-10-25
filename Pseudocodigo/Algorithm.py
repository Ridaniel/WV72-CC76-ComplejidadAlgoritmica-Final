from MergeSortVolumen import mergeSortV 
from CalVolumen import calVolumen 


def Algorithm(rectangles,anchoC,altoC,largoC):
    
    n = len(rectangles)
    calVolumen(rectangles)
    mergeSortV(rectangles)
    x = 0
    base = 0
    
    for i in range(n):
        
        if rectangles[i][7] > rectangles[i][5] and rectangles[i][6] >= rectangles[i][5]:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][6],rectangles[i][5],rectangles[i][7],rectangles[i][8],rectangles[i][9],2)
        elif rectangles[i][6] > rectangles[i][7] and rectangles[i][7] <= rectangles[i][5]:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],rectangles[i][9],2)
        elif rectangles[i][6] > rectangles[i][7] and rectangles[i][7] >= rectangles[i][5]:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][7],rectangles[i][5],rectangles[i][6],rectangles[i][8],rectangles[i][9],2)
        elif rectangles[i][5] > rectangles[i][7] and rectangles[i][7] >= rectangles[i][6]:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][7],rectangles[i][6],rectangles[i][5],rectangles[i][8],rectangles[i][9],2)
        else:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][6],rectangles[i][7],rectangles[i][5],rectangles[i][8],rectangles[i][9],2)
        
        if i != 0:
            if rectangles[i-1][4] + rectangles[i-1][6] + rectangles[i][6] <= altoC:
                rectangles[i] =  (rectangles[i][0],rectangles[i][1],rectangles[i-1][2],anchoC - rectangles[i][5],rectangles[i-1][4]+rectangles[i-1][6],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],rectangles[i][9],2)
            else:
                if rectangles[base][2]+rectangles[base][7] + rectangles[i][7] <= largoC:
                    rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[base][2]+rectangles[base][7],anchoC - rectangles[i][5],rectangles[base][4],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],rectangles[i][9],2)
                    base = i
                else:
                    if rectangles[x][3] - rectangles[i][5] <= anchoC:    
                        rectangles[i] = (rectangles[i][0],rectangles[i][1],0,rectangles[x][3] - rectangles[i][5],0,rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],rectangles[i][9],2)
                        base = i
                        x = i
                    else:
                        print("Se ha salido del contenedor")
                        break
        else:
            rectangles[i] = (rectangles[i][0],rectangles[i][1],0,anchoC - rectangle[i][5],0,rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],rectangles[i][9],2)




