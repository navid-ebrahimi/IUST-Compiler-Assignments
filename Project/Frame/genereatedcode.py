from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication([])
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QHBoxLayout(central_widget)

def PythonCode():
	webview = QWebEngineView()
	layout.addWidget(webview)

	webview.load(QUrl('https://www.varzesh3.com'))
	webview.setWindowTitle('Classic')
	webview.setFixedWidth(400)


def Test(self):
	frame = self.sender()
	# to be completed

if __name__ == '__main__':
	PythonCode()
	window.show()
	app.exec_()
