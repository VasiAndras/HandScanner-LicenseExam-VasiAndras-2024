from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Hand scanner")
        MainWindow.resize(800, 480)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainPage_ProgramName = QtWidgets.QLabel(self.centralwidget)
        self.MainPage_ProgramName.setEnabled(True)
        self.MainPage_ProgramName.setGeometry(QtCore.QRect(200, 50, 421, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.MainPage_ProgramName.setFont(font)
        self.MainPage_ProgramName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MainPage_ProgramName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainPage_ProgramName.setAutoFillBackground(False)
        self.MainPage_ProgramName.setTextFormat(QtCore.Qt.RichText)
        self.MainPage_ProgramName.setAlignment(QtCore.Qt.AlignCenter)
        self.MainPage_ProgramName.setObjectName("MainPage_ProgramName")
        self.MainPage_insertUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainPage_insertUserButton.setGeometry(QtCore.QRect(290, 200, 210, 40))
        self.MainPage_insertUserButton.setMinimumSize(QtCore.QSize(210, 40))
        self.MainPage_insertUserButton.setMaximumSize(QtCore.QSize(210, 40))
        self.MainPage_insertUserButton.setObjectName("MainPage_insertUserButton")
        self.MainPage_capturePhotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainPage_capturePhotoButton.setGeometry(QtCore.QRect(290, 250, 210, 40))
        self.MainPage_capturePhotoButton.setMinimumSize(QtCore.QSize(210, 40))
        self.MainPage_capturePhotoButton.setMaximumSize(QtCore.QSize(210, 40))
        self.MainPage_capturePhotoButton.setObjectName("MainPage_capturePhotoButton")
        self.MainPage_databaseMaintananceButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainPage_databaseMaintananceButton.setGeometry(QtCore.QRect(290, 300, 210, 40))
        self.MainPage_databaseMaintananceButton.setMinimumSize(QtCore.QSize(210, 40))
        self.MainPage_databaseMaintananceButton.setMaximumSize(QtCore.QSize(210, 40))
        self.MainPage_databaseMaintananceButton.setObjectName("MainPage_databaseMaintananceButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Hand scanner", "MainWindow"))
        self.MainPage_ProgramName.setText(_translate("Hand scanner", "Hand Vein Scanner"))
        self.MainPage_insertUserButton.setText(_translate("Hand scanner", "Inser new user"))
        self.MainPage_capturePhotoButton.setText(_translate("Hand scanner", "Capture to database"))
        self.MainPage_databaseMaintananceButton.setText(_translate("Hand scanner", "Database maintanance"))
