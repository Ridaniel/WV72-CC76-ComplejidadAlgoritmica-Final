class Algorithms():
    
    def partition(self, arr, ini, fin, pos):
        i = ini - 1
        pivote = arr[fin][pos]
    
        for j in range(ini,fin):
            if arr[j][pos] > pivote:
                i = i + 1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[fin] = arr[fin],arr[i+1]
        return i+1
    
    def quicksort(self, arr, ini, fin, pos):
    
        if ini < fin:
            pi = self.partition(arr, ini, fin, pos)
        
            self.quicksort(arr, ini, pi-1, pos)
            self.quicksort(arr, pi+1, fin, pos)
    
    def NFDH(self, arrItem, largoBin, anchBin, altoBin):
        n = len(arrItem)
        self.quicksort(arrItem, 0, n-1, 7)
        bins = 0
        y = anchBin
        z = 0
        x = 0
        larC = arrItem[0][6] ##mayor largo
    
        ########
        arrItem[0] = (arrItem[0][0], arrItem[0][1], x, y - arrItem[0][5], z, arrItem[0][5], arrItem[0][6], arrItem[0][7], 0, bins, 0)
        newEst = arrItem[0][7] ##Z
    
        for i in range(1, n):
        
            varY = arrItem[i-1][3] - arrItem[i][5]
        
            if varY >= 0: ## Si el ancho del item es mayor o igual al 0, agregar 
                arrItem[i] = (arrItem[i][0], arrItem[i][1], x, arrItem[i-1][3] - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
            
                if x + arrItem[i][6] > larC:
                    larC = arrItem[i][6]
    
        
            else:
                z = newEst ## Actualiza posicion z para un nuevo estante
                varZ = z + arrItem[i][7]
                varX = larC + arrItem[i][6]
            
                if varZ <= altoBin: ## Si el alto del item es menor o igual a altoBin, agregar
                    newEst = newEst + arrItem[i][7]
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, anchBin - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                
                    if x + arrItem[i][6] > larC:
                        larC = arrItem[i][6]
            
                elif varZ > altoBin and varX <= largoBin:
                    newEst = arrItem[i][7]
                    y = anchBin
                    z = 0
                    x = larC
                    larC = x + arrItem[i][6]
                    
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, y - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                
                    print(arrItem[i][7])
            
                else:
                    newEst = arrItem[i][7]
                    y = anchBin
                    x = 0
                    z = 0
                    bins = bins + 1
                    
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, y - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                        
        
        return arrItem, bins