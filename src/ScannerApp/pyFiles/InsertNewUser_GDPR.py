from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Agreement and sign")
        MainWindow.resize(800, 480)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InsertNewUser_GDPR_ProgramName = QtWidgets.QLabel(self.centralwidget)
        self.InsertNewUser_GDPR_ProgramName.setEnabled(True)
        self.InsertNewUser_GDPR_ProgramName.setGeometry(QtCore.QRect(200, 50, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.InsertNewUser_GDPR_ProgramName.setFont(font)
        self.InsertNewUser_GDPR_ProgramName.setFocusPolicy(QtCore.Qt.NoFocus)
        self.InsertNewUser_GDPR_ProgramName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.InsertNewUser_GDPR_ProgramName.setAutoFillBackground(False)
        self.InsertNewUser_GDPR_ProgramName.setTextFormat(QtCore.Qt.RichText)
        self.InsertNewUser_GDPR_ProgramName.setAlignment(QtCore.Qt.AlignCenter)
        self.InsertNewUser_GDPR_ProgramName.setObjectName("InsertNewUser_GDPR_ProgramName")
        self.InsertNewUser_GDPR_backButton = QtWidgets.QPushButton(self.centralwidget)
        self.InsertNewUser_GDPR_backButton.setGeometry(QtCore.QRect(700, 420, 70, 40))
        self.InsertNewUser_GDPR_backButton.setMinimumSize(QtCore.QSize(70, 40))
        self.InsertNewUser_GDPR_backButton.setMaximumSize(QtCore.QSize(70, 40))
        self.InsertNewUser_GDPR_backButton.setObjectName("InsertNewUser_GDPR_backButton")
        self.InsertNewUser_GDPR_line = QtWidgets.QFrame(self.centralwidget)
        self.InsertNewUser_GDPR_line.setGeometry(QtCore.QRect(125, 140, 550, 16))
        self.InsertNewUser_GDPR_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.InsertNewUser_GDPR_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.InsertNewUser_GDPR_line.setObjectName("InsertNewUser_GDPR_line")
        self.InsertNewUser_GDPR_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.InsertNewUser_GDPR_scrollArea.setGeometry(QtCore.QRect(100, 160, 600, 250))
        self.InsertNewUser_GDPR_scrollArea.setWidgetResizable(True)
        self.InsertNewUser_GDPR_scrollArea.setObjectName("InsertNewUser_GDPR_scrollArea")
        self.InsertNewUser_GDPR_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.InsertNewUser_GDPR_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 248))
        self.InsertNewUser_GDPR_scrollAreaWidgetContents.setObjectName("InsertNewUser_GDPR_scrollAreaWidgetContents")
        self.InsertNewUser_GDPR_cert = QtWidgets.QTextBrowser(self.InsertNewUser_GDPR_scrollAreaWidgetContents)
        self.InsertNewUser_GDPR_cert.setGeometry(QtCore.QRect(0, 0, 601, 251))
        self.InsertNewUser_GDPR_cert.setObjectName("InsertNewUser_GDPR_cert")
        self.InsertNewUser_GDPR_scrollArea.setWidget(self.InsertNewUser_GDPR_scrollAreaWidgetContents)
        self.InsertNewUser_GDPR_agreeAndSignButton = QtWidgets.QPushButton(self.centralwidget)
        self.InsertNewUser_GDPR_agreeAndSignButton.setGeometry(QtCore.QRect(275, 420, 250, 40))
        self.InsertNewUser_GDPR_agreeAndSignButton.setMinimumSize(QtCore.QSize(250, 40))
        self.InsertNewUser_GDPR_agreeAndSignButton.setMaximumSize(QtCore.QSize(250, 40))
        self.InsertNewUser_GDPR_agreeAndSignButton.setObjectName("InsertNewUser_GDPR_agreeAndSignButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Agreement and sign", "MainWindow"))
        self.InsertNewUser_GDPR_ProgramName.setText(_translate("Agreement and sign", "Insert New User"))
        self.InsertNewUser_GDPR_backButton.setText(_translate("Agreement and sign", "Back"))
        self.InsertNewUser_GDPR_scrollArea.setToolTip(_translate("Agreement and sign", "<html><head/><body><p><span style=\" font-weight:600;\">Adatkezelési Tájékoztató és Beleegyező Nyilatkozat</span></p><p><span style=\" font-weight:600;\">1. Az adatkezelő adatai:</span></p><p>Név: [Neve]<br/>Születési dátum: [Kapcsolattartó telefonszáma]</p><p><span style=\" font-weight:600;\">2. Az adatkezelés célja:</span></p><p>Az adatkezelés célja a speciális fényképezőgép által készített képek elmentése, valamint a felhasználó nevének és születési dátumának tárolása.</p><p><span style=\" font-weight:600;\">3. A kezelt adatok köre:</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fényképek a speciális fényképezőgép által készítve</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Név</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Születési dátum</li></ul><p><span style=\" font-weight:600;\">4. Az adatkezelés jogalapja:</span></p><p>Az Európai Parlament és a Tanács (EU) 2016/679 rendelete (GDPR) 6. cikk (1) bekezdés a) pontja alapján az érintett hozzájárulása.</p><p><span style=\" font-weight:600;\">5. Az adatok tárolásának időtartama:</span></p><p>Az adatokat az Ön hozzájárulásának visszavonásáig tároljuk.</p><p><span style=\" font-weight:600;\">6. Az érintett jogai:</span></p><p>Ön jogosult:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tájékoztatást kérni személyes adatai kezeléséről</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hozzáférést kérni a kezelt adatokhoz</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Helyesbítést kérni, ha a kezelt adatok pontatlanok vagy hiányosak</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Törlést kérni, ha az adatok kezelése jogellenes vagy a hozzájárulás visszavonásra kerül</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Az adatkezelés korlátozását kérni</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adathordozhatóságot kérni</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hozzájárulását bármikor visszavonni</li></ul><p><span style=\" font-weight:600;\">7. Hozzájárulás:</span></p><p>Alulírott, [Név], az alábbi beleegyező nyilatkozatot teszem:</p><p>Beleegyezem, hogy a [Cég/Szervezet neve] a személyes adataimat (név, születési dátum) és a speciális fényképezőgép által készített képeket a fent megjelölt célból kezelje. Tudomásul veszem, hogy hozzájárulásomat bármikor visszavonhatom az adatkezelőhöz intézett írásos nyilatkozattal.</p></body></html>"))
        self.InsertNewUser_GDPR_cert.setHtml(_translate("Agreement and sign", """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adatkezelési Tájékoztató és Beleegyező Nyilatkozat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: left;
            margin: 50px;
        }
        .signature {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1><span style="font-weight:600;">Adatkezelési Tájékoztató és Beleegyező Nyilatkozat</span></h1>
    <p><span style="font-weight:600;">1 Az adatkezelő adatai:</span></p>
    <p>Szervezet neve: Sapientia Erdélyi Magyar Tudomány Egyetem - Marosvásárhelyi kar - Villamosmérnöki tanszék<br/>Az adatkezelést irányító diák: Vasi András - Számítástechnika 4. év<br/>Projekt vezető tanár: Dr. Lefkovits László, Sapientia Erdélyi Magyar Tudomány Egyetem - Marosvásárhelyi kar - Villamosmérnöki tanszék</p>
    <p><span style="font-weight:600;">2. Az adatkezelés célja:</span></p>
    <p>Az adatkezelés célja a speciális fényképezőgép által készített képek elmentése, azoknak későbbi felhasználása kutatások tárgyaként, esetenként a képek publikálása tudományos folyóíratokban / konferenciákon - titokban tartva a képek alanyainak kilétét és egyéb személyes adatait, valamint a felhasználó nevének és születési dátumának tárolása.</p>
    <p><span style="font-weight:600;">3. A kezelt adatok köre:</span></p>
    <ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">
    <li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Fényképek a speciális fényképezőgép által készítve</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Név és Születési dátum</li>
    </ul>
    <p><span style="font-weight:600;">4. Az adatkezelés jogalapja:</span></p>
    <p>Az Európai Parlament és a Tanács (EU) 2016/679 rendelete (GDPR) 6. cikk (1) bekezdés a) pontja alapján az érintett hozzájárulása.</p>
    <p><span style="font-weight:600;">5. Az adatok tárolásának időtartama:</span></p>
    <p>Az adatokat az Ön hozzájárulásának visszavonásáig tároljuk.</p>
    <p><span style="font-weight:600;">6. Az érintett jogai:</span></p>
    <p>Ön jogosult:</p>
    <ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">
    <li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Tájékoztatást kérni személyes adatai kezeléséről</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Hozzáférést kérni a kezelt adatokhoz</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Helyesbítést kérni, ha a kezelt adatok pontatlanok vagy hiányosak</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Törlést kérni, ha az adatok kezelése jogellenes vagy a hozzájárulás visszavonásra kerül</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Az adatkezelés korlátozását kérni</li>
    <li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Adathordozhatóságot kérni</li>
    <li style="margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Hozzájárulását bármikor visszavonni</li>
    </ul>
    <p><span style="font-weight:600;">7. Hozzájárulás:</span></p>
    <p>Hozzájárulok az alábbi beleegyező nyilatkozatot teszem:</p>
    <p>Beleegyezem, hogy a Sapientia Erdélyi Magyar Tudomány Egyetem a személyes adataimat (név, születési dátum) és a speciális fényképezőgép által készített képeket a fent megjelölt célból kezelje. Tudomásul veszem, hogy hozzájárulásomat bármikor visszavonhatom az adatkezelőhöz intézett írásos nyilatkozattal.</p>

    <p><span style="font-weight:600;">Marosvásárhely, Maros megye, Románia    <br/>
</body>
</html>
"""))
        self.InsertNewUser_GDPR_agreeAndSignButton.setText(_translate("MainWindow", "Agreement and Signature "))
