# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created: Sun May 26 22:05:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 349)
        self.setting = QtGui.QTabWidget(Dialog)
        self.setting.setGeometry(QtCore.QRect(10, 20, 371, 291))
        self.setting.setObjectName(_fromUtf8("setting"))
        self.setting.setFixedSize(400,349)
#         self.general = QtGui.QWidget()
#         self.general.setObjectName(_fromUtf8("general"))
#         self.setting.addTab(self.general, _fromUtf8(""))
        self.account = QtGui.QWidget()
        self.account.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.account.setObjectName(_fromUtf8("account"))
        self.widget = QtGui.QWidget(self.account)
        self.widget.setGeometry(QtCore.QRect(30, 30, 261, 211))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.email = QtGui.QLabel(self.widget)
        self.email.setObjectName(_fromUtf8("email"))
        self.horizontalLayout.addWidget(self.email)
        self.emailEdit = QtGui.QLineEdit(self.widget)
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))
        self.horizontalLayout.addWidget(self.emailEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.password = QtGui.QLabel(self.widget)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout_2.addWidget(self.password)
        self.passwordEdit = QtGui.QLineEdit(self.widget)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.horizontalLayout_2.addWidget(self.passwordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.code = QtGui.QLabel(self.widget)
        self.code.setObjectName(_fromUtf8("code"))
        self.horizontalLayout_3.addWidget(self.code)
        self.codeEdit = QtGui.QLineEdit(self.widget)
        self.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        self.horizontalLayout_3.addWidget(self.codeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.codeButton = QtGui.QPushButton(self.widget)
        self.codeButton.setObjectName(_fromUtf8("codeButton"))
        self.horizontalLayout_4.addWidget(self.codeButton)
        self.codeImage = QtGui.QLabel(self.widget)
        self.codeImage.setText(_fromUtf8(""))
        self.codeImage.setObjectName(_fromUtf8("codeImage"))
        self.codeImage.setScaledContents(True)
        self.horizontalLayout_4.addWidget(self.codeImage)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.setting.addTab(self.account, _fromUtf8(""))
#         self.shortcut = QtGui.QWidget()
#         self.shortcut.setObjectName(_fromUtf8("shortcut"))
#         self.setting.addTab(self.shortcut, _fromUtf8(""))
        self.help = QtGui.QWidget()
        self.help.setObjectName(_fromUtf8("help"))
        self.widget = QtGui.QWidget(self.help)
        self.widget.setGeometry(QtCore.QRect(70, 50, 221, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.github = QtGui.QLabel(self.widget)
        self.github.setObjectName(_fromUtf8("github"))
        self.horizontalLayout_5.addWidget(self.github)
        self.glink = QtGui.QLabel(self.widget)
        self.glink.setText(_fromUtf8(""))
        self.glink.setObjectName(_fromUtf8("glink"))
        self.horizontalLayout_5.addWidget(self.glink)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.douban = QtGui.QLabel(self.widget)
        self.douban.setObjectName(_fromUtf8("douban"))
        self.horizontalLayout_6.addWidget(self.douban)
        self.dlink = QtGui.QLabel(self.widget)
        self.dlink.setText(_fromUtf8(""))
        self.dlink.setObjectName(_fromUtf8("dlink"))
        self.horizontalLayout_6.addWidget(self.dlink)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.setting.addTab(self.help, _fromUtf8(""))
        
        self.retranslateUi(Dialog)
        self.setting.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "首选项", None, QtGui.QApplication.UnicodeUTF8))
#         self.setting.setTabText(self.setting.indexOf(self.general), QtGui.QApplication.translate("Dialog", "常规", None, QtGui.QApplication.UnicodeUTF8))
        self.email.setText(QtGui.QApplication.translate("Dialog", "邮箱：", None, QtGui.QApplication.UnicodeUTF8))
        self.password.setText(QtGui.QApplication.translate("Dialog", "密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.code.setText(QtGui.QApplication.translate("Dialog", "验证码：", None, QtGui.QApplication.UnicodeUTF8))
        self.codeButton.setText(QtGui.QApplication.translate("Dialog", "获取验证码", None, QtGui.QApplication.UnicodeUTF8))
        self.setting.setTabText(self.setting.indexOf(self.account), QtGui.QApplication.translate("Dialog", "帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.github.setText(QtGui.QApplication.translate("Dialog", "项目主页：", None, QtGui.QApplication.UnicodeUTF8))
        self.douban.setText(QtGui.QApplication.translate("Dialog", "豆瓣主页：", None, QtGui.QApplication.UnicodeUTF8))
#         self.setting.setTabText(self.setting.indexOf(self.shortcut), QtGui.QApplication.translate("Dialog", "快捷键", None, QtGui.QApplication.UnicodeUTF8))
        self.setting.setTabText(self.setting.indexOf(self.help), QtGui.QApplication.translate("Dialog", "帮助", None, QtGui.QApplication.UnicodeUTF8))

