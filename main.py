from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.Qt import QImage, QPixmap
import sys
from request import image


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
        self.setGeometry(20, 60, 700, 600)
        # А также его заголовок
        self.setWindowTitle('как')
        self.pixmap = QPixmap(QImage(ImageQt(image)))
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(60, 60)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    sys.excepthook = except_hook
    form.show()
    sys.exit(app.exec())
