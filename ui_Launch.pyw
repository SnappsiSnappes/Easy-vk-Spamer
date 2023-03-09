import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_11 import Ui_MainWindow
import os
from Parcing_group import parcing_group
import time

import click

from Thread_with_cb import *
from BD import BD
from main_func import main_func


#ui0(QtWidgets.QMainWindow):



    
    
#удалить пустые строки
def remove_n(filename):
    f = open(f"{filename}","r+",encoding='utf-8')
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != "\n":
            f.write(i)
    f.truncate()
    f.close()  

#чек есть ли файл, если нет то создает пустой
def check_alive(filename):
    if os.path.exists(f'{filename}') == False:
        with open(f'{filename}',"a+",encoding='utf=8') as g: g.close()





class ui0(Ui_MainWindow,QtWidgets.QMainWindow):
    we_sub=False
    our_sub=False
    friend_msg=False
    non_friend_msg=False
    non_friend_add=False
    echo=False
    demo=False
    def __init__(self, parent = None,*args):
        super(ui0,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Easy-vk-Spamer-by-Snappesi')
        self.setWindowIcon(QIcon('snappes.ico'))


        self.init_UI()
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)

        check_alive('msg.txt');check_alive('users.txt');check_alive('old_pers.txt');check_alive('target.txt')
        check_alive('pic.txt')
        check_alive('pic_bd.txt');check_alive('msg_bd.txt')
        

        #чтение users
        with open("users.txt","r",encoding='utf-8') as file:
            for line in file:
                if line == '\n':
                    continue
                key1, key2, value1, key3, value2 = line.split()
                vk = f'{value1} + {value2}'
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget.addItem(item)
                item.setText(vk)
        #чтение msg
        with open('msg.txt','r',encoding='utf-8') as file:
            for line in file:
                if line =='\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_2.addItem(item)
                line = line.replace('{1}',' ')
                line = line.replace('{0}','_имя_')
                item.setText(line)
                #выводим юзеру более понятные данные а себе оставим технические
        with open("pic.txt","r",encoding='utf-8') as file:
            for line in file:
                if line == '\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_4.addItem(item)
                item.setText(line)
       
        with open("pic_bd.txt","r",encoding='utf-8') as file:
            for line in file:
                if line == '\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_6.addItem(item)
                item.setText(line)         

        with open('msg_bd.txt','r',encoding='utf-8') as file:
            for line in file:
                if line =='\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_5.addItem(item)
                line = line.replace('{1}',' ')
                line = line.replace('{0}','_имя_')
                item.setText(line)
                #выводим юзеру более понятные данные а себе оставим технические        

    def init_UI(self):
        self.ui.pushButton.clicked.connect(self.addUser)
        self.ui.pushButton_2.clicked.connect(self.removeUser)
        self.ui.pushButton_3.clicked.connect(self.addmsg)
        self.ui.pushButton_4.clicked.connect(self.removemsg)
        self.ui.pushButton_6.clicked.connect(self.group_parse)
        self.ui.pushButton_8.clicked.connect(self.friends_parse)
        self.ui.pushButton_5.clicked.connect(self.history)
        self.ui.pushButton_9.clicked.connect(self.addPicture)
        self.ui.pushButton_10.clicked.connect(self.removePicture)
        self.ui.pushButton_14.clicked.connect(self.addPictureBD)
        self.ui.pushButton_15.clicked.connect(self.removePictureBD)
        self.ui.pushButton_11.clicked.connect(self.addmsgBD)
        self.ui.pushButton_12.clicked.connect(self.removemsgBD)
        self.ui.pushButton_13.clicked.connect(self.BD)
        self.ui.pushButton_7.clicked.connect(self.main)
        self.ui.pushButton_16.clicked.connect(self.dono)


    def addmsg(self):
        #user_msg = ввел пользователь сообщение, далее убираем знак переноса строки
        #и заменяем его на спец символ с которым потом делаем формат , во время
        #отправки сообщений для работы, а в окно юзеру выводим обратно символ пробела
        user_msg, ok = QInputDialog.getMultiLineText(self,'Введите сообщение','Поле ввода')
        user_msg = user_msg.replace("\n","{1}")
        user_msg = user_msg.replace("_имя_","{0}")
        if user_msg and ok:
            with open('msg.txt', 'a+',encoding='utf-8') as g:
                g.write('\n' + user_msg)
        item = QtWidgets.QListWidgetItem()
        self.ui.listWidget_2.addItem(user_msg.replace('{1}',' '))
        item.setText(user_msg)
            
    def removemsg(self):
        remove_n('msg.txt')
        with open('msg.txt', 'r+',encoding='utf-8') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
        #чистим диалог и обновляем список
        self.ui.listWidget_2.clear()
        with open('msg.txt','r',encoding='utf-8') as file:
            for line in file:
                if line =='\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_2.addItem(item)
                line = line.replace('{1}',' ')
                line = line.replace('{0}','_имя_')
                item.setText(line)
        
    def addUser(self):
        #dd = скольок строчек в файле 
        dd = 1
        for line in open('users.txt','r'):
            if line == '\n':
                continue
            else:
                dd = dd+1
        #два раза диалог
        text, ok = QInputDialog.getText(self, "Введите логин", 
                                       "Логин:", QLineEdit.Normal,'')
        text2, ok2 = QInputDialog.getText(self, "Введите пароль", 
                                       "Пароль:", QLineEdit.Normal,'')
        if text2 and ok2 and text and ok:
            with open('users.txt','a+',encoding='utf-8') as g:
                g.write('\n'+str(dd)+' '+'password'+ ' ' + text2 + ' ' + 'login' + ' ' + text)
        #чистим диалог и обновляем список
        self.ui.listWidget.clear()
        with open("users.txt","r",encoding='utf-8') as file:
            for line in file:
                if line == '\n':
                    continue
                key1, key2, value1, key3, value2 = line.split()
                vk = f'{value1} + {value2}'
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget.addItem(item)
                item.setText(vk)
        
    def removeUser(self):
        remove_n('users.txt')
        #функция удаления последней строки
        with open('users.txt', 'r+',encoding='utf-8') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
        #чистим диалог и обновляем список
        self.ui.listWidget.clear()
        with open("users.txt","r",encoding='utf-8') as file:
            for line in file:
                if line == '\n':
                    continue
                key1, key2, value1, key3, value2 = line.split()
                vk = f'{value1} + {value2}'
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget.addItem(item)
                item.setText(vk)        

    def group_parse(self):


        text, ok = QInputDialog.getText(self, "Введите ссылку на группу", "Ссылка:", QLineEdit.Normal,'')

        if not 'https://' in text:
            text = 'https://'+text

        if self.ui.checkBox_3.isChecked() == True:
            global echo
            print('check is true')
            echo = True
        else:
            echo = False

        if text and ok:
            ui0.runLongTask(self,parcing_group,echo=echo,link=text)
            #item = QtWidgets.QListWidgetItem()
            #self.ui.listWidget_3.addItem(item)
            #item.setText("Ссылки успешно занесены в TARGET.TXT")
    

    def runLongTask(self,func,echo=bool,link=str):

            Worker.link = link

            # Step 2: Create a QThread object
            self.thread = QThread()
            # Step 3: Create a worker object
            self.worker = Worker()
            #передача функции func func func Моя функция

            self.worker.func = func
            if echo == True:
                Worker.echoVar=True
                 
            
            # Step 4: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.reportProgress)
            # Step 6: Start the thread
            self.thread.start(QThread.HighPriority)


            # Final resets
            s = {parcing_friends:self.ui.pushButton_8,parcing_group:self.ui.pushButton_6,
            BD:self.ui.pushButton_13,main_func:self.ui.pushButton_7}
            if func in s:
                s[func].setEnabled(False)
                self.thread.finished.connect(lambda: s[func].setEnabled(True))
                self.thread.finished.connect(lambda: self.ui.progressBar.setValue(500))    
                #self.ui.pushButton_8.setEnabled(False)
                #self.thread.finished.connect(
                #    lambda: self.ui.pushButton_8.setEnabled(True))
                #self.thread.finished.connect(
                #    lambda: self.ui.progressBar.setValue(500))
                
         

    def friends_parse(self):
        #thr_1 = threading.Thread(target=parcing_friends,name='t=1',daemon=True)
        #thr_1.start()
        

        if self.ui.checkBox_3.isChecked() == True:
            global echo
            print('check is true')
            echo = True
        else:
            echo = False

        ui0.runLongTask(self,parcing_friends,echo=echo)
        # рабочий
        #ui0.runLongTask(self,parcing_friends)

        
        item = QtWidgets.QListWidgetItem()
        self.ui.listWidget_3.addItem(item)
        item.setText("Процесс парсинга друзей запущен, ждите. Важно не нажимайте кнопки пока не закончится процесс")

    def reportProgress(self,n):
        self.ui.progressBar.setValue(n)
        #item_end = QtWidgets.QListWidgetItem()
        #self.ui.listWidget_3.addItem(item_end)
        #item_end.setText("Процесс завершен✅")

    def history(self):
        os.startfile('old_pers.txt')

    def addPicture(self):
        text, ok = QInputDialog.getText(self, "Введите ссылку на картинку", "ссылка:", QLineEdit.Normal,'')
        if text and ok:
            with open('pic.txt','a+',encoding='utf-8') as g:
                g.write('\n'+text)
        #обновuть
        #читаем
        with open("pic.txt","r",encoding='utf-8') as file:
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_4.addItem(item)
                item.setText(text)

    def removePicture(self):
        remove_n('pic.txt')
        #функция удаления последней строки
        with open('pic.txt', 'r+',encoding='utf-8') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
        #чистим диалог и обновляем список
        self.ui.listWidget_4.clear()
        with open("pic.txt","r",encoding='utf-8') as file:
            for line in file:
                
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_4.addItem(item)
                item.setText(line)

    def addPictureBD(self):
        text, ok = QInputDialog.getText(self, "Введите ссылку на картинку", "ссылка:", QLineEdit.Normal,'')
        if text and ok:
            with open('pic_bd.txt','a+',encoding='utf-8') as g:
                g.write('\n'+text)
        #обновuть
        #читаем
        with open("pic_bd.txt","r",encoding='utf-8') as file:
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_6.addItem(item)
                item.setText(text)

    def removePictureBD(self):
        remove_n('pic_bd.txt')
        #функция удаления последней строки
        with open('pic_bd.txt', 'r+',encoding='utf-8') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
        #чистим диалог и обновляем список
        self.ui.listWidget_6.clear()
        with open("pic_bd.txt","r",encoding='utf-8') as file:
            for line in file:
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_6.addItem(item)
                item.setText(line)

    def addmsgBD(self):
        #user_msg = ввел пользователь сообщение, далее убираем знак переноса строки
        #и заменяем его на спец символ с которым потом делаем формат , во время
        #отправки сообщений для работы, а в окно юзеру выводим обратно символ пробела
        user_msg, ok = QInputDialog.getMultiLineText(self,'Введите сообщение','Поле ввода')
        user_msg = user_msg.replace("\n","{1}")
        user_msg = user_msg.replace("_имя_","{0}")
        if user_msg and ok:
            with open('msg_bd.txt', 'a+',encoding='utf-8') as g:
                g.write('\n' + user_msg)
        item = QtWidgets.QListWidgetItem()
        self.ui.listWidget_5.addItem(user_msg.replace('{1}',' '))
        item.setText(user_msg)
            
    def removemsgBD(self):
        remove_n('msg_bd.txt')
        with open('msg_bd.txt', 'r+',encoding='utf-8') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
        #чистим диалог и обновляем список
        self.ui.listWidget_5.clear()
        with open('msg_bd.txt','r',encoding='utf-8') as file:
            for line in file:
                if line =='\n':
                    continue
                item = QtWidgets.QListWidgetItem()
                self.ui.listWidget_5.addItem(item)
                line = line.replace('{1}',' ')
                line = line.replace('{0}','_имя_')
                item.setText(line)       
    
    def BD(self):
        if self.ui.checkBox_3.isChecked() == True:
            global echo
            echo = True
        else:
            echo = False
            
        if self.ui.checkBox_7.isChecked() == True:
            ui0.demo = True
        else:
            ui0.demo = False
        
        ui0.runLongTask(self,BD,echo=echo,link=None)

    def main(self):
        if self.ui.checkBox_3.isChecked() == True:
            ui0.echo = True
        else:
            ui0.echo = False
        if self.ui.checkBox_6.isChecked() == True:
            ui0.we_sub = True
        else:
            ui0.we_sub = False
        if self.ui.checkBox_5.isChecked() == True:
            ui0.our_sub = True
        else:
            ui0.our_sub = False
        if self.ui.checkBox_4.isChecked() == True:
            ui0.friend_msg = True
        else:
            ui0.friend_msg = False
        if self.ui.checkBox.isChecked() == True:
            ui0.non_friend_msg = True
        else:
            ui0.non_friend_msg = False
        if self.ui.checkBox_2.isChecked() == True:
            ui0.non_friend_add = True
        else:
            ui0.non_friend_add = False

        if self.ui.checkBox_7.isChecked() == True:
            ui0.demo = True
        else:
            ui0.demo = False

        print(ui0.echo)
        ui0.runLongTask(self,main_func)
        pass

    def dono(self):
        click.launch('https://www.donationalerts.com/r/snappes_tv')


#class
class Worker(QObject):
    echoVar = False
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    link = str
    
    @QtCore.pyqtSlot(int)
    def update_progress(self, n):
        self.progress.emit(n)

    def func(func,echo=bool,link=str):
        link=str
        func
        echo=ui0.echoVar
        
    def run(self):
        echo = self.echoVar
        link = self.link
        print(link)
        print(self.echoVar)
        if self.func == main_func:
            self.func(echo=ui0.echo,we_sub=ui0.we_sub,our_sub=ui0.our_sub,friend_msg=ui0.friend_msg,
            non_friend_msg=ui0.non_friend_msg,non_friend_add=ui0.non_friend_add,demo=ui0.demo)
        else:
            self.func(echo=echo,link=link,demo=ui0.demo,worker=self)
    

        self.finished.emit()

#https://vk.com/sunstudiosolo

from Parcing_friends import parcing_friends

app = QtWidgets.QApplication(sys.argv)
application = ui0()
application.show()
#app.exec_()
sys.exit(app.exec())

#window = Window()
#form = Form()
#form.setupUi(window)
#window.show()
#app.exec_()
