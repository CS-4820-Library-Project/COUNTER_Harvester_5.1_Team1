# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditVendors51.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editVendors51(object):
    def setupUi(self, editVendors51):
        editVendors51.setObjectName("editVendors51")
        editVendors51.resize(597, 725)
        editVendors51.setStyleSheet("*{\n"
"    \n"
"    \n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"#QLineEdit{\n"
"color:black;\n"
"}\n"
"#QDateEdit{\n"
"color:black;}\n"
"\n"
"\n"
"#centralwidget{\n"
"background-color:#1f232a;\n"
"}\n"
"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.centralwidget = QtWidgets.QWidget(editVendors51)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EditVendor = QtWidgets.QWidget(self.centralwidget)
        self.EditVendor.setObjectName("EditVendor")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.EditVendor)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.EditVendor)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.edit_vendor_options_frame = QtWidgets.QFrame(self.frame_3)
        self.edit_vendor_options_frame.setEnabled(True)
        self.edit_vendor_options_frame.setStyleSheet("QFrame {\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;}\n"
"\n"
"\n"
"")
        self.edit_vendor_options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_vendor_options_frame.setObjectName("edit_vendor_options_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.edit_vendor_options_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saveVendorChangesButton = QtWidgets.QPushButton(self.edit_vendor_options_frame)
        self.saveVendorChangesButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.saveVendorChangesButton.setFont(font)
        self.saveVendorChangesButton.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../latestUI/resources/Icons/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveVendorChangesButton.setIcon(icon)
        self.saveVendorChangesButton.setDefault(False)
        self.saveVendorChangesButton.setFlat(False)
        self.saveVendorChangesButton.setObjectName("saveVendorChangesButton")
        self.horizontalLayout_5.addWidget(self.saveVendorChangesButton)
        self.undoVendorChangesButton = QtWidgets.QPushButton(self.edit_vendor_options_frame)
        self.undoVendorChangesButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.undoVendorChangesButton.setFont(font)
        self.undoVendorChangesButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(66, 66, 66); \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../latestUI/resources/Icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoVendorChangesButton.setIcon(icon1)
        self.undoVendorChangesButton.setObjectName("undoVendorChangesButton")
        self.horizontalLayout_5.addWidget(self.undoVendorChangesButton)
        self.removeVendorButton = QtWidgets.QPushButton(self.edit_vendor_options_frame)
        self.removeVendorButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.removeVendorButton.setFont(font)
        self.removeVendorButton.setStyleSheet("QPushButton {\n"
"    background-color: #E0383F; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 4px;\n"
"text-align: center;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../latestUI/resources/Icons/trash-can.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeVendorButton.setIcon(icon2)
        self.removeVendorButton.setObjectName("removeVendorButton")
        self.horizontalLayout_5.addWidget(self.removeVendorButton)
        self.gridLayout_6.addWidget(self.edit_vendor_options_frame, 2, 0, 1, 1)
        self.edit_vendor_details_frame = QtWidgets.QFrame(self.frame_3)
        self.edit_vendor_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_vendor_details_frame.setObjectName("edit_vendor_details_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.edit_vendor_details_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 13, 1, 1, 1)
        self.url_validation_label = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.url_validation_label.setText("")
        self.url_validation_label.setObjectName("url_validation_label")
        self.gridLayout_5.addWidget(self.url_validation_label, 6, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 10, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.nameEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"background-color: #2E2F30;\n"
"}\n"
"\n"
"")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_5.addWidget(self.nameEdit, 1, 3, 1, 1)
        self.apiKeyEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.apiKeyEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.apiKeyEdit.setObjectName("apiKeyEdit")
        self.gridLayout_5.addWidget(self.apiKeyEdit, 12, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 1, 1, 1)
        self.versionEdit = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.versionEdit.setObjectName("versionEdit")
        self.gridLayout_5.addWidget(self.versionEdit, 0, 3, 1, 1)
        self.provider = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.provider.setFont(font)
        self.provider.setObjectName("provider")
        self.gridLayout_5.addWidget(self.provider, 17, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)
        self.two_attempts_check_box = QtWidgets.QCheckBox(self.edit_vendor_details_frame)
        self.two_attempts_check_box.setText("")
        self.two_attempts_check_box.setObjectName("two_attempts_check_box")
        self.gridLayout_5.addWidget(self.two_attempts_check_box, 13, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 13, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 8, 0, 1, 1)
        self.baseUrlEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.baseUrlEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.baseUrlEdit.setObjectName("baseUrlEdit")
        self.gridLayout_5.addWidget(self.baseUrlEdit, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 5, 0, 1, 1)
        self.customerIdEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.customerIdEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.customerIdEdit.setObjectName("customerIdEdit")
        self.gridLayout_5.addWidget(self.customerIdEdit, 8, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 15, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 14, 1, 1, 1)
        self.platformEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.platformEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.platformEdit.setObjectName("platformEdit")
        self.gridLayout_5.addWidget(self.platformEdit, 10, 3, 1, 1)
        self.name_validation_label = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.name_validation_label.setText("")
        self.name_validation_label.setObjectName("name_validation_label")
        self.gridLayout_5.addWidget(self.name_validation_label, 2, 3, 1, 1)
        self.ip_checking_check_box = QtWidgets.QCheckBox(self.edit_vendor_details_frame)
        self.ip_checking_check_box.setText("")
        self.ip_checking_check_box.setObjectName("ip_checking_check_box")
        self.gridLayout_5.addWidget(self.ip_checking_check_box, 14, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 15, 0, 1, 1)
        self.label56 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        self.label56.setObjectName("label56")
        self.gridLayout_5.addWidget(self.label56, 5, 1, 1, 1)
        self.requestorIdEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.requestorIdEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.requestorIdEdit.setObjectName("requestorIdEdit")
        self.gridLayout_5.addWidget(self.requestorIdEdit, 9, 3, 1, 1)
        self.All_reports_edit_fetch = QtWidgets.QDateEdit(self.edit_vendor_details_frame)
        self.All_reports_edit_fetch.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.All_reports_edit_fetch.sizePolicy().hasHeightForWidth())
        self.All_reports_edit_fetch.setSizePolicy(sizePolicy)
        self.All_reports_edit_fetch.setStyleSheet("QDateEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.All_reports_edit_fetch.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 25), QtCore.QTime(0, 0, 0)))
        self.All_reports_edit_fetch.setObjectName("All_reports_edit_fetch")
        self.gridLayout_5.addWidget(self.All_reports_edit_fetch, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.edit_vendor_details_frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 16, 0, 1, 1)
        self.requests_throttled_check_box = QtWidgets.QCheckBox(self.edit_vendor_details_frame)
        self.requests_throttled_check_box.setText("")
        self.requests_throttled_check_box.setObjectName("requests_throttled_check_box")
        self.gridLayout_5.addWidget(self.requests_throttled_check_box, 15, 3, 1, 1)
        self.notesEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesEdit.sizePolicy().hasHeightForWidth())
        self.notesEdit.setSizePolicy(sizePolicy)
        self.notesEdit.setMinimumSize(QtCore.QSize(339, 0))
        self.notesEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.notesEdit.setObjectName("notesEdit")
        self.gridLayout_5.addWidget(self.notesEdit, 16, 3, 1, 1)
        self.providerEdit = QtWidgets.QLineEdit(self.edit_vendor_details_frame)
        self.providerEdit.setStyleSheet("QLineEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.providerEdit.setObjectName("providerEdit")
        self.gridLayout_5.addWidget(self.providerEdit, 17, 3, 1, 1)
        self.gridLayout_6.addWidget(self.edit_vendor_details_frame, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.EditVendor, 0, 0, 1, 1)
        editVendors51.setCentralWidget(self.centralwidget)

        self.retranslateUi(editVendors51)
        QtCore.QMetaObject.connectSlotsByName(editVendors51)
        editVendors51.setTabOrder(self.nameEdit, self.baseUrlEdit)
        editVendors51.setTabOrder(self.baseUrlEdit, self.All_reports_edit_fetch)
        editVendors51.setTabOrder(self.All_reports_edit_fetch, self.customerIdEdit)
        editVendors51.setTabOrder(self.customerIdEdit, self.requestorIdEdit)
        editVendors51.setTabOrder(self.requestorIdEdit, self.platformEdit)
        editVendors51.setTabOrder(self.platformEdit, self.apiKeyEdit)
        editVendors51.setTabOrder(self.apiKeyEdit, self.two_attempts_check_box)
        editVendors51.setTabOrder(self.two_attempts_check_box, self.ip_checking_check_box)
        editVendors51.setTabOrder(self.ip_checking_check_box, self.requests_throttled_check_box)
        editVendors51.setTabOrder(self.requests_throttled_check_box, self.notesEdit)
        editVendors51.setTabOrder(self.notesEdit, self.providerEdit)
        editVendors51.setTabOrder(self.providerEdit, self.saveVendorChangesButton)
        editVendors51.setTabOrder(self.saveVendorChangesButton, self.undoVendorChangesButton)
        editVendors51.setTabOrder(self.undoVendorChangesButton, self.removeVendorButton)

    def retranslateUi(self, editVendors51):
        _translate = QtCore.QCoreApplication.translate
        editVendors51.setWindowTitle(_translate("editVendors51", "MainWindow"))
        self.label_7.setText(_translate("editVendors51", "Edit Vendor"))
        self.saveVendorChangesButton.setText(_translate("editVendors51", "Save Changes"))
        self.undoVendorChangesButton.setText(_translate("editVendors51", "Undo Changes"))
        self.removeVendorButton.setText(_translate("editVendors51", "Remove Vendor"))
        self.label_10.setText(_translate("editVendors51", "Starting Year"))
        self.label_5.setText(_translate("editVendors51", "API Key"))
        self.label_4.setText(_translate("editVendors51", "Requester ID"))
        self.label_15.setText(_translate("editVendors51", "*"))
        self.label_13.setText(_translate("editVendors51", "*"))
        self.label_9.setText(_translate("editVendors51", "IP Checking"))
        self.label_6.setText(_translate("editVendors51", "Platform"))
        self.label_14.setText(_translate("editVendors51", "*"))
        self.label_12.setText(_translate("editVendors51", "*"))
        self.versionEdit.setText(_translate("editVendors51", "5.1"))
        self.provider.setText(_translate("editVendors51", "Provider"))
        self.label_19.setText(_translate("editVendors51", "Version"))
        self.label_8.setText(_translate("editVendors51", "2 Attempts needed"))
        self.label_3.setText(_translate("editVendors51", "Customer ID"))
        self.label_2.setText(_translate("editVendors51", "Base URL"))
        self.label_17.setText(_translate("editVendors51", "*"))
        self.label_16.setText(_translate("editVendors51", "*"))
        self.label_11.setText(_translate("editVendors51", "Request throttled"))
        self.label56.setText(_translate("editVendors51", "*"))
        self.All_reports_edit_fetch.setDisplayFormat(_translate("editVendors51", "yyyy"))
        self.label.setText(_translate("editVendors51", "Name"))
        self.label_28.setText(_translate("editVendors51", "Notes"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editVendors51 = QtWidgets.QMainWindow()
    ui = Ui_editVendors51()
    ui.setupUi(editVendors51)
    editVendors51.show()
    sys.exit(app.exec_())
