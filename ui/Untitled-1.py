from PyQt5 import QtWidgets, uic
import sys

class clsHello(QtWidgets.QMainWindow):
	def __init__(self):
		super(clsHello, self).__init__()
		uic.loadUi('hello.ui',self)


def main():
	app = QtWidgets.QApplication(sys.argv)	
	
	objeto = clsHello()
	objeto.show()
	app.exec_()


if __name__ == '__main__':
	main()