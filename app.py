"""
Comando para converter arquivos ".ui" para ".py":

$ pyuic5 nome.ui -o novo_nome.py
"""

import sys
from design import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
)


class RedimensionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.set_styles()

        self.btnChooseFile.clicked.connect(
            self.open_image
        )
        self.buttonResize.clicked.connect(
            self.resize_img
        )
        self.btnSave.clicked.connect(
            self.save_img
        )

    def open_image(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open image',
            r'C:\Users\win\Pictures'
        )
        self.inputOpenFile.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.imgLabel.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resize_img(self):
        if hasattr(self, 'original_img'):
            width = int(self.inputWidth.text())
            self.new_image = self.original_img.scaledToWidth(width)
            self.imgLabel.setPixmap(self.new_image)
            self.inputWidth.setText(str(self.new_image.width()))
            self.inputHeight.setText(str(self.new_image.height()))

    def save_img(self):
        if hasattr(self, 'new_image'):
            img, _ = QFileDialog.getSaveFileName(
                self.centralwidget,
                'Resize image',
                r'C:\Users\win\Pictures'
            )
            self.new_image.save(img, 'PNG')

    def set_styles(self):
        self.btnChooseFile.setStyleSheet('padding: 7px;')
        self.inputOpenFile.setStyleSheet('padding: 5px')
        self.inputHeight.setStyleSheet('padding: 3px')
        self.inputWidth.setStyleSheet('padding: 3px')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = RedimensionarImagem()
    app.show()
    qt.exec_()
