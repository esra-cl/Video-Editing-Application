# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayuz2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(872, 789)
        Form.setStyleSheet(u"#label1{\n"
"font: 12pt \"MS Sans Serif\";\n"
"}")
        self.pushButton_basframe = QPushButton(Form)
        self.pushButton_basframe.setObjectName(u"pushButton_basframe")
        self.pushButton_basframe.setGeometry(QRect(740, 450, 111, 41))
        self.pushButton_basframe.setStyleSheet(u"#pushButton_basframe{\n"
"background-color: rgb(0, 170, 127);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 10, 621, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_kaydet = QPushButton(Form)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")
        self.pushButton_kaydet.setGeometry(QRect(760, 360, 71, 41))
        self.pushButton_kaydet.setStyleSheet(u"#pushButton_kaydet{\n"
"background-color: rgb(226, 0, 0);\n"
"border-radius:20px;\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_play = QPushButton(Form)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setGeometry(QRect(180, 580, 71, 61))
        self.pushButton_play.setStyleSheet(u"#pushButton_play{\n"
"background-color: rgb(77, 154, 0);\n"
"border-radius:30px;\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(100, 350, 631, 61))
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"background-color: rgb(213, 213, 213);\n"
"border-radius:30px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 20, 801, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 420, 631, 151))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 641, 131))
        self.scroll_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.scroll_layout.setSpacing(0)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_videosec = QPushButton(Form)
        self.pushButton_videosec.setObjectName(u"pushButton_videosec")
        self.pushButton_videosec.setGeometry(QRect(100, 580, 71, 61))
        self.pushButton_videosec.setStyleSheet(u"#pushButton_videosec{\n"
"background-color: rgb(234, 156, 116);\n"
"border-radius:30px;\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.pushButton_bitisframe = QPushButton(Form)
        self.pushButton_bitisframe.setObjectName(u"pushButton_bitisframe")
        self.pushButton_bitisframe.setGeometry(QRect(740, 520, 111, 41))
        self.pushButton_bitisframe.setStyleSheet(u"#pushButton_bitisframe{\n"
"background-color: rgb(0, 170, 127);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.path_label = QLabel(Form)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(270, 600, 461, 41))
        self.path_label.setStyleSheet(u"#path_label {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}")
        self.path_label.setTextFormat(Qt.RichText)
        self.path_label.setScaledContents(True)
        self.path_lb = QLabel(Form)
        self.path_lb.setObjectName(u"path_lb")
        self.path_lb.setGeometry(QRect(280, 580, 171, 16))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        self.path_lb.setFont(font)
        self.guidances_label = QLabel(Form)
        self.guidances_label.setObjectName(u"guidances_label")
        self.guidances_label.setGeometry(QRect(90, 680, 711, 20))
        self.pushButton_select = QPushButton(Form)
        self.pushButton_select.setObjectName(u"pushButton_select")
        self.pushButton_select.setGeometry(QRect(740, 600, 111, 41))
        self.pushButton_select.setAutoFillBackground(False)
        self.pushButton_select.setStyleSheet(u"#pushButton_select{\n"
"background-color: rgb(0, 170, 127);\n"
"border-radius:20px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 650, 211, 10))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(98)
        self.progressBar.setValue(0)
        self.loading = QLabel(Form)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(100, 660, 201, 16))
        self.ilkframe_lbl = QLabel(Form)
        self.ilkframe_lbl.setObjectName(u"ilkframe_lbl")
        self.ilkframe_lbl.setGeometry(QRect(740, 430, 121, 16))
        self.sonframe_lbl = QLabel(Form)
        self.sonframe_lbl.setObjectName(u"sonframe_lbl")
        self.sonframe_lbl.setGeometry(QRect(740, 500, 121, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_basframe.setText(QCoreApplication.translate("Form", u"Ba\u015flang\u0131\u00e7 Frame Se\u00e7", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.pushButton_play.setText(QCoreApplication.translate("Form", u"Play", None))
        self.groupBox.setTitle("")
        self.pushButton_videosec.setText(QCoreApplication.translate("Form", u"Video Se\u00e7", None))
        self.pushButton_bitisframe.setText(QCoreApplication.translate("Form", u"Biti\u015f Frame Se\u00e7", None))
        self.path_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.path_lb.setText(QCoreApplication.translate("Form", u"Se\u00e7ilen Veri Kay\u0131t Yolu", None))
        self.guidances_label.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_select.setText(QCoreApplication.translate("Form", u"Se\u00e7", None))
        self.loading.setText(QCoreApplication.translate("Form", u"y\u00fckleniyor...", None))
        self.ilkframe_lbl.setText("")
        self.sonframe_lbl.setText("")
    # retranslateUi

