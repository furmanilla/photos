import os
from PyQt5.QtWidgets import *
from QSS import QSS

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image


app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
lw_files = QListWidget()

btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Дзеркало')
btn_shar = QPushButton('Ршзкість')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()
co11 = QVBoxLayout()
co12 = QVBoxLayout()
co11.addWidget(btn_dir)
co11.addWidget(lw_files)
co12.addWidget(lb_image,95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_shar)
row_tools.addWidget(btn_bw)
co12.addLayout(row_tools)

row.addLayout(co11,20)
row.addLayout(co12,80)
win.setLayout(row)
win.setStyleSheet(QSS)

wrkdir = ''
def filter(files,extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global  workdir 
    workdir = QFileDialog.getExistingDirectory()
def showFilenames():
    extensions = ['jpg','jpes','png','gif','bpm']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    lw_files.clear()
    for filename in filenames :
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenames)


class ImageProcesor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        Image_path = os.path.join(dir,filename)
        self.image = Image.open(Image_path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.seveImage()
        Image_path = os.path.join(self.dir,self.save_dir , self.filename)
        self.showImage(Image_path)

    def seveImage(self):
        path = os.path.join(self.dir,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
            Image_path = os.path.join(path, self.filename)
            self.image.save(Image_path)

    def showImage(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w,h = lb_image.width(),lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

def showChosenImage():
    if lw_files.currentRow() >=0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir,filename)
        Image_path = os.path.join(workimage.dir,workimage.filename )
        workimage.showImage(Image_path)

workimage = ImageProcesor()
lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)


win.show()
app.exec()