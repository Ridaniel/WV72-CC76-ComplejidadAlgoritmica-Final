
def nfdhSPP(arrItem, largoBin, anchBin, altoBin):
    n = len(arrItem)
    quicksort(arrItem, 0, n-1, 2)
    bins = 0
    y = anchBin
    z = 0
    x = 0
    larC = arrItem[0][0] ##mayor largo
    
    ########
    arrItem[0] = (arrItem[0][0], arrItem[0][1], arrItem[0][2], x, y - arrItem[0][1], z, bins)
    newEst = arrItem[0][2] ##Z
    
    for i in range(1, n):
        
        varY = arrItem[i-1][4] - arrItem[i][1]
        
        if varY >= 0: ## Si el ancho del item es mayor o igual al 0, agregar 
            arrItem[i] = (arrItem[i][0], arrItem[i][1], arrItem[i][2], x, arrItem[i-1][4] - arrItem[i][1], z, bins)
            
            if x + arrItem[i][0] > larC:
                larC = arrItem[i][0]
    
        
        else:
            z = newEst ## Actualiza posicion z para un nuevo estante
            varZ = z + arrItem[i][2]
            varX = larC + arrItem[i][0]
            
            if varZ <= altoBin: ## Si el alto del item es menor o igual a altoBin, agregar
                newEst = newEst + arrItem[i][2]
                arrItem[i] = (arrItem[i][0], arrItem[i][1], arrItem[i][2], x, anchBin - arrItem[i][1], z, bins)
                
                if x + arrItem[i][0] > larC:
                    larC = arrItem[i][0]
            
            elif varZ > altoBin and varX <= largoBin:
                newEst = arrItem[i][5]
                y = anchBin
                z = 0
                x = larC
                larC = x + arrItem[i][0]
                
                arrItem[i] = (arrItem[i][0], arrItem[i][1], arrItem[i][2], x, y - arrItem[i][1], z, bins)
                
                print(arrItem[i][2])
            
            else:
                newEst = arrItem[i][5]
                y = anchBin
                x = 0
                z = 0
                bins = bins + 1
                
                arrItem[i] = (arrItem[i][0], arrItem[i][1], arrItem[i][2], x, y - arrItem[i][1], z, bins)
                        
        
    return arrItem, bins




