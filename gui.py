# -*- coding: utf-8 -*-
import datetime
import os
import argparse
from PyQt5.QtWidgets import QHeaderView, QTextEdit

# noinspection PyUnresolvedReferences
import resource
# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCharFormat, QColor
from qt_material import apply_stylesheet
import time
import encode
import decode
import threading


def timenow():
    return time.strftime("[%m-%d %H:%M:%S] ", time.localtime())


# noinspection PyUnresolvedReferences

class signalsend(QtCore.QObject):
    mysignal = QtCore.pyqtSignal(list)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(979, 662)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qimage.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        apply_stylesheet(MainWindow, theme='light_purple.xml', css_file='ui.css')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 961, 451))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 540, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 480, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 610, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 540, 161, 41))
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 480, 61, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 610, 161, 41))
        self.pushButton_4.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 480, 421, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 480, 61, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(530, 520, 441, 131))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        MainWindow.setCentralWidget(self.centralwidget)

        self.message = QtWidgets.QMessageBox()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # noinspection PyUnresolvedReferences



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件头加解密"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "文件名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "文件大小"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "加密状态"))
        self.pushButton.setText(_translate("MainWindow", "选择加/解密项目"))
        self.pushButton_2.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton_3.setText(_translate("MainWindow", "解密"))
        self.label.setText(_translate("MainWindow", "目录:"))
        self.pushButton_4.setText(_translate("MainWindow", "加密"))
        self.label_2.setText(_translate("MainWindow", "密码:"))
        self.treeWidget.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.treeWidget.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.treeWidget.header().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.pushButton.clicked.connect(self.buttonevent)
        self.pushButton_2.clicked.connect(self.choose_dir)
        self.pushButton_3.clicked.connect(self.startdecode)
        self.pushButton_4.clicked.connect(self.startencode)
        self.treeWidget.itemChanged.connect(self.checker)
        # self.treeWidget.itemExpanded.connect()
        self.textcursor = self.textEdit.textCursor()
        self.greenFormat = QTextCharFormat()
        self.redFormat = QTextCharFormat()
        self.greyFormat = QTextCharFormat()
        self.greenFormat.setForeground(QColor(0, 128, 0))
        self.redFormat.setForeground(QColor(255, 0, 0))
        self.greyFormat.setForeground(QColor(128, 128, 128))
        self.log('程序启动', self.greenFormat)

    def log(self, text, format):
        self.textcursor.insertText(timenow() + text + '\n', format)

    def pr(self, text, format):
        if format == 'red':
            format = self.redFormat
        elif format == 'green':
            format = self.greenFormat
        elif format == 'grey':
            format = self.greyFormat
        self.log(text, format)

    def updatechecklist(self, encode):

        self.checklist = []

        def get_checked_items(item):
            checked_items = []
            if item.checkState(0) == QtCore.Qt.CheckState.Checked and (os.path.splitext(item.text(0))[-1] != '.enc' or encode is False):
                checked_items.append(item)
            for i in range(item.childCount()):
                child = item.child(i)
                checked_items.extend(get_checked_items(child))
            return checked_items

        check1 = get_checked_items(self.treeWidget.invisibleRootItem())

        def getpath(item):
            path = ''
            parentlist = []
            parent = item.parent()
            while parent is not None:
                parentlist.append(parent)
                parent = parent.parent()
            parentlist.reverse()
            for b in parentlist:
                path = os.path.join(path, b.text(0))
            path = os.path.join(path, item.text(0))
            if os.path.isfile(path):
                return path

        for i in check1:
            self.checklist.append(getpath(i))
        self.checklist = list(set(filter(None, self.checklist)))

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
            icon_provider = QtWidgets.QFileIconProvider()
            file_info = QtCore.QFileInfo(self.lineEdit.text())
            icon = icon_provider.icon(file_info)
            self.root.setIcon(0, icon)
            print(self.root.parent())

            self.startadd(self.lineEdit.text(), self.root)
        elif os.path.isfile(self.lineEdit.text()):
            self.treeWidget.clear()
            self.root = QtWidgets.QTreeWidgetItem(self.treeWidget)
            self.root.setText(0, self.lineEdit.text())
            self.root.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            icon_provider = QtWidgets.QFileIconProvider()
            file_info = QtCore.QFileInfo(self.lineEdit.text())
            icon = icon_provider.icon(file_info)

            size = os.path.getsize(self.lineEdit.text())
            if size > 1024:
                self.root.setText(1, str(size // 1024) + ' Kb')
            else:
                self.root.setText(1, str(size) + ' b')

            if os.path.splitext(self.lineEdit.text())[-1] == '.enc':

                self.root.setText(2, '√')
            else:

                self.root.setText(2, '×')

            self.root.setIcon(0, icon)

        else:
            self.log('目录不存在', self.redFormat)
    def messgaebox(self,type,title,text):
        if type == 'info':
            self.message.information(MainWindow, title, text)
        if type == 'warning':
            self.message.warning(MainWindow, title, text)
        if type == 'critical':
            self.message.critical(MainWindow, title, text)

    @QtCore.pyqtSlot(list)  # 槽函数
    def recevent(l1):
        mestype = l1[0]
        mestitle = l1[1]
        mesinfo = l1[2]

    rec = signalsend()  # 信号
    rec.mysignal.connect(recevent)

    def startadd(self, path, parent):
        path1 = os.listdir(path)
        for i in path1:
            if os.path.isfile(path + "\\" + i):
                item = self.add(parent, os.path.basename(i))
                size = os.path.getsize(path + "\\" + i)
                if size > 1024:
                    item.setText(1, str(size // 1024) + ' Kb')
                else:
                    item.setText(1, str(size) + ' b')
                file_path = path + "\\" + i
                icon_provider = QtWidgets.QFileIconProvider()
                file_info = QtCore.QFileInfo(file_path)
                icon = icon_provider.icon(file_info)
                item.setIcon(0, icon)
                if os.path.splitext(file_path)[-1] == '.enc':
                    item.setText(2, '√')
                else:
                    item.setText(2, '×')



            else:
                pitem = self.add(parent, os.path.basename(i))
                icon_provider = QtWidgets.QFileIconProvider()
                file_info = QtCore.QFileInfo(path + '\\' + i)
                icon = icon_provider.icon(file_info)
                pitem.setIcon(0, icon)

                self.startadd(path=path + "\\" + i, parent=pitem)

    def startencode(self):
        if not self.lineEdit_2.text():
            self.log('密码不能为空', self.redFormat)
            return

        print('加密')
        self.updatechecklist(encode=True)
        print(self.checklist)
        thre = encodefile(self.checklist, self.lineEdit_2.text())
        thre1 = threading.Thread(target=thre.run)
        thre1.start()
        return

    def startdecode(self):
        if not self.lineEdit_2.text():
            self.log('密码不能为空', self.redFormat)
            return

        print('解密')
        self.updatechecklist(encode=False)
        print(self.checklist)
        thre = decodefile(self.checklist, self.lineEdit_2.text())
        thre1 = threading.Thread(target=thre.run)
        thre1.start()
        return


class decodefile():
    def __init__(self, listfile, password):
        super().__init__()
        self.listfile = listfile
        self.password = password
        print('encode:', self.listfile)

    def run(self):
        print('start run')
        for i in self.listfile:
            dict1 = decode.decodefile(i, self.password)

            print(dict1)
            if dict1['status'] == 'ok':
                format1 = 'green'
                filename = dict1['filename']
                newfile = dict1['newfile']
                runtime = dict1['time']
                ui.pr('文件:{}解密成功,解密后文件名:{},运行时间:{}'.format(filename, newfile, runtime), format1)



            else:
                format1 = 'red'
                filename = dict1['filename']
                reason = dict1['reason']
                runtime = dict1['time']
                ui.pr('文件:{}解密失败,原因:{},运行时间:{}'.format(filename, reason, runtime), format1)
        ui.buttonevent()


class encodefile():
    def __init__(self, listfile, password):
        super().__init__()
        self.listfile = listfile
        self.password = password
        self.message = QtWidgets.QMessageBox()
        print('encode:', self.listfile)

    def run(self):
        print('start run')
        tim = 0
        for i in self.listfile:
            dict1 = encode.encodefile(i, self.password)

            print(dict1)
            if dict1['status'] == 'ok':
                format1 = 'green'
                filename = dict1['filename']
                newfile = dict1['newfile']
                runtime = dict1['time']
                ui.pr('文件:{}加密成功,加密后文件名:{},运行时间:{}'.format(filename, newfile,
                                                                           str(datetime.timedelta(seconds=runtime))),
                      format1)
                tim += runtime



            else:
                format1 = 'red'
                filename = dict1['filename']
                reason = dict1['reason']
                runtime = dict1['time']
                ui.pr('文件:{}加密失败,原因:{},运行时间:{}'.format(filename, reason,
                                                                   str(datetime.timedelta(seconds=runtime))), format1)
                tim += runtime

        ui.buttonevent()
        text = '加密完成,总用时:'+str(datetime.timedelta(seconds=tim))
        ui.messgaebox('info', '信息', text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    parser = argparse.ArgumentParser(description='参数')
    parser.add_argument('-p', '--password', help='密码', required=False)
    parser.add_argument('-fp', '--folderpath', help='目录', required=False)
    args = parser.parse_args()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if args.password:
        ui.lineEdit_2.insert(args.password)
    if args.folderpath:
        ui.lineEdit.insert(args.folderpath)
        ui.buttonevent()
        ui.treeWidget.expandAll()
    sys.exit(app.exec_())
