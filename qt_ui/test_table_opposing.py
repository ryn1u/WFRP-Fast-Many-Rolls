# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_table_opposing.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 688)
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.table_header_frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.line_4 = QtWidgets.QFrame(self.table_header_frame)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.testing_name_label_2 = QtWidgets.QLabel(self.table_header_frame)
        self.testing_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.testing_name_label_2.setObjectName("testing_name_label_2")
        self.horizontalLayout_5.addWidget(self.testing_name_label_2)
        self.test_skill_list_left = QtWidgets.QComboBox(self.table_header_frame)
        self.test_skill_list_left.setObjectName("test_skill_list_left")
        self.horizontalLayout_5.addWidget(self.test_skill_list_left)
        self.testing_roll_label_2 = QtWidgets.QLabel(self.table_header_frame)
        self.testing_roll_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.testing_roll_label_2.setObjectName("testing_roll_label_2")
        self.horizontalLayout_5.addWidget(self.testing_roll_label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
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
        self.label_4 = QtWidgets.QLabel(self.table_header_frame)
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.table_header_frame)
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.table_header_frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
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
        self.test_skill_list_right = QtWidgets.QComboBox(self.table_header_frame)
        self.test_skill_list_right.setObjectName("test_skill_list_right")
        self.horizontalLayout_2.addWidget(self.test_skill_list_right)
        self.testing_roll_label = QtWidgets.QLabel(self.table_header_frame)
        self.testing_roll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.testing_roll_label.setObjectName("testing_roll_label")
        self.horizontalLayout_2.addWidget(self.testing_roll_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.base_table_layout.addWidget(self.table_header_frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollAreaLeft = QtWidgets.QScrollArea(self.frame_2)
        self.scrollAreaLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollAreaLeft.setWidgetResizable(True)
        self.scrollAreaLeft.setObjectName("scrollAreaLeft")
        self.scrollAreaWidgetLeft = QtWidgets.QWidget()
        self.scrollAreaWidgetLeft.setGeometry(QtCore.QRect(0, 0, 429, 492))
        self.scrollAreaWidgetLeft.setObjectName("scrollAreaWidgetLeft")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetLeft)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_btn_frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetLeft)
        self.add_btn_frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.add_btn_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_btn_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_btn_frame_2.setObjectName("add_btn_frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.add_btn_frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_to_list_button_left = QtWidgets.QPushButton(self.add_btn_frame_2)
        self.add_to_list_button_left.setMaximumSize(QtCore.QSize(20, 16777215))
        self.add_to_list_button_left.setObjectName("add_to_list_button_left")
        self.horizontalLayout_6.addWidget(self.add_to_list_button_left)
        spacerItem = QtWidgets.QSpacerItem(811, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.add_btn_frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.scrollAreaLeft.setWidget(self.scrollAreaWidgetLeft)
        self.horizontalLayout_7.addWidget(self.scrollAreaLeft)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(80, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(20, 471, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_7.addWidget(self.frame)
        self.scrollAreaRight = QtWidgets.QScrollArea(self.frame_2)
        self.scrollAreaRight.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollAreaRight.setWidgetResizable(True)
        self.scrollAreaRight.setObjectName("scrollAreaRight")
        self.scrollAreaWidgetRight = QtWidgets.QWidget()
        self.scrollAreaWidgetRight.setGeometry(QtCore.QRect(0, 0, 429, 492))
        self.scrollAreaWidgetRight.setObjectName("scrollAreaWidgetRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetRight)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_btn_frame = QtWidgets.QFrame(self.scrollAreaWidgetRight)
        self.add_btn_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.add_btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_btn_frame.setObjectName("add_btn_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.add_btn_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(811, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.add_to_list_button_right = QtWidgets.QPushButton(self.add_btn_frame)
        self.add_to_list_button_right.setMaximumSize(QtCore.QSize(20, 16777215))
        self.add_to_list_button_right.setObjectName("add_to_list_button_right")
        self.horizontalLayout_4.addWidget(self.add_to_list_button_right)
        self.verticalLayout_3.addWidget(self.add_btn_frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.scrollAreaRight.setWidget(self.scrollAreaWidgetRight)
        self.horizontalLayout_7.addWidget(self.scrollAreaRight)
        self.base_table_layout.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.base_table_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.only_positive_check = QtWidgets.QCheckBox(self.centralwidget)
        self.only_positive_check.setObjectName("only_positive_check")
        self.horizontalLayout_3.addWidget(self.only_positive_check)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.difficulty_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.difficulty_spin_box.setMinimumSize(QtCore.QSize(50, 0))
        self.difficulty_spin_box.setMinimum(-100)
        self.difficulty_spin_box.setMaximum(100)
        self.difficulty_spin_box.setObjectName("difficulty_spin_box")
        self.horizontalLayout_3.addWidget(self.difficulty_spin_box)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.horizontalLayout_3.addWidget(self.result_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 22))
        self.menubar.setObjectName("menubar")
        self.menuList = QtWidgets.QMenu(self.menubar)
        self.menuList.setObjectName("menuList")
        self.menuCharacter = QtWidgets.QMenu(self.menubar)
        self.menuCharacter.setObjectName("menuCharacter")
        MainWindow.setMenuBar(self.menubar)
        self.actionListNew = QtWidgets.QAction(MainWindow)
        self.actionListNew.setObjectName("actionListNew")
        self.actionListSave = QtWidgets.QAction(MainWindow)
        self.actionListSave.setObjectName("actionListSave")
        self.actionListLoad = QtWidgets.QAction(MainWindow)
        self.actionListLoad.setObjectName("actionListLoad")
        self.actionCaracterNew = QtWidgets.QAction(MainWindow)
        self.actionCaracterNew.setObjectName("actionCaracterNew")
        self.actionCharacterEdit = QtWidgets.QAction(MainWindow)
        self.actionCharacterEdit.setObjectName("actionCharacterEdit")
        self.menuList.addAction(self.actionListNew)
        self.menuList.addAction(self.actionListSave)
        self.menuList.addAction(self.actionListLoad)
        self.menuCharacter.addAction(self.actionCaracterNew)
        self.menuCharacter.addAction(self.actionCharacterEdit)
        self.menubar.addAction(self.menuList.menuAction())
        self.menubar.addAction(self.menuCharacter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Testing"))
        self.testing_name_label_2.setText(_translate("MainWindow", "Name"))
        self.testing_roll_label_2.setText(_translate("MainWindow", "Roll"))
        self.ps_label.setText(_translate("MainWindow", "PS"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.label_5.setText(_translate("MainWindow", "PS"))
        self.label_2.setText(_translate("MainWindow", "Testing"))
        self.testing_name_label.setText(_translate("MainWindow", "Name"))
        self.testing_roll_label.setText(_translate("MainWindow", "Roll"))
        self.add_to_list_button_left.setText(_translate("MainWindow", "+"))
        self.add_to_list_button_right.setText(_translate("MainWindow", "+"))
        self.only_positive_check.setText(_translate("MainWindow", "Only Positive"))
        self.pushButton.setText(_translate("MainWindow", "Roll Dice"))
        self.label.setText(_translate("MainWindow", "Difficulty"))
        self.menuList.setTitle(_translate("MainWindow", "List"))
        self.menuCharacter.setTitle(_translate("MainWindow", "Character"))
        self.actionListNew.setText(_translate("MainWindow", "New"))
        self.actionListSave.setText(_translate("MainWindow", "Save"))
        self.actionListLoad.setText(_translate("MainWindow", "Load"))
        self.actionCaracterNew.setText(_translate("MainWindow", "New"))
        self.actionCharacterEdit.setText(_translate("MainWindow", "Edit"))