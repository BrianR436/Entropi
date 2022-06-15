from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox, QTableWidget, QTableWidgetItem
from Interfaz.Entropia import Ui_MainWindow
from collections import Counter
from math import log2
import sys
import io
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ejecutar.clicked.connect(self.extraer_ruta)#Se ejecuta el metodo "extraer_ruta"
       
    def extraer_ruta(self):
        try:
            RUTA = self.ruta.text()
            archivo = io.open(RUTA,mode='r',encoding="utf-8")
            print(archivo.read())
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No se encontro ningun archivo de texto .TXT")
            msg.setWindowTitle("ERROR")
            msg.exec()
        self.calcular_probabilidad(RUTA)
    def calcular_probabilidad(self, RUTA):
        archivo = io.open(RUTA, mode='r', encoding="utf-8")
        texto = archivo.read()
        t = texto.splitlines()
        t1 = len(t)-1
        sinsaltos = len(texto)
        numero_caracteres = sinsaltos-t1#sacamos la longitud del archivo de texto
        
        numero = str(numero_caracteres)#convertimos a string el numero de caracteres para poder ponerlo en la tabla
        contador = Counter(texto)#para saber cuantas veces aparece cada caracter se almacena en un diccionario
        if(t1>0):
            contador.pop('\n')#eliminamos los saltos de linea
          # contador.pop(' ')  
        print(contador)   
        nuevo_contador = len(contador)
        texto1 = QTableWidgetItem('Archivo de texto')
        self.tableWidget.setItem(0,0,texto1)#ponemos el texto Archivo de texto en la fila 0 columna 0
        texto2 = QTableWidgetItem(numero)
        self.tableWidget.setItem(3,0,texto2)#ponemos el valor de numero de caracteres en fila 3 columna 0
        
        caracter = []#aqui se van a almacenar los caracteres
        concurrencia = []#se almacena las veces que aparecen
        Probabilidad_letra = [] 
        informacion = []
        entropia = []
        H_S= 0
        longitud_media = 0
        informacion_total = 0 
        for termino,valor in contador.items():
            nuevo_termino = termino
            caracter.append(nuevo_termino)#se agrega el caracter
            nuevo_valor = valor
            concurrencia.append(nuevo_valor)#se agrega el numero
            print(termino, valor)

        for i in range(int(nuevo_contador)):
            informacion.append(log2(numero_caracteres/concurrencia[i]))#saco la informacion de cada letra
            Probabilidad_letra.append(concurrencia[i]/numero_caracteres)#saco la probabilidad de cada caracter
            entropia.append((Probabilidad_letra[i])*(log2(numero_caracteres/concurrencia[i])))
            H_S = entropia[i]+H_S 
            informacion_total = informacion[i]+informacion_total
            longitud_media = longitud_media+Probabilidad_letra[i]*concurrencia[i] 
        self.calcular_eficiencia_redundancia(H_S,longitud_media)
        Probabilidad={}
        Probabilidad = dict(zip(caracter,Probabilidad_letra))#anexo a un diccionario el caracter y su probabilidad
        p_cada_letra = str(Probabilidad)#convierto a string para poder ponerlo en la tabla
        texto3 = QTableWidgetItem(p_cada_letra)
        self.tableWidget.setItem(1,0,texto3)
        informacion_cada_letra = {}
        informacion_cada_letra = dict(zip(caracter, informacion))#anexo a un diccionario el caracter y su informacion
        i_c_l = str(informacion_cada_letra)
        texto4 = QTableWidgetItem(i_c_l)
        self.tableWidget.setItem(2,0,texto4)
        h_s=str(H_S)
        texto5 = QTableWidgetItem(h_s)
        self.tableWidget.setItem(4,0,texto5)
        i_total=str(informacion_total)
        texto6 = QTableWidgetItem(i_total)
        self.tableWidget.setItem(5,0,texto6)
        
    def calcular_eficiencia_redundancia(self,Entropia,L):
        Eficiencia = (Entropia/L)*100
        n=str(Eficiencia)
        texto7 = QTableWidgetItem(n)
        self.tableWidget.setItem(7,0,texto7)
        redundancia = 1-Eficiencia/100
        P=str(redundancia)
        texto7 = QTableWidgetItem(P)
        self.tableWidget.setItem(6,0,texto7)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())