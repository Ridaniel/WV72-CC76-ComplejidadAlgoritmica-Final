class Algorithms():
    
    def calVolumen(self, arr):
        n = len(arr)
        for i in range(n):
            vol = arr[i][5]*arr[i][6]*arr[i][7]
            arr[i] = (arr[i][0],arr[i][1],arr[i][2],arr[i][3],arr[i][4],arr[i][5],arr[i][6],arr[i][7],vol,arr[i][9],arr[i][10])
    
    def mergeSort(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 
            L = arr[:mid] 
            R = arr[mid:] 
        
            self.mergeSort(L) 
            self.mergeSort(R) 
  
            i = j = k = 0
          
            while i < len(L) and j < len(R): 
                if L[i][2] < R[j][2]: 
                    arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3]) 
                    i+=1
                else: 
                    arr[k] = (R[j][0],R[j][1],R[j][2],R[j][3]) 
                    j+=1
                    k+=1

            while i < len(L): 
                arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3])
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = (R[j][0],R[j][1],R[j][2],R[j][3]) 
                j+=1
                k+=1
    
    def mergeSortV(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 
            L = arr[:mid] 
            R = arr[mid:] 
        
            self.mergeSortV(L) 
            self.mergeSortV(R) 
  
            i = j = k = 0
          
            while i < len(L) and j < len(R): 
                if L[i][8] < R[j][8]: 
                    arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5],L[i][6],L[i][7],L[i][8],L[i][9],L[i][10]) 
                    i+=1
                else: 
                    arr[k] = (R[i][0],R[i][1],R[i][2],R[i][3],R[i][4],R[i][5],R[i][6],R[i][7],R[i][8],R[i][9],R[i][10])  
                    j+=1
                k+=1

            while i < len(L): 
                arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5],L[i][6],L[i][7],L[i][8],L[i][9],L[i][10]) 
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = (R[i][0],R[i][1],R[i][2],R[i][3],R[i][4],R[i][5],R[i][6],R[i][7],R[i][8],R[i][9],R[i][10])  
                j+=1
                k+=1
    
    def CalMax(self, arr):
        return arr.index(max(arr[0],arr[1],arr[2]))
    
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
    
    def Algorithm(self, rectangles, anchoC, altoC, largoC):
    
        n = len(rectangles)
        self.calVolumen(rectangles)
        self.mergeSortV(rectangles)

        x = 0
        cont = 1
        base = 0
    
        for i in range(n):
        
            if rectangles[i][7] > rectangles[i][5] and rectangles[i][6] >= rectangles[i][5]:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][6],rectangles[i][5],rectangles[i][7],rectangles[i][8],cont,2)
            elif rectangles[i][6] > rectangles[i][7] and rectangles[i][7] <= rectangles[i][5]:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],cont,2)
            elif rectangles[i][6] > rectangles[i][7] and rectangles[i][7] >= rectangles[i][5]:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][7],rectangles[i][5],rectangles[i][6],rectangles[i][8],cont,2)
            elif rectangles[i][5] > rectangles[i][7] and rectangles[i][7] >= rectangles[i][6]:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][7],rectangles[i][6],rectangles[i][5],rectangles[i][8],cont,2)
            else:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][6],rectangles[i][7],rectangles[i][5],rectangles[i][8],cont,2)
        
            if i != 0:
                if rectangles[i-1][4] + rectangles[i-1][6] + rectangles[i][6] <= altoC:
                    rectangles[i] =  (rectangles[i][0],rectangles[i][1],rectangles[i-1][2],anchoC - rectangles[i][5],rectangles[i-1][4]+rectangles[i-1][6],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],cont,2)
                else:
                    if rectangles[base][2]+rectangles[base][7] + rectangles[i][7] <= largoC:
                        rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[base][2]+rectangles[base][7],anchoC - rectangles[i][5],rectangles[base][4],rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],cont,2)
                        base = i
                    else:
                        if rectangles[x][3] - rectangles[i][5] <= anchoC:    
                            rectangles[i] = (rectangles[i][0],rectangles[i][1],0,rectangles[x][3] - rectangles[i][5],0,rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],cont,2)
                            base = i
                            x = i
                        else:
                            cont +=1
                            rectangles[i] = (rectangles[i][0],rectangles[i][1],0,anchoC - rectangles[i][5],0,rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],cont,2)
                        
            else:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],0,anchoC - rectangles[i][5],0,rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],cont,2)
