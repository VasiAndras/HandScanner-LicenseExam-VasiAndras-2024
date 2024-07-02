import sys
import argparse
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage
from PyQt5.QtCore import Qt, QPoint

class SignatureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signature")
        self.setGeometry(100, 100, 800, 480)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.canvas = QPixmap(750, 350)
        self.canvas.fill(Qt.white)
        self.drawing = False
        self.last_point = QPoint()
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.canvas_label = Canvas()
        main_layout.addWidget(self.canvas_label, alignment=Qt.AlignCenter)
        button_layout = QHBoxLayout()
        self.btn_ok = QPushButton("OK")
        self.btn_reset = QPushButton("Reset")
        self.btn_back = QPushButton("Back")
        button_height = 40
        self.btn_ok.setFixedHeight(button_height)
        self.btn_reset.setFixedHeight(button_height)
        self.btn_back.setFixedHeight(button_height)
        button_layout.addWidget(self.btn_ok)
        button_layout.addWidget(self.btn_reset)
        button_layout.addWidget(self.btn_back)
        main_layout.addLayout(button_layout)
        self.btn_ok.clicked.connect(self.save_signature)
        self.btn_reset.clicked.connect(self.canvas_label.reset_canvas)
        self.btn_back.clicked.connect(self.close)

    def save_signature(self):
        usercode = window.canvas_label.usercode
        file_path = "Signatures/" + usercode + ".png"
        self.canvas_label.save_image(file_path)
        QMessageBox.information(self, "Signature", "You have successfully accepted and signed the contract! \n Thank you!")
        QMessageBox.information(self, "USER CODE", "Your user code: " + usercode)

        self.close()

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750, 350)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: white;")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.last_point = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 5, Qt.SolidLine, Qt.RoundCap)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def save_image(self, file_path):
        self.image.save(file_path)
        print(f"Signature saved as {file_path}")

    def reset_canvas(self):
        self.image.fill(Qt.white)
        self.update()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Signature App')
    parser.add_argument('-uc', '--usercode', type=str, default='UC000000', help='USER CODE')
    parser.add_argument('-ln', '--legalname', type=str, default='LEGAL NAME', help='LEGAL NAME OF USER')
    parser.add_argument('-bd', '--birthday', type=str, default='2000.01.01.', help='BIRTH DATE OF USER')
    args = parser.parse_args()
    app = QApplication(sys.argv)
    window = SignatureApp()
    window.canvas_label.usercode = args.usercode
    window.canvas_label.legalname = args.legalname
    window.canvas_label.birthdaybirthday = args.birthday
    window.show()
    sys.exit(app.exec_())
