# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(598, 480))
        MainWindow.setMaximumSize(QtCore.QSize(598, 480))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 351, 361))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(16, 39, 328, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.name_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 0, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_label.setMinimumSize(QtCore.QSize(30, 0))
        self.name_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.gender_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.gender_comboBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gridLayout.addWidget(self.gender_comboBox, 0, 3, 1, 1)
        self.gender_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gender_label.setMinimumSize(QtCore.QSize(30, 0))
        self.gender_label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.gender_label.setObjectName("gender_label")
        self.gridLayout.addWidget(self.gender_label, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.birth_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.birth_label.setMinimumSize(QtCore.QSize(30, 0))
        self.birth_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.birth_label.setObjectName("birth_label")
        self.gridLayout_3.addWidget(self.birth_label, 0, 0, 1, 1)
        self.retire_age_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.retire_age_comboBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.retire_age_comboBox.setObjectName("retire_age_comboBox")
        self.gridLayout_3.addWidget(self.retire_age_comboBox, 0, 3, 1, 1)
        self.birthday_dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.birthday_dateEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.birthday_dateEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.birthday_dateEdit.setObjectName("birthday_dateEdit")
        self.gridLayout_3.addWidget(self.birthday_dateEdit, 0, 1, 1, 1)
        self.retire_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.retire_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.retire_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.retire_label.setObjectName("retire_label")
        self.gridLayout_3.addWidget(self.retire_label, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.company_out_time_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.company_out_time_label.setObjectName("company_out_time_label")
        self.gridLayout_2.addWidget(self.company_out_time_label, 0, 1, 1, 1)
        self.company_in_dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.company_in_dateEdit.setObjectName("company_in_dateEdit")
        self.gridLayout_2.addWidget(self.company_in_dateEdit, 1, 0, 1, 1)
        self.company_out_dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.company_out_dateEdit.setObjectName("company_out_dateEdit")
        self.gridLayout_2.addWidget(self.company_out_dateEdit, 1, 1, 1, 1)
        self.company_in_time_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.company_in_time_label.setObjectName("company_in_time_label")
        self.gridLayout_2.addWidget(self.company_in_time_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.working_suspend_year_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.working_suspend_year_lineEdit.setObjectName("working_suspend_year_lineEdit")
        self.horizontalLayout.addWidget(self.working_suspend_year_lineEdit)
        self.year_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.year_label.setObjectName("year_label")
        self.horizontalLayout.addWidget(self.year_label)
        self.working_suspend_month_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.working_suspend_month_lineEdit.setObjectName("working_suspend_month_lineEdit")
        self.horizontalLayout.addWidget(self.working_suspend_month_lineEdit)
        self.month_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.month_label.setObjectName("month_label")
        self.horizontalLayout.addWidget(self.month_label)
        self.working_suspend_day_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.working_suspend_day_lineEdit.setObjectName("working_suspend_day_lineEdit")
        self.horizontalLayout.addWidget(self.working_suspend_day_lineEdit)
        self.day_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.day_label.setObjectName("day_label")
        self.horizontalLayout.addWidget(self.day_label)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.working_start_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.working_start_label.setObjectName("working_start_label")
        self.gridLayout_4.addWidget(self.working_start_label, 0, 0, 1, 1)
        self.working_suspend_time_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.working_suspend_time_label.setObjectName("working_suspend_time_label")
        self.gridLayout_4.addWidget(self.working_suspend_time_label, 0, 1, 1, 1)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.gridLayout_4.addWidget(self.dateEdit_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.personal_average_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.personal_average_label.setObjectName("personal_average_label")
        self.gridLayout_5.addWidget(self.personal_average_label, 0, 0, 1, 1)
        self.society_average_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.society_average_label.setObjectName("society_average_label")
        self.gridLayout_5.addWidget(self.society_average_label, 0, 1, 1, 1)
        self.society_average_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.society_average_lineEdit.setObjectName("society_average_lineEdit")
        self.gridLayout_5.addWidget(self.society_average_lineEdit, 1, 1, 1, 1)
        self.personal_average_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.personal_average_lineEdit.setObjectName("personal_average_lineEdit")
        self.gridLayout_5.addWidget(self.personal_average_lineEdit, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(420, 330, 151, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 101, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.generate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.generate_pushButton.setMinimumSize(QtCore.QSize(90, 31))
        self.generate_pushButton.setMaximumSize(QtCore.QSize(90, 31))
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.verticalLayout_3.addWidget(self.generate_pushButton)
        self.xls_calculate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.xls_calculate_pushButton.setMinimumSize(QtCore.QSize(90, 31))
        self.xls_calculate_pushButton.setMaximumSize(QtCore.QSize(90, 31))
        self.xls_calculate_pushButton.setObjectName("xls_calculate_pushButton")
        self.verticalLayout_3.addWidget(self.xls_calculate_pushButton)
        self.xls_label = QtWidgets.QLabel(self.centralWidget)
        self.xls_label.setGeometry(QtCore.QRect(350, 400, 101, 20))
        self.xls_label.setObjectName("xls_label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(429, 20, 131, 301))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 111, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.time_to_retire_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_to_retire_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.time_to_retire_label.setObjectName("time_to_retire_label")
        self.verticalLayout_2.addWidget(self.time_to_retire_label)
        self.time_to_retire_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.time_to_retire_lineEdit.setEnabled(True)
        self.time_to_retire_lineEdit.setReadOnly(True)
        self.time_to_retire_lineEdit.setObjectName("time_to_retire_lineEdit")
        self.verticalLayout_2.addWidget(self.time_to_retire_lineEdit)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.working_years_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.working_years_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.working_years_label.setObjectName("working_years_label")
        self.verticalLayout_2.addWidget(self.working_years_label)
        self.working_years_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.working_years_lineEdit.setReadOnly(True)
        self.working_years_lineEdit.setObjectName("working_years_lineEdit")
        self.verticalLayout_2.addWidget(self.working_years_lineEdit)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.compensation_money_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.compensation_money_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.compensation_money_label.setObjectName("compensation_money_label")
        self.verticalLayout_2.addWidget(self.compensation_money_label)
        self.working_years_lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.working_years_lineEdit_2.setReadOnly(True)
        self.working_years_lineEdit_2.setObjectName("working_years_lineEdit_2")
        self.verticalLayout_2.addWidget(self.working_years_lineEdit_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(False)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 598, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "退休金计算器"))
        self.groupBox.setTitle(_translate("MainWindow", "数据输入"))
        self.name_label.setText(_translate("MainWindow", "姓名:"))
        self.gender_label.setText(_translate("MainWindow", "  性别:"))
        self.birth_label.setText(_translate("MainWindow", "生日:"))
        self.retire_label.setText(_translate("MainWindow", "退休年龄:"))
        self.company_out_time_label.setText(_translate("MainWindow", "从本单位离职时间"))
        self.company_in_time_label.setText(_translate("MainWindow", "进本单位时间"))
        self.year_label.setText(_translate("MainWindow", "年"))
        self.month_label.setText(_translate("MainWindow", "月"))
        self.day_label.setText(_translate("MainWindow", "日"))
        self.working_start_label.setText(_translate("MainWindow", "个人开始工作时间"))
        self.working_suspend_time_label.setText(_translate("MainWindow", "未上班累计时间"))
        self.personal_average_label.setText(_translate("MainWindow", "上年度个人平均工资(元)"))
        self.society_average_label.setText(_translate("MainWindow", "上年度社会平均工资(元)"))
        self.generate_pushButton.setText(_translate("MainWindow", "输出"))
        self.xls_calculate_pushButton.setText(_translate("MainWindow", "批量计算"))
        self.xls_label.setText(_translate("MainWindow", "文件名: data.xls"))
        self.groupBox_3.setTitle(_translate("MainWindow", "计算结果"))
        self.time_to_retire_label.setText(_translate("MainWindow", "距离退休时间"))
        self.working_years_label.setText(_translate("MainWindow", "累计工龄"))
        self.compensation_money_label.setText(_translate("MainWindow", "赔偿金额"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

