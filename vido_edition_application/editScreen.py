from arayuz2 import Ui_Form
from PySide6.QtWidgets import QWidget,QVBoxLayout,QStyle,QFileDialog
from PySide6.QtCore import Qt,QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
import cv2
from moviepy.editor import *
import datetime
from PySide6.QtWidgets import *
import os 
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
from pathlib import Path
from PySide6.QtMultimedia import QMediaMetaData

#thread 
 
import numpy as np 
from os import listdir
from PySide6.QtCore import QObject, QThread, Signal




class MediaPlayerApp(QMainWindow, Ui_Form):
    #this is for video playing 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollWidget = QWidget()
        self.scrollWidgetLayout = QHBoxLayout(self.scrollWidget)
        self.scrollArea = QScrollArea()

        self.create_framesFolder()
        self.video_name=""
        self.filename=""
        self.mediaPlayer = QMediaPlayer()
        self.videowidget = QVideoWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.videowidget)
        self.verticalLayout.addLayout(layout) 
        self.temp_hold_time=0.0
        self.time = 0.0
        self.flag= True
        self.create_player()
        
        


    #this is for croping from video directly 

        self.hold_path=""
        self.list = []
        self.list.append(0)
        self.list.append(0)
        
        self.cropfile = ""
        self.path = rf'C:\Users\HP\Downloads\bitirme projesi\data'
        self.scroller_sconds =[]
        self.scroller_sconds.append(0)
        
    #this is for creating slider 
        self.ctr=0
        self.get_label_number=0
        self.Labels=[]

        self.filename=""
        self.slider_val=[]
        self.slider_val.append(0)
 
        self.capture = None
        self.dragging_line = False
        self.dragging_slider=False
        self.line_sec=[]
        self.current_time_seconds=0
        self.label_time=0
        self.progressBar.setMinimum(0)
        
        
       
        
    def callback(self):
        self.setVisible(False)
        self.sayfa.setVisible(True)

    def create_framesFolder(self):
                    # r'C:\Users\User\Desktop\bitirme projesi\frames'
        folder_name = r'C:\Users\HP\Downloads\bitirme projesi\frames'
        path = Path(folder_name)
        if path.exists() : 
            self.delete_folders()
            self.create_framesFolder()
        elif not path.exists() :
            os.makedirs(folder_name)
        
    def closeEvent(self, event):
        self.delete_folders()
        event.accept()
        
    def create_player(self):
        #the video playing part 
        self.pushButton_videosec.clicked.connect(self.open_file)
        self.pushButton_play.clicked.connect(self.play_video)
        self.pushButton_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.mediaPlayer.setVideoOutput(self.videowidget)
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        
        #her hangi bir sey degismedi 

        self.mediaPlayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        
        #cropping from video directly 
        self.pushButton_select.clicked.connect(self.select_folder)
        self.pushButton_basframe.clicked.connect(self.cropstartt)
        self.pushButton_bitisframe.clicked.connect(self.cropendd)
    
        self.pushButton_kaydet.mousePressEvent=self.kaydet_changeColor
        self.horizontalSlider.valueChanged.connect(self.init_line_dragging)
        
        #slider things 
        self.progressBar.setVisible(False)
        self.loading.setVisible(False)
        self.horizontalSlider.setMouseTracking(True)
        self.init_slider_dragging()

#to play video 
    def open_file(self):
        
        try:
            self.filename, _ = QFileDialog.getOpenFileName(self, "Video Seç", "", "Video files (*.mp4 *.avi)")
            if self.filename != '':
                if len(self.Labels)>0:
                    self.flag=True
                    self.resetGroupBox_components()
                self.capture = cv2.VideoCapture(self.filename)  
                self.cropfile = self.filename
                #print("cropfile :", self.filename)
                fps = self.capture.get(cv2.CAP_PROP_FPS)
                
                self.mediaPlayer.setSource(QUrl.fromLocalFile(self.filename))
                #self.mediaPlayer.setMediaContent(QUrl.fromLocalFile(self.filename))

                self.video_name = os.path.splitext(os.path.basename(self.filename))[0]
                #print(f"opened video -> {self.video_name}")
                self.create_labels()
                self.create_lines()

        
                 
        except Exception as e:
            print("Error occurred:", e)

    def play_video(self):
        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.pause()
            self.pushButton_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.pushButton_play.setText("Pause")

        else:
            self.pushButton_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.pushButton_play.setText("Play")
            self.mediaPlayer.play()


    def set_position(self, position):
        #print("form set position slider position",self.horizontalSlider.sliderPosition())
        self.mediaPlayer.setPosition(position)
        self.time = float(position / 1000)+0.000000000000000000000000001

    def duration_changed(self, duration):
        self.duration= duration
        self.horizontalSlider.setRange(0, duration)
        self.time = float(duration / 1000)+0.000000000000000000000000001 #1 
        if self.flag:
            self.temp_hold_time = self.time
            print(self.temp_hold_time)
            self.flag=False


    def position_changed(self, position):
        self.horizontalSlider.setValue(position)
        if self.mediaPlayer.isPlaying():
            self.set_scrollerArea_value()

    def set_scrollerArea_value(self):
        hold = self.line_to_label()
        self.line_sec[1].setText(f"{round(hold,3)}")
        slide_max = self.horizontalSlider.maximum()
        scroller_max=self.scrollArea.horizontalScrollBar().maximum()
        value=(scroller_max/slide_max)*self.horizontalSlider.value() 
        self.scrollArea.horizontalScrollBar().setValue(value)

    def init_slider_dragging(self):
        self.dragging_slider = False
        self.horizontalSlider.setMouseTracking(True)
        self.horizontalSlider.mousePressEvent = self.slider_mousePressEvent
        self.horizontalSlider.mouseMoveEvent = self.slider_mouseMoveEvent
        self.horizontalSlider.mouseReleaseEvent = self.slider_mouseReleaseEvent

    def slider_mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging_slider = True
            QSlider.mousePressEvent(self.horizontalSlider, event)

    def slider_mouseMoveEvent(self, event):
        if self.dragging_slider:
            self.set_scrollerArea_value()
            # Ensure the event is passed to the base class for default behavior
            QSlider.mouseMoveEvent(self.horizontalSlider, event)

    def slider_mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging_slider = False
            # Ensure the event is passed to the base class for default behavior
            QSlider.mouseReleaseEvent(self.horizontalSlider, event)

    def keyPressEvent(self, event):
        hold = self.line_to_label()
        self.line_sec[1].setText(f"{round(hold,3)}")
        slide_max = self.horizontalSlider.maximum()
        now_value= self.scrollArea.horizontalScrollBar().value()
        scroller_max=self.scrollArea.horizontalScrollBar().maximum()
        value=(scroller_max/slide_max)*self.horizontalSlider.value()
        change_amount = abs(now_value - value) 

        if event.key() == Qt.Key_Right or event.key()==Qt.Key_Left:
            self.set_scrollerArea_value()




    def set_slider_position(self):
        slide_max = self.horizontalSlider.maximum()
        scroller_max=self.scrollArea.horizontalScrollBar().maximum()

        value = (slide_max/scroller_max )*self.scrollArea.horizontalScrollBar().value()

        if not self.mediaPlayer.isPlaying():
            #print("checkpoint1")
            self.horizontalSlider.setValue(value)
            self.mediaPlayer.setPosition(self.horizontalSlider.sliderPosition())
            #print(f"{self.mediaPlayer.position()}, h {self.horizontalSlider.sliderPosition()}")
            hold = self.line_to_label()
            self.line_sec[1].setText(f"{round(hold,3)}")   
            
    def mediastate_changed(self, state):
        self.pushButton_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            
#to crop directly 

    def select_folder(self):
        try:
            self.path_label.setText("")  # Clear previous path
            folder_path, _ = QFileDialog.getSaveFileName(self, "Select Video", "", "Videos (*.mp4)")
            if folder_path:
                self.path_label.setText(folder_path)
                self.writetoFile()
        except Exception as e:
            print(f"Error in select_folder: {e}")

    def createFile(self, dosyayolu):
        try:
            os.makedirs(dosyayolu)
            #print("dosya yolu -> ",dosyayolu)
        except FileExistsError as error:
            print(error, "Dosya zaten mevcut")

    def cropstartt(self):
        self.path_label.setText("")
        current_time= self.mediaPlayer.position()/ 1000
        #print("time : ",current_time)
        start_time = current_time
        self.ilkframe_lbl.setText(f"Başlangıç Frame:{round(start_time,2)}")
        self.list[0]=start_time

    def cropendd(self):
        current_time= self.mediaPlayer.position()/ 1000
        #print("time : ",current_time)
        end_time = current_time
        self.sonframe_lbl.setText(f"Bitiş Frame:{round(end_time,2)}")
        self.list[1]=end_time

    def control_secs(self):
        temp = 0
        if self.list[0] > self.list[1]:
            temp = self.list[1]
            self.list[1] = self.list[0]
            self.list[0] = temp
            

    def reset_Framesec_Labels(self):
        self.ilkframe_lbl.setText("Başlangıç Frame")
        self.sonframe_lbl.setText("Bitiş Frame")
    
    def kaydet_reventColor(self):
        self.pushButton_kaydet.setStyleSheet(
                                            "#pushButton_kaydet{\n"
                                            "background-color: rgb(226, 0, 0);\n"
                                            "border-radius:20px;\n"
                                            "color:rgb(255, 255, 255)\n"
                                            "}")
        
        
    def kaydet_changeColor(self,event):
        self.pushButton_kaydet.setStyleSheet(
                                            "#pushButton_kaydet{\n"
                                            "background-color: #538d22;\n"  # Set the background color to the specified green tone
                                            "border-radius: 20px;\n"
                                            "color: rgb(255, 255, 255);\n" 
    "}")
        
        self.writetoFile()
            
    def writetoFile(self):
        #print("checkpoint12")
        self.reset_Framesec_Labels()
        cap = cv2.VideoCapture(self.cropfile)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        #print("frame per sec from ->",fps)
        #print("checkpoint24")
        fps2 = int(cap.get(cv2.CAP_PROP_FPS))
        self.control_secs()
        
        self.list[0]= round(self.list[0],2)
        self.list[1]= round(self.list[1],2)        
        #print(self.list[0])
        #print(self.list[1])
        start_time = self.list[0]
        start_frame = int(start_time * fps)
        end_time = self.list[1]
        end_frame = int(end_time * fps2)
        #print("start frame , endframe",start_frame, end_frame)
        width2 = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height2 = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter.fourcc(*"mp4v")
        file = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{file}.mp4"
        yeniyol = rf'C:\Users\HP\Downloads\bitirme projesi\data\{file}'
        if len(self.path_label.text())>0 :
            #print("path lab ", self.path_label.text())
            
            #file_path = rf"{self.path_label.text()}\{filename}"
            #self.path_label.setText(file_path)
            out = cv2.VideoWriter(self.path_label.text(),fourcc,fps,(width2,height2))
            #print("filename : ",self.path_label.text())
            
        else :
            defualt_path=rf'C:\Users\HP\Downloads\bitirme projesi\data\{file}\{filename}'
            self.path_label.setText(defualt_path)
            self.createFile(yeniyol)
            out = cv2.VideoWriter(defualt_path,fourcc,fps,(width2,height2))
            #print("filename : ",defualt_path)
        #print("start frame and end frame ",start_frame,end_frame)
        self.write_from_thread (frame_count,cap,start_frame, end_frame,out)
        
        
        self.line_sec[0].setStyleSheet("background-color: gray;")
        self.line_sec[1].setText(str(end_time))
    
    def write_from_thread (self, frame_count,cap,start_frame, end_frame,out):
        self.worker1= WorkerThread(cap,start_frame,end_frame,out,frame_count,1,None,None,None,self)
        self.worker1.start()

# to create slider 
    def create_labels(self,situation = False) -> int:

        path=rf"frames\{self.video_name}"

        if os.path.isdir(path) :
            self.loading.setVisible(False)
            self.progressBar.setVisible(False)
            self.progressBar.destroy()  

            fps = self.capture.get(cv2.CAP_PROP_FPS)
            self.progressBar.setMaximum(self.time*fps)

            self.scrollWidget = QWidget()
            self.scrollWidgetLayout = QHBoxLayout(self.scrollWidget)
            self.scrollArea = QScrollArea() 

            self.get_label_number=0
            filenames = os.listdir(path)
            sorted_filenames = sorted(filenames, reverse=False)
            for filename in sorted_filenames:
                image_path =fr"{path}\{filename}"
                label = QLabel()
                pixmap = QPixmap(image_path)
                label.setPixmap(pixmap)
                self.scrollWidgetLayout.addWidget(label)
                self.scrollWidgetLayout.setSpacing(0)
                self.scrollWidget.setFixedSize((self.get_label_number+1)*200,120)
                label.setVisible(True)
                self.Labels.append(label)
                self.get_label_number += 1
            self.pushButton_play.setEnabled(True)
            
            
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setWidget(self.scrollWidget)
            self.scroll_layout.addWidget(self.scrollArea)
            self.scroll_layout.addSpacing(0)
 
            self.scrollArea.verticalScrollBar().setVisible(False)
            self.scrollArea.horizontalScrollBar().setVisible(False)
            
            self.scrollArea.horizontalScrollBar().valueChanged.connect(self.set_slider_position)
        
        else: 
            from PySide6.QtCore import QRect
            self.progressBar.destroy()  
            self.progressBar = QProgressBar(self)
            self.progressBar.setObjectName(u"progressBar")
            self.progressBar.setGeometry(QRect(100, 650, 211, 10))
            self.progressBar.setStyleSheet(u"")
            self.progressBar.setValue(0)

            self.get_label_number=0
            os.makedirs(path)
            self.pushButton_play.setEnabled(False)
            self.loading.setVisible(True)
            self.progressBar.setVisible(True)
            self.loading.setText("yüleniyor.....")
            #print("checkpoint1")
            self.extracte_frames(path)
        
    def extracte_frames(self, path):
        self.worker3= WorkerThread(None,None,None,None,None,3,self.capture,path,self.get_label_number,self)
        self.worker3.start()
        self.worker3.result_signal.connect(self.create_labels)

    def create_lines(self):
        
        self.line_sec.clear()
        line1 = QtWidgets.QFrame(self.groupBox)
        line1.setGeometry(QtCore.QRect(0, 10, 7, 130))
        line1.setSizeIncrement(QtCore.QSize(0, 0))
        font1 = QtGui.QFont()
        font1.setBold(False)
        font1.setWeight(QtGui.QFont.Bold)
 
        line1.setFrameShadow(QtWidgets.QFrame.Raised)
        line1.setLineWidth(3)
        line1.setFrameShape(QtWidgets.QFrame.VLine)
        line1.setObjectName("line1")
        line1.setVisible(True)

        self.line_sec.append(line1)

        lbl_line1=QtWidgets.QLabel(self.groupBox)
        lbl_line1.setGeometry(QtCore.QRect(0, 0, 200,10))
        lbl_line1.setText("0.0")

        lbl_line1.setStyleSheet("color: #3a0ca3;")
        lbl_line1.setObjectName("sec1")
        lbl_line1.setVisible(True)
        self.line_sec.append(lbl_line1)
        self.line_sec[0].setStyleSheet("background-color: gray;")
        return self.line_sec

    def resetGroupBox_components(self):
        if len(self.Labels) >0 and len(self.line_sec)>0:
            for child in self.groupBox.children():
                if (isinstance(child, QFrame) and child.frameShape() == QFrame.VLine) or isinstance(child, QLabel):
                    child.deleteLater()
                if child.layout() is not None:
                # If the child has a layout, clear the layout's items
                    layout = child.layout()
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget is not None:
                            widget.deleteLater()
        

#to crop from the slider 
    def cropstart(self,time):
        self.path_label.setText("")
        #print(time)
        start_time = time
        self.list[0] =start_time
    def cropend(self,time):
        #print(time)
        end_time = time
        self.list[1]=end_time

    def init_line_dragging(self):
        self.dragging_line = False
        self.line_start_pos = QtCore.QPoint()
        self.line_sec[0].setMouseTracking(True)
        self.line_sec[0].mousePressEvent = self.line_mousePressEvent
        self.line_sec[0].mouseMoveEvent = self.line_mouseMoveEvent
        self.line_sec[0].mouseReleaseEvent = self.line_mouseReleaseEvent
        self.line_sec[0].mouseDoubleClickEvent = self.line_doublePressing

    
    def line_mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging_line = True
            self.line_start_pos = event.pos()  # Store the QPoint object
            self.guidances_label.setStyleSheet("color: #9e2a2b;")
            self.guidances_label.setText("*frame sec* button'a veya line'e çift tıklayarak kesme sınırları seçebilirsin")

    def line_mouseMoveEvent(self, event):
        if self.dragging_line:
            delta_x = event.position().x() - self.line_start_pos.x()  # Calculate the x difference
            if 0 <= self.line_sec[0].pos().x() + delta_x <= 805:
                self.line_sec[0].move(self.line_sec[0].pos().x() + delta_x, self.line_sec[0].pos().y())
                self.line_sec[1].move(self.line_sec[1].pos().x() + delta_x, self.line_sec[1].pos().y())
                hold = self.line_to_label2()
                
                self.line_sec[1].setText(f"{round(hold,3)}")
            if 830 < self.line_sec[0].pos().x() + delta_x < 0:
                self.line_sec[0].move(0, self.line_sec[0].pos().y())

    def line_mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging_line = False
            self.guidances_label.setText("")

    def line_doublePressing(self,event):
        hold = self.line_to_label2()
        self.ctr +=1
        if self.ctr%2==1:
            self.line_sec[0].setStyleSheet("background-color: #6a994e;")
            self.line_sec[1].setText(f"başlangıç frame saniyesi secildi")
            self.cropstart(hold)
 
        elif self.ctr%2==0:
            self.line_sec[0].setStyleSheet("background-color: #9e2a2b;")
            self.line_sec[1].setText(f"son frame saniyesi secildi")
            self.cropend(hold)

    def line_to_label(self):
        self.time = self.temp_hold_time
        label_time=0
        get_label_index=0
        if self.time!=0:
            frame_rate = round((self.get_label_number-1)/(self.time))
            distence= abs(self.scrollArea.horizontalScrollBar().value() - self.line_sec[0].pos().x())/200
            if distence >0:
                get_label_index= round(distence)
                label_time = get_label_index/frame_rate
            return label_time
        else: 
            return 0.0
            
    def line_to_label2(self):
        self.time = self.temp_hold_time
        label_time=0
        get_label_index=0
        if self.time!=0:
            frame_rate = round((self.get_label_number-1)/(self.time))
            #acess the labels 
            scroller_max=self.scrollArea.horizontalScrollBar().maximum()
            distence= abs(self.scrollArea.horizontalScrollBar().value() + self.line_sec[0].pos().x())/200
            if distence >0:
                get_label_index= distence
                label_time = get_label_index/frame_rate
            return label_time
        else: 
            return 0.0
 
    #clean the frames folder after the application is colsed 

    def delete_folders(self, directory=r'C:\Users\HP\Downloads\bitirme projesi\frames'):
        # Iterate over all items in the directory
        for item in os.listdir(directory):
            # Create the full path to the item
            item_path = os.path.join(directory, item)
            # Check if the item is a directory
            if os.path.isdir(item_path):
                # Recursively call delete_folders to delete subfolders and their contents
                self.delete_folders(item_path)
            else:
                # If the item is a file, remove it
                os.remove(item_path)
        
        # After deleting all files and subdirectories, remove the directory itself
        os.rmdir(directory)


class WorkerThread(QThread,QObject):
    result_signal = Signal(bool)
    def __init__(self,cap,start_frame,end_frame,out,frame_count,flag,capture,path,get_label_number,main_window=None):
        super().__init__()
        self.main_window= main_window
        self.flag= flag 

        #video kaydet parameters 
        self.cap=cap
        self.start_frame= start_frame
        self.end_frame= end_frame
        self.out= out
        self.frame_count=frame_count
        #extracte frames 
        self.capture= capture
        self.path = path 
        self.get_label_number=get_label_number

    def run(self):
        if self.flag==1 : 
            self.vido_kaydet(self.cap,self.start_frame,self.end_frame,self.out,self.frame_count)
        if self.flag==2:
            pass
        elif self.flag==3:
            flag = self.extracte_frames()
            self.result_signal.emit(flag)
 
    def vido_kaydet(self,cap,start_frame,end_frame,out,frame_count):
        for i in range(frame_count):
            ret, frame = cap.read()
            if ret == False:
                break
            if i >= start_frame and i <= end_frame:
                out.write(frame)
        self.main_window.kaydet_reventColor()

        #-------------------------------------------------------------------------------------------------
        fname = os.path.basename(self.main_window.filename).split(".")[0]
        #print("fname",fname)
        #fname= deneme2.txt
        directory_path = os.path.dirname(self.main_window.filename)
        #print("directory_path",directory_path)
        #directory_path = C:\Users\HP\Downloads\bitirme projesi\raw\testing_crop
        files = os.listdir(directory_path)
        txt_file = [file for file in files if file == fname and file.endswith('.txt')]
        
        #txt_files = deneme2.txt
        if os.path.exists(rf"{directory_path}/{fname}.txt"):
            #print("came here 532 around ")
            hold_action =[]
            #print("fcontent ",rf"{directory_path}/{fname}.txt")
            kaydedilecek_yer=  os.path.dirname(self.main_window.path_label.text())
            kaydedilecek_ismi= os.path.basename(self.main_window.path_label.text()).split(".")[0]
            output_file = rf"{kaydedilecek_yer}/{kaydedilecek_ismi}.txt"
            #print("output",output_file)
            
            fcontent= self.load_txt_file_as_array(rf"{directory_path}/{fname}.txt")
            if not fcontent[-1]:
                fcontent = fcontent[:-1]
            for _, el in enumerate(fcontent):
                if int(el.split()[0]) == int(start_frame):
                    for _,e in enumerate(fcontent):
                        if int(e.split()[0]) >=int(start_frame) and int(e.split()[0]) <= int(end_frame):
                            #print(e.split()[0])
                            hold_action.append(e)
            self.write_to_file_(output_file,hold_action)
            #print(hold_action)
        else : 
            print("there is no file like this ")
        #-------------------------------------------------------------------------------------------------
        
        #print("kaydedildi")
        cap.release()
        out.release()

    def load_txt_file_as_array(self,filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            array = np.array(lines)
        return array
    
    def write_to_file_(self, file_name, get_txt):
        with open(file_name,"w", encoding='utf-8') as file:
            for line in get_txt:
                file.write(line + "\n")
        #print(f"joint's file cropping process done ! ")

    def extracte_frames(self):
            while True:
                ret, frame = self.capture.read()
                if not ret:
                    print("couldnt extracte frames....")
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resized_frame = cv2.resize(rgb_frame, (200, 140)) 
                cv2.imwrite(rf"{self.path}\{self.get_label_number:010d}.jpg", resized_frame)
                if self.main_window.progressBar.value()<98:
                    self.main_window.progressBar.setValue(self.get_label_number)
                self.get_label_number += 1                
            self.capture.release()
            cv2.destroyAllWindows()
            return True


    







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPlayerApp()
    window.show()
    sys.exit(app.exec())
    




    
