# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mask.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import threading

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QFileDialog

from train_data import predict
from video_rcnn import detect_video


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1103, 841)
        self.picture = None
        self.vido_path = None
        self.choose=None
        self.current_file_dictory = r'C:\Users\hedeqing\Desktop\SchoolWork\mask_rcnn\images'
        self.current_result_dictory = r'C:\Users\hedeqing\Desktop\SchoolWork\mask_rcnn\result'
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(430, 10, 121, 21))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(20, 50, 401, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 590, 93, 28))
        self.pushButton.setObjectName("pushButton")
        # 绑定点击事件
        self.pushButton.clicked.connect(self.on_click)

        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(490, 50, 591, 461))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(760, 610, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 590, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.detect_btn)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 750, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.loadFile)

        # self.label_3 = QtWidgets.QLabel(Form)
        # self.label_3.setGeometry(QtCore.QRect(430, 720, 72, 15))
        # self.label_3.setText("")
        # self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 680, 421, 41))
        self.textEdit.setObjectName("textEdit")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(740, 750, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.endRun)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图片检测与切割"))
        self.pushButton.setText(_translate("Form", "选择图片"))
        self.label_2.setText(_translate("Form", "生成结果"))
        self.pushButton_2.setText(_translate("Form", "检测"))
        self.pushButton_3.setText(_translate("Form", "选择视频"))
        self.pushButton_4.setText(_translate("Form", "终止运行"))


    def endRun(self):
        quit()
    def loadFile(self):
        try:
            fileName1, filetype = QFileDialog.getOpenFileName(None, "选取文件", "./",
                                                              "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
            print(fileName1)
            self.choose = 2
            self.vido_path = fileName1
            self.textEdit.setText(fileName1)
        except  Exception as e:
            print("error")
            print(e.__traceback__.tb_lineno)

    def on_click(self):
        try:
            fileName1, filetype = QFileDialog.getOpenFileName(None, "选取文件", "./",
                                                              "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
            self.picture = fileName1
            self.choose = 1
            # print(fileName1, filetype)
            # print(os.path.join(self.current_file_dictory, "Asian Elephant_64.jpg"))
            # img = cv2.imread(os.path.join(self.current_file_dictory, "Asian Elephant_64.jpg"))
            img = cv2.imread(fileName1)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            x = img.shape[1]  # 获取图像大小
            y = img.shape[0]
            frame = QImage(img, x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame).scaled(int(self.graphicsView.width() * 0.9),
                                                      int(self.graphicsView.height() * 0.9))
            item = QGraphicsPixmapItem(pix)  # 创建像素图元
            scene = QGraphicsScene()  # 创建场景
            scene.addItem(item)
            self.graphicsView.setScene(scene)
        except  Exception as e:
            print("error")
            print(e.__traceback__.tb_lineno)
    def detect_btn(self):
        if self.choose ==1:
            t_sing = threading.Thread(target=predict(self.picture), args=(5,))
            t_sing.start()
        else:
            t_sing = threading.Thread(target=detect_video(self.vido_path), args=(5,))
            t_sing2 = threading.Thread(target=detect_video(self.vido_path), args=(5,))
            t_sing3 = threading.Thread(target=detect_video(self.vido_path), args=(5,))
            t_sing.start()
            t_sing2.start()
            t_sing3.start()

        self.draw_result()

    def draw_result(self):
        img2 = cv2.imread(os.path.join(self.current_result_dictory, "result.png"))
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        x2 = img2.shape[1]  # 获取图像大小
        y2 = img2.shape[0]
        frame2 = QImage(img2, x2, y2, QImage.Format_RGB888)
        pix2 = QPixmap.fromImage(frame2).scaled(int(self.graphicsView_2.width() * 2.0),
                                                int(self.graphicsView_2.height() * 2.0))
        item2 = QGraphicsPixmapItem(pix2)  # 创建像素图元
        scene2 = QGraphicsScene()  # 创建场景
        scene2.addItem(item2)
        self.graphicsView_2.setScene(scene2)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    w = Ui_Form()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())
