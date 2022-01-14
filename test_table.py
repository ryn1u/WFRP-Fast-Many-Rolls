# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.base_table_layout = QtWidgets.QVBoxLayout()
        self.base_table_layout.setObjectName("base_table_layout")
        self.table_header_frame = QtWidgets.QFrame(self.centralwidget)
        self.table_header_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.table_header_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.table_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_header_frame.setObjectName("table_header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.table_header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.table_header_frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.table_header_frame)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.testing_name_label = QtWidgets.QLabel(self.table_header_frame)
        self.testing_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.testing_name_label.setObjectName("testing_name_label")
        self.horizontalLayout_2.addWidget(self.testing_name_label)
        self.test_skill_list = QtWidgets.QComboBox(self.table_header_frame)
        self.test_skill_list.setObjectName("test_skill_list")
        self.horizontalLayout_2.addWidget(self.test_skill_list)
        self.testing_roll_label = QtWidgets.QLabel(self.table_header_frame)
        self.testing_roll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.testing_roll_label.setObjectName("testing_roll_label")
        self.horizontalLayout_2.addWidget(self.testing_roll_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.table_header_frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.ps_label = QtWidgets.QLabel(self.table_header_frame)
        self.ps_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ps_label.setObjectName("ps_label")
        self.horizontalLayout.addWidget(self.ps_label)
        self.base_table_layout.addWidget(self.table_header_frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 998, 610))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_to_list_button = QtWidgets.QPushButton(self.frame)
        self.add_to_list_button.setMaximumSize(QtCore.QSize(20, 16777215))
        self.add_to_list_button.setObjectName("add_to_list_button")
        self.horizontalLayout_4.addWidget(self.add_to_list_button)
        spacerItem = QtWidgets.QSpacerItem(811, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.base_table_layout.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.base_table_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menuList = QtWidgets.QMenu(self.menubar)
        self.menuList.setObjectName("menuList")
        self.menuCharacter = QtWidgets.QMenu(self.menubar)
        self.menuCharacter.setObjectName("menuCharacter")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionCreate_New = QtWidgets.QAction(MainWindow)
        self.actionCreate_New.setObjectName("actionCreate_New")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.menuList.addAction(self.actionNew)
        self.menuList.addAction(self.actionSave)
        self.menuList.addAction(self.actionLoad)
        self.menuCharacter.addAction(self.actionCreate_New)
        self.menuCharacter.addAction(self.actionEdit)
        self.menubar.addAction(self.menuList.menuAction())
        self.menubar.addAction(self.menuCharacter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Testing"))
        self.testing_name_label.setText(_translate("MainWindow", "Name"))
        self.testing_roll_label.setText(_translate("MainWindow", "Roll"))
        self.ps_label.setText(_translate("MainWindow", "PS"))
        self.add_to_list_button.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Roll Dice"))
        self.menuList.setTitle(_translate("MainWindow", "List"))
        self.menuCharacter.setTitle(_translate("MainWindow", "Character"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionCreate_New.setText(_translate("MainWindow", "New"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
