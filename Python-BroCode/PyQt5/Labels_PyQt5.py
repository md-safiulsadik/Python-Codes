
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("D:\\Study\\Python\\Python_BroCode\\PyQt5\\Icon.jpg"))
        self.setGeometry(555, 250, 800, 720)
        self.setWindowTitle("QLabels")
        
        label = QLabel("This is QLabels", self)

        label.setFont(QFont("Space Mono", 30))
        label.setGeometry(0, 0, 800, 720)
        label.setStyleSheet("color : #f09d22;"
                            "background-color : #88bcd1;"
                            "font-weight: bold;"
                            "font-style: normal;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        
        label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER
        
        
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()