# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(979, 610)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(30, 10, 371, 451))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setObjectName("treeWidget")
        self.root = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.choicedirbut = QtWidgets.QPushButton(self.centralwidget)
        self.choicedirbut.setGeometry(QtCore.QRect(420, 20, 91, 41))
        self.choicedirbut.setText("选择文件夹")
        self.choicedirbut.setObjectName("choicedirbut")
        self.choicedirbut.clicked.connect(self.choose_dir)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 530, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 480, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试GUI"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "文件名"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "path1"))

        self.treeWidget.itemChanged.connect(self.checker)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "选择目录"))
        self.pushButton.clicked.connect(self.buttonevent)
        self.add(self.root, "test.txt")
        # list1 = self.treeWidget.selectedItems() 获取选中
        # print(list1)

    def choose_dir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self.centralwidget, "选择文件夹"
        ).replace("/", "\\")
        self.lineEdit.setText(path)

    def checker(self, item, column):
        if item.checkState(column) == QtCore.Qt.CheckState.Checked:
            if item.childCount() > 0:
                for i in range(item.childCount()):
                    item.child(i).setCheckState(0, QtCore.Qt.CheckState.Checked)
                    self.checker(item.child(i), column)
        else:
            if item.childCount() > 0:
                for i in range(item.childCount()):
                    item.child(i).setCheckState(0, QtCore.Qt.CheckState.Unchecked)
                    self.checker(item.child(i), column)

    def add(self, parent, text):
        item = QtWidgets.QTreeWidgetItem(parent)
        item.setText(0, text)

        item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
        return item

    def buttonevent(self):
        if os.path.isdir(self.lineEdit.text()):
            self.treeWidget.clear()
            self.root = QtWidgets.QTreeWidgetItem(self.treeWidget)
            self.root.setText(0, self.lineEdit.text())
            self.root.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            self.startadd(self.lineEdit.text(), self.root)
        else:
            print("目录不存在")

    def startadd(self, path, parent):
        path1 = os.listdir(path)
        for i in path1:
            if os.path.isfile(path + "\\" + i):
                self.add(parent, os.path.basename(i))
                print("文件", os.path.basename(i))
            else:
                pitem = self.add(parent, os.path.basename(i))
                print(pitem)
                print("目录:", os.path.basename(i))
                print(i)
                self.startadd(path=path + "\\" + i, parent=pitem)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
