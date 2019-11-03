import sys
from PyQt5 import uic,QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random

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
            arr.append((arrAux[0],arrAux[1],0,0,0,arrAux[2],arrAux[3],arrAux[4],arrAux[2]*arrAux[3]*arrAux[4],0,0))
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
        
        n = random.randint(1,10)
        
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
        
    def addItem(self):
        self.listWidget.addItem(self.lineEdit_6.text()+" - "+self.lineEdit_5.text()+" - "+self.lineEdit_7.text()+" - "+self.lineEdit_8.text()+" - "+self.lineEdit_9.text())
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
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


