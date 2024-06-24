import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget, QSlider
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt


class FontPreviewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("实时字体试用程序")
        self.setGeometry(100, 100, 500, 400)

        self.createMenu()

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(20, 50, 460, 200)

        self.label = QLabel("实时预览", self)
        self.label.setGeometry(20, 260, 460, 100)

        self.createFontSizeSlider()

    def createMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件")

        loadFontAction = QAction("加载字体", self)
        loadFontAction.triggered.connect(self.loadFont)
        fileMenu.addAction(loadFontAction)

        exitAction = QAction("退出", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def createFontSizeSlider(self):
        self.sliderLabel = QLabel("字体大小", self)
        self.sliderLabel.setGeometry(20, 370, 70, 20)

        self.fontSizeSlider = QSlider(Qt.Horizontal, self)
        self.fontSizeSlider.setGeometry(100, 370, 300, 20)
        self.fontSizeSlider.setRange(10, 50)
        self.fontSizeSlider.setValue(20)
        self.fontSizeSlider.valueChanged.connect(self.changeFontSize)

    def changeFontSize(self):
        font = self.label.font()
        font.setPointSize(self.fontSizeSlider.value())
        self.textEdit.setFont(font)
        self.label.setFont(font)

    def loadFont(self):
        fontDialog = QFileDialog.getOpenFileName(
            self, "选择字体文件", filter="字体文件 (*.ttf *.otf)")
        fontPath = fontDialog[0]
        if fontPath:
            fontId = QFontDatabase.addApplicationFont(fontPath)
            fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
            if fontFamilies:
                font = QFont(fontFamilies[0])
                font.setPointSize(self.fontSizeSlider.value())
                self.textEdit.setFont(font)
                self.label.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontPreviewer()
    window.show()
    sys.exit(app.exec_())
