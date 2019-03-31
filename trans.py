#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'LENOVO'
import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5.QtCore import Qt
from Ui_trans import Ui_Form
from content import *


class Content(QWidget, Ui_Form):
    def __init__(self, parent=None):
        # 继承主窗口类
        super(Content, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        # 将 textEdit 设置为只读模式
        self.textEdit.setReadOnly(True)
        # 将鼠标焦点放在 lineEdit 编辑栏里
        self.lineEdit.setFocus()

    def queryContent(self):
        # 获取 lineEdit 中的文本
        city = self.lineEdit.text()
        info = query_content(city)
        self.lineEdit.setFocus()
        # 设置文本
        self.textEdit.setText(info)

    def keyPressEvent(self, e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
            self.queryContent()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    content = Content()
    content.show()
    sys.exit(app.exec_())
