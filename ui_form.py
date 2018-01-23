# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try5.ui'
#
# Created: Thu Apr 16 23:04:49 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton)

import sandhi_splitter_driver_mod
from sandhi_splitter_driver_mod import *

import spell_check_driver_mod
from spell_check_driver_mod import *

import pratyaya_chopper_driver_mod
from pratyaya_chopper_driver_mod import *

import file_input_strip
from file_input_strip import *

import textedit
from textedit import *

import semantic12
from semantic12 import *
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 1100)
        Form.setMaximumSize(QtCore.QSize(1100, 1100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 83, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 83, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 83, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        Form.setPalette(palette)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_language_combo = QtWidgets.QComboBox(Form)
        self.input_language_combo.setGeometry(QtCore.QRect(510, 50, 289, 41))
        self.input_language_combo.setMinimumSize(QtCore.QSize(289, 27))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_language_combo.setFont(font)
        self.input_language_combo.setObjectName("input_language_combo")
        self.input_language_combo.addItem("")
        self.input_language_combo.addItem("")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 110, 1011, 16))
        self.line.setMinimumSize(QtCore.QSize(200, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 131, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 180, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 240, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(700, 190, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(50, 300, 981, 16))
        self.line_2.setMinimumSize(QtCore.QSize(200, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 320, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.single_word = QtWidgets.QPushButton(Form)
        self.single_word.setGeometry(QtCore.QRect(120, 380, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.single_word.setFont(font)
        self.single_word.setMouseTracking(True)
        self.single_word.setObjectName("single_word")
        self.file_input = QtWidgets.QPushButton(Form)
        self.file_input.setGeometry(QtCore.QRect(690, 380, 291, 41))
        self.file_input.setMinimumSize(QtCore.QSize(289, 27))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.file_input.setFont(font)
        self.file_input.setMouseTracking(True)
        self.file_input.setObjectName("file_input")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(60, 490, 981, 16))
        self.line_3.setMinimumSize(QtCore.QSize(200, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(380, 530, 331, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.submit.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setAutoFillBackground(True)
        self.submit.setObjectName("submit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 600, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(60, 650, 981, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(60, 720, 981, 321))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.given_input = QtWidgets.QLabel(Form)
        self.given_input.setGeometry(QtCore.QRect(60, 430, 961, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.given_input.setFont(font)
        self.given_input.setText("")
        self.given_input.setObjectName("given_input")
        self.apply_encoding = QtWidgets.QPushButton(Form)
        self.apply_encoding.setGeometry(QtCore.QRect(880, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.apply_encoding.setFont(font)
        self.apply_encoding.setObjectName("apply_encoding")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(1070, 20, 20, 1061))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(20, 1070, 1061, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(10, 20, 20, 1061))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(20, 10, 1061, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(700, 250, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select Input Encoding: "))
        self.input_language_combo.setItemText(0, _translate("Form", "English"))
        self.input_language_combo.setItemText(1, _translate("Form", "Kannada"))
        self.label_2.setText(_translate("Form", "Select Mode:"))
        self.radioButton_3.setText(_translate("Form", "Spell Checker with Sandhi Splitter"))
        self.radioButton_2.setText(_translate("Form", "Sandhi Splitter"))
        self.radioButton.setText(_translate("Form", "Root word extractor"))
        self.label_3.setText(_translate("Form", "Provide Input:"))
        self.single_word.setText(_translate("Form", "Single Word "))
        self.file_input.setText(_translate("Form", "File Input"))
        self.submit.setText(_translate("Form", "Submit"))
        self.label_4.setText(_translate("Form", "Output:"))
        self.apply_encoding.setText(_translate("Form", "Apply"))
        self.radioButton_4.setText(_translate("Form", "Semantic Analyser"))
        self.single_word.clicked.connect(self.setText)
        self.file_input.clicked.connect(self.setOpenFileName)
        self.apply_encoding.clicked.connect(self.change_encoding)
        self.submit.clicked.connect(self.submit_clicked)
    
    def open_popup(self):
    	textLabel = QLabel()
    	textButton = QPushButton("QInputDialog.get&Text()")
    	print(textButton)
    	textButton.clicked.connect(self.setText)
    	
    def setText(self):
        self.progressBar.setProperty("value", 0)
        global given_input
        self.textBrowser.setText("")
        self.given_input.setText("")
        dialog=Dialog()
        if self.input_language_combo.currentIndex()==1:
        	text, ok = QInputDialog.getText(dialog, "ಪದ",
                "ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ : ", QLineEdit.Normal,"")
        	if ok and text != '':
        		print(text)
        		provided_input="ದಾಖಲಿಸಿದ ಪದ : "+text
        		self.given_input.setText(provided_input)
        else:
        	text, ok = QInputDialog.getText(dialog, "Single word",
                "Enter the input:", QLineEdit.Normal,"")
        	if ok and text != '':           
        	    print(text)
        	    provided_input="The given input : "+text
        	    self.given_input.setText(provided_input)
        given_input=text
        
		
    def setOpenFileName(self):    
        options = QFileDialog.Options()
        self.progressBar.setProperty("value", 0)
        global given_input
        self.textBrowser.setText("")
        self.given_input.setText("")
        dialog=Dialog()
      
        fileName, _ = QFileDialog.getOpenFileName(dialog,
                "Select file", "",
                "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            provided_input="Input file : "+fileName
            self.given_input.setText(provided_input)
        given_input=fileName
       
    def change_encoding(self):
    #so current index 0= english
    #current index 1 is kannada
    #if kannada is selected, change everything to kannada
    	self.given_input.setText("")
    	self.textBrowser.setText("")
    	self.progressBar.setProperty("value", 0)
    	if self.input_language_combo.currentIndex()==1:
    		self.label.setText("ಪದ ಸಂಕೇತೀಕರಣವನ್ನು ಸೂಚಿಸಿ ")
    		self.input_language_combo.setItemText(0,"ಆಂಗ್ಲ")
    		self.input_language_combo.setItemText(1, "ಕನ್ನಡ")
    		self.label_2.setText("ಇವುಗಳಲ್ಲಿ ಒಂದು ಕಾರ್ಯವನ್ನು ಆಯ್ದುಕೊಳ್ಳಿರಿ : ")
    		self.radioButton_3.setText("ಪದ ಪರಿಶೀಲನೆ - ಸಂಧಿ ಛೇದದೊಡಗೂಡಿ")
    		self.radioButton_4.setText("ವಾಕ್ಯ ಪರಿಶೀಲನೆ")
    		self.radioButton_2.setText("ಸಂಧಿ ಛೇದ")
    		self.radioButton.setText("ಮೂಲ ಪದ ಉದ್ಧರಣ")
    		self.label_3.setText("ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ :")
    		self.single_word.setText("ಪದ")
    		self.file_input.setText("ವಾಕ್ಯವೃಂದ")
    		self.submit.setText("ಸಲ್ಲಿಸು")
    		self.label_4.setText("ಫಲಿತಾಂಶ : ")
    		self.apply_encoding.setText("ಒಪ್ಪಿಸು")
    	else:
    		self.label.setText("Select Input Encoding: ")
    		self.input_language_combo.setItemText(0,"English")
    		self.input_language_combo.setItemText(1, "Kannada")
    		self.label_2.setText("Select Mode:")
    		self.radioButton_3.setText("Spell Checker with Sandhi Splitter")
    		self.radioButton_4.setText("Semantic Analyser")
    		self.radioButton_2.setText("Sandhi Splitter")
    		self.radioButton.setText("Root word extractor")
    		self.label_3.setText("Provide Input:")
    		self.single_word.setText("Single Word")
    		self.file_input.setText("File Input")
    		self.submit.setText("Submit")
    		self.label_4.setText("Output:")
    		self.apply_encoding.setText("Apply")
    		 #"ಪರಿಶೀಲಿಸಲು ಬಯಸುವ ಪದ : ", QLineEdit.Normal,"")
    def called_file(self,given_file_input,mode,prnt_res):
    #this is to handle the file cases.
    #taking three arguments, first to self, second input, third mode, fourt language
    	print("file called")
    	file_path=given_file_input.split('/')
    	file_name=file_path[-1]
    	in_file=open(file_name,"r")
    	file_write=""
    	ignored_words=[]
    	final_pratyaya=""
    	if prnt_res==3:
    	#stuffs are in kannada
    		if mode==1:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							for word in words:
    								intact_word=word
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								found_print=spell_check_kan(word)
    								if found_print[0]==1:
    									
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]=="" or found_print[2]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ : "+word+"\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=intact_word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[2])>0:
    										dialog=Dialog()
    										ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]
    										#dialog.move(400,500)
    										item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ  ಮೂಲ ಪದ : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?  :",found_print[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,3)
    											print(selected)
    											if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												ignored_words.append(word)
    											if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												file_write+=intact_word+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												continue
    											
    											if after_pratyaya[0]==1:
    												pratyayas=after_pratyaya[4]
    												pr_len=len(pratyayas)
    												i=1
    												while i<=pr_len:
    													pr=pratyayas[-i]
    													print("word is",word)
    													print("pr is",pr)
    													if len(pr)==1:
    														final_pratyaya+=pr
    													else:
    														final_pratyaya+=pr[:-1]
    													i=i+1
    												final_pratyaya+=pr[-1]
    												print("final pr",final_pratyaya)
    												print("prinintin pratyays")
    												print(pratyayas)
    												file_write+=to_uni(to_roman(selected)+final_pratyaya)+" "
    												final_pratyaya=""
    												
    											else:
    												file_write+=selected+" "
    											self.textBrowser.setText(file_write)
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    			
    			
    		elif mode==2:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					sent_num=0
    					
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								file_write+="\n"+word+" :\n"    								
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])    									
    									file_write+=after_pratyaya[2]
    								
    								if word in ignored_words:
    									file_write+=word+" "
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									continue
    								
    								if after_pratyaya[3]==1:
    									file_write+="ಈ ಪದವು ಪದಕೋಶದಲ್ಲಿ ಲಭ್ಯವಿದೆ! ಈ ಪದವು ಸಂದಿಪದವಲ್ಲದಿರಬಹುದು!\n"
    									continue
    								found_print=sandhi_splitter_kan(word)
    								if found_print[0]==1:
    									file_write+=found_print[1]    										
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]==0 or found_print[3]=="" or found_print[3]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ : "+word+"\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[3])>0:
    										dialog=Dialog()
    										ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]
    										
    										item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ ಮೂಲ ಪದ  : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? ",found_print[3]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												ignored_words.append(word)
    											if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    												file_write+=word+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    											
    											
    											file_write+="ನೀವು ಆಯ್ದ ಪದ : "+selected+"\n "
    											found_print=sandhi_splitter_kan(selected)
    											file_write+=found_print[1]
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    		elif mode==3:
    	#this is for kannada pratyaya chopper
    			sent_num=0
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								intact_word=word
    								file_write+="\n"+word+" :\n"   
    								after_pratyaya=pratyaya_chopper(word,3)
    								if after_pratyaya[0]==1:
    									word=to_uni(after_pratyaya[1])
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								if after_pratyaya[3]==1:
    									file_write+="ಮೂಲ ಪದ  : "+to_uni(after_pratyaya[1])+"\n"
    									continue
    								else:
    								#check pratyaya has to_uni function in it
    									correct_selected=check_pratyaya(after_pratyaya[1],3)
    									print("cor",correct_selected[2])
    								
    									
    								if correct_selected[0]==1:    								
    									file_write+="\n"+after_pratyaya[2]+correct_selected[1]+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    									dialog=Dialog()
    									file_write+=after_pratyaya[2]+word+" : ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    									text, ok = QInputDialog.getText(dialog,"ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ : "+word+"\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    									if ok and text != '':
    										print(text)
    										add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    										if add_success==1:
    											QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    	   				
    						
    								else:	
    									dialog=Dialog()
    									ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]							    											    					
    									item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ ಮೂಲ ಪದ : "+word+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? :", correct_selected[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    									if ok and item:
    										print(item)
    										selected=pick_selected(item,1)
    										if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    											ignored_words.append(word)
    										if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    											file_write+="ಮೂಲ ಪದ : "+word+"\n "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    										after_pratyaya=pratyaya_chopper(selected,3)
    										if after_pratyaya[0]==1:
    											word=to_uni(after_pratyaya[1])
    										file_write+=after_pratyaya[2]+"ನೀವು ಆಯ್ದ ಮೂಲ ಪದ  : "+word+"\n"
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    									else:
		    								
		    								dialog=Dialog()
		    								text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
		    								if ok and text != '':
		    									print(text)
		    									add_success=add_word(text,3)
		    				# 1 coz stuffs in english
		    									if add_success==1:
		    										QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    		elif mode==4:
    	#this is for semantic stuff in eng
    			print("semantic called for file")
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						print("set",sentence)
    						file_write+="\n"
    						#self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						print("file",file_write)
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							if sentence in ignored_words:
    								file_write+=sentence+" "
    								self.textBrowser.setText(file_write)
    								QApplication.processEvents()
    								continue
    							ret_list=semantic(sentence,3)
    							if ret_list[0]==1:
    								sem_set=""
    								for sem_l in ret_list[1]:
    									sem_set+=sem_l+"\n"
    								file_write+=sem_set
    								self.textBrowser.setText(file_write)
    								self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    								continue
    							if ret_list[0]==0 and len(ret_list[2])==0: 
    								dialog=Dialog()
    								file_write+=sentence+" : ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!\n"
    								self.textBrowser.setText(file_write)
    								self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    								QApplication.processEvents()
    									
    								text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ : "+sentence+"\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    								if ok and text != '':
    									print(text)
    									add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    									if add_success==1:
    										QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    	   				
    						
    							elif ret_list[0]==0:	
    								dialog=Dialog()
    								ignore=["ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ", "ಸದಾ ಕಡೆಗಣಿಸಿ"]								    											    					
    								item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ದೋಷಯುಕ್ತ ಮೂಲ ವಾಕ್ಯ : "+sentence+"\nನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? :", ret_list[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,1)
    									if selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    										ignored_words.append(word)
    									if selected=="ಒಮ್ಮೆ ಕಡೆಗಣಿಸಿ" or selected=="ಸದಾ ಕಡೆಗಣಿಸಿ":
    										file_write+=sentence+"\n "
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    										continue
    									file_write+=selected+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								else:
		    								
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,3)
		    				# 1 coz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")

		    			
		    #everything in english for file stuff		
    	else:
    		if mode==1:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							for word in words:
    								intact_word=word
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								found_print=spell_check_eng(word)
    								if found_print[0]==1:
    									
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]=="" or found_print[2]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available for "+word+"\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=intact_word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[2])>0:
    										dialog=Dialog()
    										ignore=["Ignore Once","Ignore All"]
    										#dialog.move(400,500)
    										item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :",found_print[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="Ignore All":
    												ignored_words.append(word)
    											if selected=="Ignore Once" or selected=="Ignore All":
    												file_write+=intact_word+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												continue
    											
    											if after_pratyaya[0]==1:
    												pratyayas=after_pratyaya[4]
    												pr_len=len(pratyayas)
    												i=1
    												while i<=pr_len:
    													pr=pratyayas[-i]
    													print("word is",word)
    													print("pr is",pr)
    													if len(pr)==1:
    														final_pratyaya+=pr
    													else:
    														final_pratyaya+=pr[:-1]
    													i=i+1
    												final_pratyaya+=pr[-1]
    												print("final pr",final_pratyaya)
    												print("prinintin pratyays")
    												print(pratyayas)
    												file_write+=selected+final_pratyaya+" "
    												final_pratyaya=""
    												
    											else:
    												file_write+=selected+" "
    											self.textBrowser.setText(file_write)
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												QApplication.processEvents()
    												add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    			
    			
    		elif mode==2:
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					sent_num=0
    					
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								file_write+="\n"+word+" :\n"    								
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]    									
    									file_write+=after_pratyaya[2]
    								
    								if word in ignored_words:
    									file_write+=word+" "
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									continue
    								
    								if after_pratyaya[3]==1:
    									file_write+="The given word is present in the dictionary.The given word might not contain a sandhi!\n"
    									continue
    								found_print=sandhi_splitter_eng(word)
    								if found_print[0]==1:
    									file_write+=found_print[1]    										
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    								else:
    									if found_print[2]==0 or found_print[3]=="" or found_print[3]=='notthere':
    										dialog=Dialog()
    										
    									
    										text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available for "+word+"\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    										if ok and text != '':
    											print(text)
    											add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    											if add_success==1:
    												QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    										else:
    											file_write+=word+" "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    									if len(found_print[3])>0:
    										dialog=Dialog()
    										ignore=["Ignore Once","Ignore All"]
    										
    										item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :",found_print[3]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)										
    										if ok and item:
    											selected=pick_selected(item,1)
    											print(selected)
    											if selected=="Ignore All":
    												ignored_words.append(word)
    											if selected=="Ignore Once" or selected=="Ignore All":
    												file_write+=word+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												continue
    											
    											
    											file_write+="You have selected : "+selected+"\n "
    											found_print=sandhi_splitter_eng(selected)
    											file_write+=found_print[1]
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											
    										else:
    										#cancel is selected . no word is selected from suggestions
    											dialog=Dialog()
    											text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    											if ok and text != '':
    												print(text)
    												file_write+=text+" "
    												self.textBrowser.setText(file_write)
    												self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    												QApplication.processEvents()
    												add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    												if add_success==1:
    													QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    		elif mode==3:
    	#this is for englisg pratyaya chopper
    			sent_num=0
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						sent_num+=1
    						nums=str(sent_num)
    						file_write+="\n\n["+nums+"] "+sentence+"\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							words=sentence.split()
    							words=list(set(words))
    							for word in words:
    								intact_word=word
    								file_write+="\n"+word+" :\n"   
    								after_pratyaya=pratyaya_chopper(word,1)
    								if after_pratyaya[0]==1:
    									word=after_pratyaya[1]
    								if word in ignored_words:
    									file_write+=intact_word+" "
    									self.textBrowser.setText(file_write)
    									QApplication.processEvents()
    									continue
    								if after_pratyaya[3]==1:
    									file_write+="The root word is "+after_pratyaya[1]+"\n"
    									continue
    								else:
    									correct_selected=check_pratyaya(after_pratyaya[1],1)
    									print("cor",correct_selected[2])
    								
    									
    								if correct_selected[0]==1:    								
    									file_write+="\n"+after_pratyaya[2]+correct_selected[1]+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    									dialog=Dialog()
    									file_write+=after_pratyaya[2]+"No Suggestions are generated for "+word+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    									
    									text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available for "+word+"\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    									if ok and text != '':
    										print(text)
    										add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    										if add_success==1:
    											QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    	   				
    						
    								else:	
    									dialog=Dialog()
    									ignore=["Ignore Once","Ignore All"]							    											    					
    									item, ok = QInputDialog.getItem(dialog, "Suggestions","Mis-spelt root word : "+word+"\nDid you mean? :", correct_selected[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    									if ok and item:
    										print(item)
    										selected=pick_selected(item,1)
    										if selected=="Ignore All":
    											ignored_words.append(word)
    										if selected=="Ignore Once" or selected=="Ignore All":
    											file_write+="The root word is "+word+"\n "
    											self.textBrowser.setText(file_write)
    											self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    											QApplication.processEvents()
    											continue
    										after_pratyaya=pratyaya_chopper(selected,1)
    										if after_pratyaya[0]==1:
    											word=after_pratyaya[1]
    										file_write+=after_pratyaya[2]+"The correct root word is : "+after_pratyaya[1]+"\n"
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    									else:
		    								
		    								dialog=Dialog()
		    								text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    								if ok and text != '':
		    									print(text)
		    									add_success=add_word(text,1)
		    				# 1 coz stuffs in english
		    									if add_success==1:
		    										QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    		elif mode==4:
    	#this is for semantic stuff in eng
    			
    			for line in in_file:
    				if line!='\n':
    					sentences=line.split(".")
    					for sentence in sentences:
    						
    						file_write+="\n"
    						self.textBrowser.setText(file_write)
    						self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    						QApplication.processEvents()
    						file_write+="\n"
    						for num in remove_numbers:
    							if num in sentence:
    								sentence=sentence.replace(num,"")
    						for char in remove_chars:
    							if char in sentence:
    								sentence=sentence.replace(char,"")
    						if sentence!="":
    							if sentence in ignored_words:
    								file_write+=sentence+" "
    								self.textBrowser.setText(file_write)
    								QApplication.processEvents()
    								continue
    							ret_list=semantic(sentence,1)
    							if ret_list[0]==1:
    								sem_set=""
    								for sem_l in ret_list[1]:
    									sem_set+=sem_l+"\n"
    								file_write+=sem_set
    							
    								self.textBrowser.setText(file_write)
    								self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    								continue
    							
    							if ret_list[0]==0 and len(ret_list[2])==0: 
    								dialog=Dialog()
    								file_write+="No Suggestions are generated for "+sentence+"\n"
    								self.textBrowser.setText(file_write)
    								self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    								QApplication.processEvents()
    									
    								text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available for "+sentence+"\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    								if ok and text != '':
    									print(text)
    									add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    									if add_success==1:
    										QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    	   				    						
    							elif ret_list[0]==0:	
    								dialog=Dialog()
    								ignore=["Ignore Once","Ignore All"]							    											    					
    								item, ok = QInputDialog.getItem(dialog, "Suggestions","Incorrect sentence : "+sentence+"\nDid you mean? :", ret_list[2]+ignore, 0, False,QtCore.Qt.FramelessWindowHint)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,1)
    									if selected=="Ignore All":
    										ignored_words.append(word)
    									if selected=="Ignore Once" or selected=="Ignore All":
    										file_write+=sentence+"\n "
    										self.textBrowser.setText(file_write)
    										self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    										QApplication.processEvents()
    										continue
    									file_write+=selected+"\n"
    									self.textBrowser.setText(file_write)
    									self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
    									QApplication.processEvents()
    								else:
		    								
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,1)
		    				# 1 oz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")

		    			
		    					
    	#texteditor()
    	print("outside")
    	output_file=file_name[:-4]+"_out.txt"
    	out_file=open(output_file,"w")
    	out_file.write("%s\n" % file_write)
    	out_file.close()
    	dialog=Dialog()
    	#w=QWidget()
    	reply = QMessageBox.question(dialog, "Text Editor option","The file "+output_file+" is generated.\n Would you like to open it in an editor?" ,QMessageBox.Yes | QMessageBox.No)
    	
    	if reply == QMessageBox.Yes:
    		os.system("gedit "+output_file)
			
    def submit_clicked(self):
    	pb=0
    	add_success=0
    	after_chop_print=''
    	if given_input!="":

    		while pb<=100:
    			value = self.progressBar.value() + 1
    			self.progressBar.setProperty("value", value)
    			time.sleep(0.0000000001)
    			pb=value
    			#to update the GUI
    			QApplication.processEvents()
    			
    		#spell checker stuff	
    		if self.radioButton_3.isChecked():
    			
    			print("Spell checker selected")
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,1,3)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,3)
    		
    					if to_chop_returned[0]==1:
    							#self.textBrowser.setText(to_chop_returned[2])
    						correct_selected=spell_check_kan(to_uni(to_chop_returned[1]))
    						print("sent",to_chop_returned[1])
    						print("in elif returned to[2]",to_chop_returned[2])
    					else:   					  					
    					   	correct_selected=spell_check_kan(given_input)
    					print("cor",correct_selected[2])
    					if correct_selected[0]==1:
    						self.textBrowser.setText(to_chop_returned[2]+correct_selected[1]+"\nಸರಿಯಾದ ಪದ :"+given_input)
    				
    					elif correct_selected[2]=="" or correct_selected[2]=='notthere':
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText(to_chop_returned[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    						text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,3)
    							# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    					else:
    						dialog=Dialog()
    						print("correct_selected[2] is",correct_selected[2])
    						item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? ", correct_selected[2], 0, False)
    						if ok and item:
    							print(item)
    							#3 because kannada
    							selected=pick_selected(item,3)
    							print(selected)
    							selected=to_roman(selected)
    							if to_chop_returned[0]==1:
    								pratyayas=to_chop_returned[4]
    								pr_len=len(pratyayas)
    								i=1
    								final_pratyaya=""
    								while i<=pr_len:
    									pr=pratyayas[-i]
    									
    									print("pr is",pr)
    									if len(pr)==1:
    										final_pratyaya+=pr
    									else:
    										final_pratyaya+=pr[:-1]
    									i=i+1
    								final_pratyaya+=pr[-1]
    								selected+=final_pratyaya
    							selected=to_uni(selected)
    							print("sel",selected)
    							self.textBrowser.setText("ನೀವು ಆಯ್ದ ಸರಿಯಾದ ಪದ : "+selected)
    						else:
    						#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ  ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    					
       			
        			
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,1,1)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,0)
    					#need to improvise this and add changes to the kannada version as well
    					#this also seems to be fine!
    					if to_chop_returned[0]==1:
    						#self.textBrowser.setText(to_chop_returned[2])
    						correct_selected=spell_check_eng(to_chop_returned[1])
    						print("in elif returned to[2]",to_chop_returned[2])
    					else:   					  					
    					   	correct_selected=spell_check_eng(given_input)
    					if correct_selected[0]==1:
    						self.textBrowser.setText(to_chop_returned[2]+correct_selected[1])
    					
    					elif correct_selected[2]=="" or correct_selected[2]=='notthere':
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText(to_chop_returned[2]+"No Suggestions are generated!")
    						text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					else:
    						dialog=Dialog()
    						print("correct_selected[2] is",correct_selected[2])
    						item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", correct_selected[2], 0, False)
    						if ok and item:
    							print(item)
    							#3 because kannada
    							selected=pick_selected(item,1)
    							print(selected)
    							if to_chop_returned[0]==1:
    								pratyayas=to_chop_returned[4]
    								pr_len=len(pratyayas)
    								i=1
    								final_pratyaya=""
    								while i<=pr_len:
    									pr=pratyayas[-i]
    									
    									print("pr is",pr)
    									if len(pr)==1:
    										final_pratyaya+=pr
    									else:
    										final_pratyaya+=pr[:-1]
    									i=i+1
    								final_pratyaya+=pr[-1]
    								selected+=final_pratyaya
    								
    							self.textBrowser.setText("The correct word is "+selected)
    						else:
    						#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					
    				
    				
    		#whole sandhi splitter stuff	
    		if self.radioButton_2.isChecked():
    			print("Sandhi splitter selected")
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,2,3)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,3)
    					#need to improvise this and add changes to the kannada version as well
    					#I guess everything is proper now. need to make a kannada version
    					print("inside")
    					if to_chop_returned[3]==1:
    						self.textBrowser.setText(to_chop_returned[2]+to_uni(to_chop_returned[1])+" : ಈ ಪದವು ಪದಕೋಶದಲ್ಲಿ ಲಭ್ಯವಿದೆ.\nಈ ಪದವು ಸಂದಿಪದವಲ್ಲದಿರಬಹುದು!")
    					else:
    						if to_chop_returned[0]==1:
    							found_print=sandhi_splitter_kan(to_uni(to_chop_returned[1]))
    							self.textBrowser.setText(to_chop_returned[2]+found_print[1])
    							print("in elif returned to[2]",to_chop_returned[2])
    						else:  
    							print("in else")  					  					
    							found_print=sandhi_splitter_kan(given_input)
    							self.textBrowser.setText(found_print[1])
    							
    						#print("found prnt 3 is",found_print[3])
    						print("length of found_prin",len(found_print))
    						if len(found_print)>2:
    							if found_print[4]==1:
    								print("found_print[4] ",found_print[4])
    								print("found_print[5] ",found_print[5])
    								print("found_print[3] ",found_print[3])
    								self.textBrowser.setText(found_print[5])
    								
#	
#	
    							
    						if len(found_print)>2:
    							if found_print[2]==1 and not (found_print[3]=='notthere' or found_print[3]==""):
    								dialog=Dialog()
    								print("that erros thisg",found_print[3])
    								item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?", found_print[3], 0, False)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,3)
    									print(selected)
    									found_print=sandhi_splitter_kan(selected)
    									self.textBrowser.setText(found_print[1])
    								else:
		    							self.textBrowser.setText("")
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ? : ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,3)
		    							# 1 coz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")				    		
    				
    						elif (len(found_print)<3 and found_print[0]!=1): #or (found_print[3]=='notthere' or found_print[3]==""):
		    					dialog=Dialog()
    							self.textBrowser.setText(to_chop_returned[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    
    				
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,2,1)
    				else:
    					to_chop_returned=pratyaya_chopper(given_input,0)
    					#need to improvise this and add changes to the kannada version as well
    					#I guess everything is proper now. need to make a kannada version
    					print("inside")
    					if to_chop_returned[3]==1:
    						self.textBrowser.setText(to_chop_returned[2]+"\nThe word "+to_chop_returned[1]+" is present in the dictionary.\n It might not contain a sandhi!")
    					else:
    						if to_chop_returned[0]==1:
    							found_print=sandhi_splitter_eng(to_chop_returned[1])
    							self.textBrowser.setText(to_chop_returned[2]+found_print[1])
    							print("in elif returned to[2]",to_chop_returned[2])
    						else:    					  					
    							found_print=sandhi_splitter_eng(given_input)
    							self.textBrowser.setText(found_print[1])
    							print("in else")
    						#print("found prnt 3 is",found_print[3])
    						print("length of found_prin",len(found_print))
    						if len(found_print)>2:
    							if found_print[4]==1:
    								print("found_print[4] ",found_print[4])
    								print("found_print[5] ",found_print[5])
    								print("found_print[3] ",found_print[3])
    								self.textBrowser.setText(found_print[5])
    								
#	
#	
    							
    						if len(found_print)>2:
    							if found_print[2]==1 and not (found_print[3]=='notthere' or found_print[3]==""):
    								dialog=Dialog()
    								print("that erros thisg",found_print[3])
    								item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", found_print[3], 0, False)
    								if ok and item:
    									print(item)
    									selected=pick_selected(item,1)
    									print(selected)
    									found_print=sandhi_splitter_eng(selected)
    									self.textBrowser.setText(found_print[1])
    								else:
		    							self.textBrowser.setText("")
		    							dialog=Dialog()
		    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    							if ok and text != '':
		    								print(text)
		    								add_success=add_word(text,1)
		    							# 1 coz stuffs in english
		    								if add_success==1:
		    									QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")				    		
    				
    						elif (len(found_print)<3 and found_print[0]!=1): #or (found_print[3]=='notthere' or found_print[3]==""):
		    					dialog=Dialog()
    							self.textBrowser.setText(to_chop_returned[2]+"No Suggestions are generated!")
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    								# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    
		    #for pratyaya chopper	   			
    		if self.radioButton.isChecked():
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,3,3)
    				else:
    					print("Root word extractor kannada selected")
    					after_pratyaya=pratyaya_chopper(given_input,3)
    					if after_pratyaya[0]==1:
    						self.textBrowser.setText(after_pratyaya[2])
    					if after_pratyaya[3]==0:
    						correct_selected=check_pratyaya(after_pratyaya[1],3)
    						print("cor",correct_selected[2])
    						if correct_selected[0]==1:
    							self.textBrowser.setText(after_pratyaya[2]+correct_selected[1])
    						elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    							dialog=Dialog()
    							self.textBrowser.setText(after_pratyaya[2]+"ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!!")
    							text, ok = QInputDialog.getText(dialog,"ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ? ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    									# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    		   				
    							
    						else:	
    							dialog=Dialog()    					
    							item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ?:", correct_selected[2], 0, False)
    							if ok and item:
    								print(item)
    								selected=pick_selected(item,1)
    								print("after")
    								print(after_pratyaya[2])
    								after_pratyaya=pratyaya_chopper(selected,3)
    								if after_pratyaya[0]==1:
    									self.textBrowser.setText(after_pratyaya[2])
    								self.textBrowser.setText(after_pratyaya[2]+"\nಸರಿಯಾದ ಮೂಲ ಪದ : "+to_uni(after_pratyaya[1]))
    							
    							else:
		    						self.textBrowser.setText("")
		    						dialog=Dialog()
		    						text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ : ", QLineEdit.Normal,"")
		    						if ok and text != '':
		    							print(text)
		    							add_success=add_word(text,1)
		    					# 1 coz stuffs in english
		    							if add_success==1:
		    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
		    			
    			else:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,3,1)
    				else:
    					print("Root word extractor selected")
    					after_pratyaya=pratyaya_chopper(given_input,1)
    					if after_pratyaya[0]==1:
    						self.textBrowser.setText(after_pratyaya[2])
    					if after_pratyaya[3]==0:
    						correct_selected=check_pratyaya(after_pratyaya[1],1)
    						print("cor",correct_selected[2])
    						if correct_selected[0]==1:
    							self.textBrowser.setText(after_pratyaya[2]+correct_selected[1])
    						elif correct_selected[2]=='' or correct_selected[2]=='notthere': 
    							dialog=Dialog()
    							self.textBrowser.setText(after_pratyaya[2]+"No Suggestions are generated!")
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    									# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
		    		   				
    							
    						else:	
    							dialog=Dialog()    					
    							item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", correct_selected[2], 0, False)
    							if ok and item:
    								print(item)
    								selected=pick_selected(item,1)
    								after_pratyaya=pratyaya_chopper(selected,1)
    								if after_pratyaya[0]==1:
    									self.textBrowser.setText(after_pratyaya[2])
    								self.textBrowser.setText(after_pratyaya[2]+"\nThe correct root word is : "+after_pratyaya[1])
    							else:
		    						self.textBrowser.setText("")
		    						dialog=Dialog()
		    						text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
		    						if ok and text != '':
		    							print(text)
		    							add_success=add_word(text,1)
		    					# 1 coz stuffs in english
		    							if add_success==1:
		    								QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")



#semantic checker stuff	
    		if self.radioButton_4.isChecked():
    			if self.input_language_combo.currentIndex()==1:
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,4,3)
    				else:
    					ret_list=semantic(given_input,3)
    					if ret_list[0]==1:
    						sem_write=""
    						for sem_set in ret_list[1]:
    							sem_write+=sem_set+"\n" 
    						self.textBrowser.setText(sem_write)
    					
    					elif ret_list[0]==0 and len(ret_list[1])==0:
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText("ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ!")
    						text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಸಲಹೆಗಳು ಲಭ್ಯವಾಗಿಲ್ಲ.\nಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ?", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,3)
    								# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
    					elif ret_list[0]==0:
    						dialog=Dialog()
    						item, ok = QInputDialog.getItem(dialog, "ಸಲಹೆಗಳು","ನೀವು ಈ ಪದ ಬಯಸಿದಿರೇ? :", ret_list[2], 0, False)
    						if ok and item:
    							print(item)
    								#3 because kannada
    							selected=pick_selected(item,1)    							
    							self.textBrowser.setText("ನೀವು ಆಯ್ದ ಸರಿಯಾದ ವಾಕ್ಯ :  "+selected)
    						else:
    					#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "ನೂತನ ಪದ","ಬಯಸಿದ ಪದವಿರದೆ ಪದಕೋಶಕ್ಕೆ ನೂತನ ಪದ ಸೇರಿಸಲು ಬಯಸುವಿರೇ ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    								QMessageBox.information(dialog,"ಯಶಸ್ವಿ ಸೇರ್ಪಡೆ ", "ನೂತನ ಪದ ಸೇರ್ಪಡೆ ಸಫಲವಾಗಿದೆ")
 	
    			else:
    			#englisg stuff
    				if given_input.endswith(".txt"):
    					self.called_file(given_input,4,1)
    				else:
    					ret_list=semantic(given_input,1)
    					if ret_list[0]==1:
    						sem_write=""
    						for sem_set in ret_list[1]:
    							sem_write+=sem_set+"\n" 
    						self.textBrowser.setText(sem_write)
    				
    					elif ret_list[0]==0 and len(ret_list[1])==0:
    						#no suggestions are generated
    						dialog=Dialog()
    						self.textBrowser.setText("No Suggestions are generated!")
    						text, ok = QInputDialog.getText(dialog, "Adding a new word","No suggestions are available.\nDo you want to add this word to the dictionary : ", QLineEdit.Normal,"")
    						if ok and text != '':
    							print(text)
    							add_success=add_word(text,1)
    							# 1 coz stuffs in english adn 3 for kan
    						if add_success==1:
    							QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					elif ret_list[0]==0:
    						dialog=Dialog()
    						item, ok = QInputDialog.getItem(dialog, "Suggestions","Did you mean? :", ret_list[2], 0, False)
    						if ok and item:
    							print(item)
    							#3 because kannada
    							selected=pick_selected(item,1)
    							    							
    							self.textBrowser.setText("The correct sentence is "+selected)
    						else:
    						#cancel is selected . no word is selected from suggestions
    							dialog=Dialog()
    							text, ok = QInputDialog.getText(dialog, "Adding a new word","If the intended word is not in suggestions, \nPlease try adding a new word to the dictionary : ", QLineEdit.Normal,"")
    							if ok and text != '':
    								print(text)
    								add_success=add_word(text,1)
    									# 1 coz stuffs in english adn 3 for kan
    							if add_success==1:
    									QMessageBox.information(dialog,"Success", "The word is successfully added to the dictionary")
    					
    				
		    			
		    				
    			
    	else:
    		dialog=Dialog()
    		if self.input_language_combo.currentIndex()==1:
    			reply = QMessageBox.information(dialog,"ಸೂಚನೆ", "ದಯಮಾಡಿ ಪರಿಶೀಲಿಸ ಬಯಸುವ ಪದವನ್ನು ದಾಖಲಿಸಿ")
    		else:
    			reply = QMessageBox.information(dialog,"Information", "Please provide a valid input")
   
   
   	
             
class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.move(400,150)
    



