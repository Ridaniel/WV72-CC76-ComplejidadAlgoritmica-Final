import sys
from Algorithms import Algorithms
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from PyQt5 import uic,QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
import timeit

qtCreatorFile = "MyForm.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

filename = ""
filename2 =""
rectangles = []
cantRectangles = 0
contain = []
class Files():
    def readFile(self,ruta):
        global rectangles
        global cantRectangles
        global contain
        f = open(ruta, "r")
        count = 0
        arr = []
        container = None
        n = 0
        for line in f.readlines():
            l = line.split()
            if count == 0:
                container = list(map(int,l))
                count +=1
                continue
            if count == 1:
                n = int(line[0])
                count +=1
                continue
            arrAux = []
            for i in range(len(l)):
                if i == 1:
                    arrAux.append(l[i])
                else:
                    arrAux.append(int(l[i]))
            arr.append((arrAux[0],arrAux[1],0,0,0,arrAux[2],arrAux[4],arrAux[3],arrAux[2]*arrAux[3]*arrAux[4],0,0))
            count +=1
        rectangles = arr
        cantRectangles = n
        contain = container
        f.close()
    def writeGenerator(self,ruta):
        f = open(ruta,"w")
        largo = random.randint(200, 300)
        ancho = random.randint(200, 300)
        alto = random.randint(200, 300)
        
        while ancho > alto or alto > largo:
           largo = random.randint(200, 300)
           ancho = random.randint(200, 300)
           alto = random.randint(200, 300)
        
        n = random.randint(30,50)
        
        f.write(str(ancho)+" "+str(alto)+" "+str(largo)+'\n')
        f.write(str(n)+"\n")
        
        idOne = 65
        for i in range(n):
        
           count = random.randint(1,5)
           id =  chr(idOne)
           ancho = random.randint(20,50)
           alto = random.randint(20,50)
           largo = random.randint(20,50)
           while ancho > alto or alto > largo:
              alto = random.randint(20,50)
              largo = random.randint(20,50)
           idOne+=1
           f.write(str(count)+" "+id+" "+str(ancho)+" "+str(alto)+" "+str(largo)+'\n')
        f.close()  
    def writeResult(self, rectangles):
        
        n = len(rectangles)
        containersU = rectangles[n-1][9]
        volumenT = 2000
        volumenO = 1000
        voluemenD = volumenT- volumenO
        
        f = open("result.txt","w")
        f.write("Contenedores usados:  "+str(containersU)+"\n")
        f.write("Volumen disponible:  "+str(voluemenD)+"m3"+"\n")
        f.write("Volumen Ocupado:  " + str(volumenO)+"m3 - ("+ str((volumenO/volumenT)*100)+"%)"+"\n")
        f.write("Cajas a transportar:  "+str(n)+"\n")
        f.write("\tContenedor\t\tFormato\t\tCoordenadas\t\tOrientacion "+"\n")
        
        for i in rectangles:
            f.write("\t"+str(i[9])+"\t\t\t"+i[1]+"\t\t("+str(i[2])+","+str(i[3])+","+str(i[4])+") \t\t"+ str(i[10])+"\n")
        
        f.close()         
       
class MyApp(QtWidgets.QMainWindow ,Ui_MainWindow):
    
    def __init__(self):
        Tk().withdraw()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.frame_2.hide()
        self.frame_3.hide()
        #Push and Delete item
        self.pushButton_6.clicked.connect(self.addItem)
        self.pushButton_5.clicked.connect(self.deleteItem)
        #Change Page
        self.pushButton.clicked.connect(self.changePagePrincipal)
        self.pushButton_2.clicked.connect(self.changePageArchivos)
        self.pushButton_4.clicked.connect(self.changePageAlumnos)
        self.pushButton_8.clicked.connect(self.searchWriteRuta)
        self.pushButton_9.clicked.connect(self.searchReadRuta)
        #Read File
        self.pushButton_11.clicked.connect(self.readRuta)
        #Write File
        self.pushButton_10.clicked.connect(self.writeRuta)
        #clearPage
        self.pushButton_12.clicked.connect(self.clear)
        #Graphic
        self.pushButton_13.clicked.connect(self.graph3D)
        self.pushButton_7.clicked.connect(self.graph3DFile)
        
        #ArrItems
        self.arrItem = []
        self.curr_pos = 0
        
    def addItem(self):
        self.listWidget.addItem(self.lineEdit_6.text()+" - "+self.lineEdit_5.text()+" - "+self.lineEdit_7.text()+" - "+self.lineEdit_8.text()+" - "+self.lineEdit_9.text())
        
        self.cantT = int(self.lineEdit_4.text())
        self.tupItem = (0,'id',0,0,0,0,0,0,0,0,0)
        self.cantI = int(self.lineEdit_6.text())
        self.n = len(self.arrItem)
        self.altBin = int(self.lineEdit_2.text())
        self.anchBin = int(self.lineEdit.text())
        self.larBin = int(self.lineEdit_3.text())
        
        for i in range(self.cantI):
            
            self.form = self.lineEdit_5.text()
            self.anch = int(self.lineEdit_7.text())
            self.alt = int(self.lineEdit_8.text())
            self.larg = int(self.lineEdit_9.text())
                
            self.tupItem = (1, self.form, 0, 0, 0, self.anch, self.alt, self.larg, 0, 0, 0)
            self.arrItem.append(self.tupItem)
            print(self.arrItem)
        
        
        print(self.comboBox.currentText())
    
        
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        
    def deleteItem(self):
        items = self.listWidget.selectedItems()
        self.listWidget.takeItem(self.listWidget.row(items[0]))
        
    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.listWidget.clear()
        
    def changePagePrincipal(self):
        self.frame.show()
        self.frame_2.hide()  
        self.frame_3.hide()
        
    def changePageArchivos(self):
        self.frame_2.show()
        self.frame.hide()  
        self.frame_3.hide()
        
    def changePageAlumnos(self):
        self.frame_3.show()
        self.frame.hide()  
        self.frame_2.hide()
        
    def searchWriteRuta(self):
        global filename
        filename = askopenfilename()
        self.lineEdit_10.setText(filename)
    def searchReadRuta(self):
        global filename2
        filename2 = askopenfilename()
        self.lineEdit_11.setText(filename2)
    def writeRuta(self):
        global filename
        file = Files()
        file.writeGenerator(filename)
        self.lineEdit_10.setText("")
        
    def readRuta(self):
        global filename2
        global rectangles
        file = Files()
        file.readFile(filename2)
        self.lineEdit_11.setText("")
        print(rectangles)
    
    def graph3D(self):
        global rectangles
        
        alg = Algorithms()

        if self.comboBox.currentText() == "NFDH":
            
            start = timeit.default_timer()
            self.arrItem, bins = alg.NFDH(self.arrItem, self.larBin, self.anchBin, self.altBin)
            stop = timeit.default_timer()
            execution_time = stop - start

            print("Program Executed in "+str(execution_time)) #It returns time in sec
            
        elif self.comboBox.currentText() == "Algorithm":
            start = timeit.default_timer()
            alg.Algorithm(self.arrItem, self.anchBin, self.altBin, self.larBin)
            stop = timeit.default_timer()
            execution_time = stop - start

            print("Program Executed in "+str(execution_time)) #It returns time in sec
        else:
            print("En proceso")
            
        print(self.arrItem)
        
        nBin = self.arrItem[len(self.arrItem) - 1][9]
        
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')
        
        plots = [(0, 0, 0, 0, 0, 0)] * (nBin+1)
         
        for i in range(nBin+1):
            x = []
            y = []
            z = []
        
            dx = []
            dy = []
            dz = []
        
            for j in range(len(self.arrItem)):
                if self.arrItem[j][9] == i:
                    x.append(self.arrItem[j][2])
                    y.append(self.arrItem[j][3])
                    z.append(self.arrItem[j][4])
            
                    dx.append(self.arrItem[j][7])
                    dy.append(self.arrItem[j][5])
                    dz.append(self.arrItem[j][6])
            
            
            plots[i] = (x, y, z, dx, dy, dz)
        
        print("ss ",plots)
        
        def key_event(e):

            if e.key == "right":
                self.curr_pos = self.curr_pos + 1
            elif e.key == "left":
                self.curr_pos = self.curr_pos - 1
            else:
                return
            self.curr_pos = self.curr_pos % len(plots)

            ax1.cla()
            ax1.bar3d(plots[self.curr_pos][0],plots[self.curr_pos][1],plots[self.curr_pos][2],plots[self.curr_pos][3],plots[self.curr_pos][4],plots[self.curr_pos][5])
            print(self.curr_pos)
            fig.canvas.draw()
        file = Files()
        file.writeResult(self.arrItem)
        
        fig.canvas.mpl_connect('key_press_event', key_event)
        ax1.bar3d(x, y, z, dx, dy, dz)
        plt.show()
    
    def graph3DFile(self):
        alg = Algorithms()
        global rectangles
        global contain
        
        if self.comboBox_2.currentText() == "NFDH":
            rectangles, bins = alg.NFDH(rectangles, contain[1], contain[0], contain[2])
            print("NFDH")
        elif self.comboBox_2.currentText() == "Algorithm":
            alg.Algorithm(rectangles, contain[0], contain[1], contain[2])
        else:
            print("En proceso")
        
        nBin = rectangles[len(rectangles) - 1][9]
        
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')
        
        plots = [(0, 0, 0, 0, 0, 0)] * (nBin+1)
         
        for i in range(nBin+1):
            x = []
            y = []
            z = []
        
            dx = []
            dy = []
            dz = []
        
            for j in range(len(rectangles)):
                if rectangles[j][9] == i:
                    x.append(rectangles[j][2])
                    y.append(rectangles[j][3])
                    z.append(rectangles[j][4])
            
                    dx.append(rectangles[j][7])
                    dy.append(rectangles[j][5])
                    dz.append(rectangles[j][6])
            
            
            plots[i] = (x, y, z, dx, dy, dz)
        
        print("ss ",plots)
        
        def key_event(e):

            if e.key == "right":
                self.curr_pos = self.curr_pos + 1
            elif e.key == "left":
                self.curr_pos = self.curr_pos - 1
            else:
                return
            self.curr_pos = self.curr_pos % len(plots)

            ax1.cla()
            ax1.bar3d(plots[self.curr_pos][0],plots[self.curr_pos][1],plots[self.curr_pos][2],plots[self.curr_pos][3],plots[self.curr_pos][4],plots[self.curr_pos][5])

            fig.canvas.draw()
        
        file = Files()
        file.writeResult(rectangles)
        
        fig.canvas.mpl_connect('key_press_event', key_event)
        ax1.bar3d(x, y, z, dx, dy, dz)
        plt.show()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


