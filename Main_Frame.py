import sys
import time

import pandas as pd

from AudioPlayerSpeech import AudioPlayerSpeech
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()

        self.read_news_dataset()
        self.current_index = -1
        self.is_change_type = False
        self.current_person = 'banmai'
        self.audio_layer = AudioPlayerSpeech()
        self.list_person = {"banmai": "Ban Mai: Nữ miền Bắc",
                            "linhsan": "Linh San: Nữ miền Nam",
                            "minhquang": "Minh Quang: Nam miền Nam"}

        self.url_api = 'https://api.fpt.ai/hmi/tts/v5'


        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(self.Dialog)

        self.add_item_combobox_type()
        self.add_item_combobox_person()
        self.add_item_news()
        
        self.Dialog.show()

        sys.exit(app.exec_())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(931, 836)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 931, 841))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layout_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_main.setContentsMargins(10, 0, 10, 0)
        self.layout_main.setSpacing(10)
        self.layout_main.setObjectName("layout_main")
        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_top.setContentsMargins(-1, -1, 15, -1)
        self.layout_top.setObjectName("layout_top")
        self.layout_logo = QtWidgets.QVBoxLayout()
        self.layout_logo.setContentsMargins(12, 10, -1, 10)
        self.layout_logo.setSpacing(10)
        self.layout_logo.setObjectName("layout_logo")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("image/news-logo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.layout_logo.addWidget(self.label)
        self.layout_top.addLayout(self.layout_logo)
        self.layout_name_project = QtWidgets.QVBoxLayout()
        self.layout_name_project.setObjectName("layout_name_project")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setMaximumSize(QtCore.QSize(934, 144))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.layout_name_project.addWidget(self.label_2)
        self.layout_top.addLayout(self.layout_name_project)
        self.layout_languague = QtWidgets.QVBoxLayout()
        self.layout_languague.setContentsMargins(-1, -1, -1, 18)
        self.layout_languague.setSpacing(0)
        self.layout_languague.setObjectName("layout_languague")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.layout_languague.addWidget(self.label_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(23, 0, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image/vietnam.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.layout_languague.addLayout(self.verticalLayout_8)
        self.layout_top.addLayout(self.layout_languague)
        self.layout_top.setStretch(0, 2)
        self.layout_top.setStretch(1, 12)
        self.layout_top.setStretch(2, 2)
        self.layout_main.addLayout(self.layout_top)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layout_main.addWidget(self.line)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 18, -1)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_show_type = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_show_type.setFont(font)
        self.label_show_type.setObjectName("label_show_type")
        self.horizontalLayout_3.addWidget(self.label_show_type)
        self.label_show_news = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_show_news.setFont(font)
        self.label_show_news.setObjectName("label_show_news")
        self.horizontalLayout_3.addWidget(self.label_show_news)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.label_show_name = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_show_name.setFont(font)
        self.label_show_name.setObjectName("label_show_name")
        self.verticalLayout_6.addWidget(self.label_show_name)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.button_show_mic = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_show_mic.setMinimumSize(QtCore.QSize(50, 50))
        self.button_show_mic.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/mute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_show_mic.setIcon(icon)
        self.button_show_mic.setIconSize(QtCore.QSize(40, 40))
        self.button_show_mic.setObjectName("button_show_mic")
        self.horizontalLayout_7.addWidget(self.button_show_mic)
        self.button_show_download = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_show_download.setMinimumSize(QtCore.QSize(50, 50))
        self.button_show_download.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_show_download.setIcon(icon1)
        self.button_show_download.setIconSize(QtCore.QSize(40, 40))
        self.button_show_download.setObjectName("button_show_download")
        self.horizontalLayout_7.addWidget(self.button_show_download)
        self.horizontalLayout_7.setStretch(0, 18)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.layout_main.addLayout(self.horizontalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layout_main.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_type = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_type.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")
        self.horizontalLayout_2.addWidget(self.comboBox_type)

        self.comboBox_person = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_person.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.comboBox_person.setFont(font)
        self.comboBox_person.setObjectName("comboBox_person")
        self.horizontalLayout_2.addWidget(self.comboBox_person)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 4)
        self.layout_main.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.listWidget.setSpacing(6)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.layout_main.addWidget(self.listWidget)
        self.layout_main.setStretch(2, 3)
        self.layout_main.setStretch(4, 2)
        self.layout_main.setStretch(5, 18)

        Dialog.setWindowTitle(self._translate("Dialog", "Tin tức Việt Nam"))
        self.label_2.setText(self._translate("Dialog", "ỨNG DỤNG ĐỌC TIN TỨC VIỆT NAM"))
        self.label_3.setText(self._translate("Dialog", "Ngôn Ngữ"))
        self.label_show_type.setText(self._translate("Dialog", "Thể loại"))
        self.label_show_news.setText(self._translate("Dialog", "Nguồn tin"))
        self.label_show_name.setText(self._translate("Dialog", "Tiêu đề tin tức"))
        self.label_5.setText(self._translate("Dialog", "Tùy chỉnh"))

        self.comboBox_type.activated.connect(self.action_combobox_type)
        self.comboBox_person.activated.connect(self.action_comboBox_person)
        self.button_show_mic.clicked.connect(self.action_button_show_mic)
        self.button_show_download.clicked.connect(self.action_button_show_download)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def read_news_dataset(self):
        df = pd.read_csv("./dataset/news_dataset.csv")
        self.list_topic = df["topic"]
        self.list_content = df["content"]
        self.list_title = df["title"]
        self.list_source = df["source"]

    def add_item_combobox_type(self):
        topics = list(dict.fromkeys(self.list_topic))
        for t in topics:
            self.comboBox_type.addItem(str(t))

    def add_item_combobox_person(self):
        for t in self.list_person.values():
            self.comboBox_person.addItem(str(t))

    def add_item_news(self):
        self.listWidget.clear()
        if self.is_change_type:
            self.listWidget.itemClicked.disconnect(self.click_item_list_news)

        self.list_index = []
        type_select = self.comboBox_type.currentText()
        for i, type in enumerate(self.list_topic):
            if type == type_select:
                self.list_index.append(i)
                item = QtWidgets.QListWidgetItem()
                self.listWidget.addItem(item)
                item = self.listWidget.item(len(self.list_index)-1)
                item.setText(self._translate("Dialog", str(self.list_title[i])))

        self.listWidget.itemClicked.connect(self.click_item_list_news)
        self.is_change_type = True

    def action_combobox_type(self):
        self.add_item_news()

    def action_comboBox_person(self):
        for key, value in self.list_person.items():
            if value == self.comboBox_person.currentText():
                self.current_person = key
                break

    def action_button_show_mic(self):
        self.play_pause_toggle()

    def action_button_show_download(self):
        if self.current_index != -1:
            self.audio_layer.download()
            self.message_warning("Download successfully")
        else:
            self.message_warning()

    def click_item_list_news(self, x):
        try:
            row = self.listWidget.row(x)
            index = self.list_index[row]

            self.label_show_name.setText(self._translate("Dialog", str(self.list_title[index])))
            self.label_show_type.setText(self._translate("Dialog", str(self.list_topic[index])))
            self.label_show_news.setText(self._translate("Dialog", str(self.list_source[index])))

            self.current_index = index
            time.sleep(0.5)
            self.change_icon_mic("image/mic.png")

            self.audio_layer.init(index, self.current_person, self.list_title[index])
        except:
            self.message_warning("Lỗi !! Vui lòng thử lại")

    def play_pause_toggle(self):
        if self.current_index != -1:
            if not self.audio_layer.is_paused:
                self.audio_layer.pause()
                self.change_icon_mic("image/mute.png")

            else:
                self.audio_layer.unpause()
                self.change_icon_mic("image/mic.png")
        else:
            self.message_warning()

    def change_icon_mic(self, path):
        if self.current_index != -1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.button_show_mic.setIcon(icon)
            self.button_show_mic.setIconSize(QtCore.QSize(40, 40))
        else:
            self.message_warning()

    def message_warning(self, text="Vui lòng chọn tin tức cần đọc !!"):
        dialog = QtWidgets.QMessageBox(self.Dialog)
        dialog.setText(text)
        dialog.setWindowTitle("Cảnh báo")
        dialog.exec_()

if __name__ == "__main__":
    ui = Ui_Dialog()
