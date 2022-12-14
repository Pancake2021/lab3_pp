from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QRadioButton, QMessageBox
from typing import Optional, Union

from Task1 import run1
from Task2 import run2
from Task3 import run3
from Task5 import *


class Ui_MainWindow(QWidget):
    '''main window class'''
    def setupUi(self, MainWindow)  -> Union[str, None]:
        '''I am creating a general (main) window in which we will work'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.dir = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 301, 32))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 100, 301, 32))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 10, 301, 32))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 190, 301, 32))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 140, 301, 32))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow)  -> Union[str, None]:
        '''function used to connect buttons'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Tsk1"))
        self.pushButton_2.setText(_translate("MainWindow", "Tsk2"))
        self.pushButton_3.setText(_translate("MainWindow", "Open dir"))
        self.pushButton_4.setText(_translate("MainWindow", "photo iterator"))
        self.pushButton_5.setText(_translate("MainWindow", "Tsk3"))

        self.pushButton_3.clicked.connect(self.get_my_folder)
        self.pushButton.clicked.connect(self.Task1)
        self.pushButton_2.clicked.connect(self.Task2)
        self.pushButton_5.clicked.connect(self.Task3)
        self.pushButton_4.clicked.connect(self.secondwind)

    def get_my_folder(self) -> Union[str, None]:
        '''getting a folder with a dateset'''
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "?????????? ????????????????")
        os.chdir(self.dir)
        print(self.dir)

    def Task1(self)  -> Union[str, None]:
        '''completing 1 task'''
        run1(self.dir, 'cat', 'annotationCat')
        run1(self.dir, 'dog', 'annotationDog')

    def Task2(self) -> Union[str, None]:
        '''completing 2 task'''
        run2(self.dir, "datasetcopy", "AnnotationTask2")

    def Task3(self) -> Union[str, None]:
        '''completing 3 task'''
        run3(self.dir, "AnnotationTask3", 'datasetcopy1')

    def secondwind(self) -> Union[str, None]:
        '''switching for the next window'''
        wind = secondwindow(self)
        wind.exec()


class secondwindow(QtWidgets.QDialog):
    '''the class of the second working window'''
    def __init__(self, parent=None)-> Union[str, None]:
        '''function for operation of the second window and generation of the second window'''
        super(secondwindow, self).__init__(parent)
        self._iterator = IteratorTask5("/Users/glebpankeev/Desktop/lab3_pp", "cat", "dataset")
        self._pixelmap = QPixmap('.jpg')
        self.resize(400, 400)
        self.verticalLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(200, 400, 100, 50))
        self.verticalLayout.setSpacing(10)
        self.setLayout(self.verticalLayout)
        self.setGeometry(200, 200, 200, 200)

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setGeometry(QtCore.QRect(200, 100, 100, 20))

        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("ImgTsk")
        self.pushButton.setText("Next")
        self.pushButton.clicked.connect(self.nextButt)
        self.pushButton_1.setText("Close")
        self.pushButton_1.clicked.connect(self.buttClose)
        self.verticalLayout.addWidget(self.pushButton_1)

        pix = QPixmap("/Users/glebpankeev/Desktop/lab3_pp/dataset/cat/0000.jpg").scaledToWidth(400).scaledToHeight(400)
        self._lable = QLabel(self)

        self._lable.setPixmap(pix)

        self.verticalLayout.addWidget(self._lable)

        self.radio_button_1 = QRadioButton('cat')
        self.radio_button_1.setChecked(True)
        self.radio_button_1.setAccessibleName("cat")

        self.radio_button_2 = QRadioButton('dog')
        self.radio_button_2.setAccessibleName("dog")

        self.verticalLayout.addWidget(self.radio_button_1)
        self.verticalLayout.addWidget(self.radio_button_2)
        self.radio_button_1.clicked.connect(self.buttonClick)
        self.radio_button_2.clicked.connect(self.buttonClick)

    def buttonClick(self) -> Union[str, None]:
        ''''radio' button for switching between dataset categories'''
        send = self.sender()
        if send.text() == 'cat':
            self._iterator.setclassName(send.text())
            self._iterator.getclassName()
        elif send.text() == 'dog':
            self._iterator.setclassName(send.text())
            self._iterator.getclassName()

    def nextButt(self, )  -> Union[str, None]:
        '''functionality of the button to switch between images'''
        try:
            tmp = os.path.join(os.path.join(self._iterator.dataset, self._iterator.pathdir, self._iterator.classname),
                               self._iterator.__next__())
            print(tmp)
            self._pixelmap = QPixmap(f"{tmp}").scaledToWidth(400).scaledToHeight(400)
            self._lable.setPixmap(self._pixelmap)
            print(tmp)
        except:
            reply = QMessageBox.question(self, 'End img',
                                         "null", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self._iterator.clear()
            print("!!!ERR!!!")

    def buttClose(self) -> Union[str, None]:
        '''close button functionality'''
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
