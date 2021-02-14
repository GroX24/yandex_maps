from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.Qt import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys
from request import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()
        # В метод initUI() будем выносить всю настройку интерфейса,
        # чтобы не перегружать инициализатор
        self.initUI()

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(200, 200, 700, 550)
        # А также его заголовок
        self.setWindowTitle('как')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.coords = find_toponym("Москва Коптево")
        self.delta = defaultdelta
        self.image = QLabel(self)
        self.image.move(50, 50)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(QPixmap(QImage(ImageQt(gib_me_da_pic(*self.coords, self.delta)))))

    def keyPressEvent(self, e):
        sizechange = 2
        if e.key() == Qt.Key_PageDown:
            self.delta *= sizechange
        elif e.key() == Qt.Key_PageUp:
            self.delta /= sizechange
        self.delta = round(min(max(mindelta, self.delta), maxdelta), 5)
        self.update()

    def update(self):
        self.image.setPixmap(QPixmap(QImage(ImageQt(gib_me_da_pic(*self.coords, self.delta)))))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    sys.excepthook = except_hook
    form.show()
    sys.exit(app.exec())
