from memory_profiler import profile

true = True
false= False

# =============================================================================
# class StripLevelY():
#     bin=0
#     def __init__(self,y,top):
#         self.y=y
#         self.top=top
#         self.availableY
#     def fitRectangle(self,rectangle):
#         queda=self.availableY-rectangle[6]
#         if queda>=0:
#             rectangle[3]=self.top
#             self.availableY=queda
#             return True
#         else:
#             return False
#     def canFit(self,rectangle):
#         if self.availableY-rectangle[6]>=0:
#             return True
#         else:
#             return False
# =============================================================================
class StripLevel():
    bin=0
    def __init__(self,x,top,topY,bins):
        self.x=x
        self.top=top
        self.availableX=x
        self.topY=topY
        self.bins=bins
    def fitRectangle(self,rectangle):
        if rectangle[11] is False:
            queda=self.availableX-rectangle[5]
            print("puse rectangulo en " + str(self.bins))
            print("en " + str(self.availableX-rectangle[5]) + " ; " + str(self.topY)+ " ; "+ str(self.top))
            rectangle=(rectangle[0],rectangle[1],self.availableX-rectangle[5],self.topY,self.top,rectangle[5],rectangle[6],rectangle[7],rectangle[8],self.bins,2,True)
            self.availableX=queda
            print("me queda :" +str(self.availableX))
        return rectangle
    def canFit(self,rectangle):
        resta=self.availableX-rectangle[5]
        if  resta>=0:
            print("canfit")
            return True
        else:
            return False
        
class Algorithms():
    
    def calVolumen(self, arr):
        n = len(arr)
        for i in range(n):
            vol = arr[i][5]*arr[i][6]*arr[i][7]
            arr[i] = (arr[i][0],arr[i][1],arr[i][2],arr[i][3],arr[i][4],arr[i][5],arr[i][6],arr[i][7],vol,arr[i][9],arr[i][10])
        return arr
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
                if L[i][8] > R[j][8]: 
                    arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5],L[i][6],L[i][7],L[i][8],L[i][9],L[i][10]) 
                    i+=1
                else: 
                    arr[k] = (R[j][0],R[j][1],R[j][2],R[j][3],R[j][4],R[j][5],R[j][6],R[j][7],R[j][8],R[j][9],R[j][10])  
                    j+=1
                k+=1

            while i < len(L): 
                arr[k] = (L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5],L[i][6],L[i][7],L[i][8],L[i][9],L[i][10]) 
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = (R[j][0],R[j][1],R[j][2],R[j][3],R[j][4],R[j][5],R[j][6],R[j][7],R[j][8],R[j][9],R[j][10])  
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
    @profile
    def NFDH(self, arrItem, largoBin, anchBin, altoBin):
        n = len(arrItem)
        self.quicksort(arrItem, 0, n-1, 6)
        bins = 0
        y = anchBin
        z = 0
        x = 0
        larC = arrItem[0][7] ##mayor largo
    
        ########
        arrItem[0] = (arrItem[0][0], arrItem[0][1],x, y - arrItem[0][5], z, arrItem[0][5], arrItem[0][6], arrItem[0][7], 0, bins, 0)
        newEst = arrItem[0][6] ##Z
    
        for i in range(1, n):
        
            varY = arrItem[i-1][3] - arrItem[i][5]
        
            if varY >= 0: ## Si el ancho del item es mayor o igual al 0, agregar 
                arrItem[i] = (arrItem[i][0], arrItem[i][1], x, arrItem[i-1][3] - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
            
                if x + arrItem[i][7] > larC:
                    larC = arrItem[i][7]
    
        
            else:
                z = newEst ## Actualiza posicion z para un nuevo estante
                varZ = z + arrItem[i][6]
                varX = larC + arrItem[i][7]
            
                if varZ <= altoBin: ## Si el alto del item es menor o igual a altoBin, agregar
                    newEst = newEst + arrItem[i][6]
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, anchBin - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                
                    if x + arrItem[i][7] > larC:
                        larC = arrItem[i][7]
            
                elif varZ > altoBin and varX <= largoBin:
                    newEst = arrItem[i][6]
                    y = anchBin
                    z = 0
                    x = larC
                    larC = x + arrItem[i][7]
                    
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, y - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                
                    print(arrItem[i][6])
            
                else:
                    newEst = arrItem[i][6]
                    y = anchBin
                    x = 0
                    z = 0
                    bins = bins + 1
                    
                    arrItem[i] = (arrItem[i][0], arrItem[i][1], x, y - arrItem[i][5], z, arrItem[i][5], arrItem[i][6], arrItem[i][7], 0, bins, 0)
                        
        
        return arrItem, bins
    
    @profile
    def BFDH(self, rectangles, largoBin, anchBin, altoBin):
        print("llegue al bf")
        n=len(rectangles)
        topeY=0
        topeY2=0
        levels=[]
        highestY=-1
        bins=0
        topZ=0
        for i in range(0,n):         
                rectangles[i] = (rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],rectangles[i][4],rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],0,2,False)
        self.quicksort(rectangles, 0, n-1,7)
        indexOH=-1
        
        for i in range(0,n):
           d=int(rectangles[i][6])
           if d > highestY and rectangles[i][11] is False:                         
               highestY=rectangles[i][6]
               indexOH=i   
        rectangles[indexOH]=(rectangles[indexOH][0],rectangles[indexOH][1],largoBin-rectangles[indexOH][5],0,0,rectangles[indexOH][5],rectangles[indexOH][6],rectangles[indexOH][7],0,bins,0,True)
        topeY=0
        highestY=-1
        topeY2=rectangles[indexOH][6]
        
        for j in range(0,n):
               print("llegue")
               levelWithSmallestResidual=None
               for level in levels:
                   if level.canFit(rectangles[j]) and rectangles[j][11] is False:
                       print("if de can Fit")
                       if levelWithSmallestResidual is not None and levelWithSmallestResidual.availableX>level.availableX:
                           levelWithSmallestResidual=level
                       elif levelWithSmallestResidual is None:
                           levelWithSmallestResidual=level
               if levelWithSmallestResidual is None and rectangles[j][11] is False:    
                   print("entro a este if")
     
                   if topZ+rectangles[j][7]>altoBin:
                       topZ=0 
                       for i in range(0,n):
                           if rectangles[i][6]>=highestY and rectangles[i][11]==False:                         
                               highestY=rectangles[i][6]
                               indexOH=i
                       print("topey : " + str(topeY) + "mH : " + str(rectangles[indexOH][6]))
                       
                       if topeY2+rectangles[indexOH][6]> anchBin:
                            print("creo bin")
                            bins+=1
                            topeY=0
                            highestY=-1
                            rectangles[indexOH]=(rectangles[indexOH][0],rectangles[indexOH][1],largoBin-rectangles[indexOH][5],0,0,rectangles[indexOH][5],rectangles[indexOH][6],rectangles[indexOH][7],0,bins,0,True)
                            print("topey es 0")
                            topeY=0
                            topeY2=rectangles[indexOH][6]
                            topZ=0      
                       else:
                            print("topey " + str(topeY))
                        
                            rectangles[indexOH]=(rectangles[indexOH][0],rectangles[indexOH][1],largoBin-rectangles[indexOH][5],topeY+rectangles[indexOH][6],0,rectangles[indexOH][5],rectangles[indexOH][6],rectangles[indexOH][7],0,bins,0,True)                           
                            
                            topeY=topeY+rectangles[indexOH][6]
                            topeY2=topeY2+rectangles[indexOH][6]
                            print("topey " + str(topeY))
                            highestY=-1
                            topZ=0
                    
                   if topZ==0:
                       print("iftp=0")
                       levelt=StripLevel(largoBin-rectangles[indexOH][5],topZ,topeY,bins)
                   else:
                       print("elsep=0")
                       levelt=StripLevel(largoBin,topZ,topeY,bins)
                   print("topz es " + str(topZ)) 
                   print("topz es " + str(topZ))
                   rectangles[j]=levelt.fitRectangle(rectangles[j])
                   topZ+=rectangles[j][7]
                  
                   print(rectangles[j])
                   levels.append(levelt)
               elif rectangles[j][11] is False:
                   print("llenar nivel con residuo")
                   rectangles[j]=levelWithSmallestResidual.fitRectangle(rectangles[j])
        return bins

  
        
    @profile
    def Algorithm(self, rectangles, anchoC, altoC, largoC):
    
        n = len(rectangles)
        self.calVolumen(rectangles)
        self.mergeSortV(rectangles)

        x = 0
        cont = 0
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
                        if rectangles[x][3] - rectangles[i][5] > 0:    
                            rectangles[i] = (rectangles[i][0],rectangles[i][1],0,rectangles[x][3] - rectangles[i][5],0,rectangles[i][5],rectangles[i][7],rectangles[i][6],rectangles[i][8],cont,2)
                            base = i
                            x = i
                        else:
                            print("cambia :c")
                            cont += 1
                            rectangles[i] = (rectangles[i][0],rectangles[i][1],0,anchoC - rectangles[i][5],0,rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],cont,2)
                        
            else:
                rectangles[i] = (rectangles[i][0],rectangles[i][1],0,anchoC - rectangles[i][5],0,rectangles[i][5],rectangles[i][6],rectangles[i][7],rectangles[i][8],cont,2)
