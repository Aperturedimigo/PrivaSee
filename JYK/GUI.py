from PyQt5.QtCore import Qt
from Jmod import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from picamera import PiCamera
from time import sleep

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # 버튼, 뷰 생성

        self.registButton = QPushButton("Register Face")
        self.registButton.clicked.connect(self.register)

        self.captureButton = QPushButton("Capture Face")
        self.captureButton.clicked.connect(self.captureImage)

        self.confirmButton = QPushButton("Confirm Face")
        self.confirmButton.clicked.connect(self.confirm)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.cancel)

        self.imageLabel = QLabel()
        self.image = QPixmap()

        # camera 실행
        self.camera = PiCamera()
        sleep(2)

        # 초기화면 세팅
        self.setPreview()

        self.imageLabel.setScaledContents(True)

        # 메인 GridLayout, 버튼 Layout 생성
        self.mainLayout = QGridLayout()
        self.buttonLayout = QVBoxLayout()
        self.buttonSecondLayout = QVBoxLayout()

        self.buttonLayout.addWidget(self.registButton)
        self.buttonLayout.addWidget(self.captureButton)
        self.buttonLayout.addWidget(self.confirmButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.registButton.hide()
        self.confirmButton.hide()
        self.cancelButton.hide()

        self.mainLayout.addWidget(self.imageLabel, 0, 0)
        self.mainLayout.addLayout(self.buttonLayout, 1, 0)

        # 초기화면 세팅
        self.setPreview()

        self.setLayout(self.mainLayout)
        self.setWindowTitle("PrivaSee")

        # 전체 화면 함수

        self.showFullScreen()



    def setPreview(self):
        # 카메라를 바라보고 사진을 찍으세요!! 이미지 : preview.jpg
        self.image = QPixmap("preview.jpg")
        self.imageLabel.setPixmap(self.image)
        self.imageLabel.setFixedWidth(600)
        self.imageLabel.setFixedHeight(int(600 * (self.image.height() / self.image.width())))


    def captureImage(self):
        # face.jpg라는 이름으로 사진 촬영
        self.camera.capture("face.jpg")
        self.image = QPixmap("face.jpg")
        self.imageLabel.setPixmap(self.image)

        self.next()


    def register(self):
        # 해야할것 싸그리 작성, cancel 냅두셈! 할일 끝나면 초기화면으로 돌아갈거에요
        # if 오류면 밑에 showPopupErrorWindow 실행, 팝업 후 초기화면으로 되돌아갈거임
        boolean = Add_Face()
        if boolean == False:
            self.showPopUpErrorWindow("register")
        else :
            self.showPopUpSuccessWindow("register")
        #############
        self.cancel()


    def confirm(self):
        # 해야할 것 싸그리 작성, cancel 냅두셈! 할일 끝나면 초기화면으로 돌아갈거에요
        # if 오류면 밑에 showPopupErrorWindow 실행
        Faceid = Detect()
        if Faceid == False:
            self.showPopUpErrorWindow("confirm")
        value = Find_Similar(Faceid)
        if value == False:
            self.showPopUpErrorWindow("confirm")
        else:
            self.showPopUpSuccessWindow("confirm")
        #############
        self.cancel()



    def next(self):
        # 찍고나서 다음 화면 세팅
        self.captureButton.hide()
        self.registButton.show()
        self.confirmButton.show()
        self.cancelButton.show()


    def cancel(self):

        # 다시 초기화면으로!
        self.registButton.hide()
        self.captureButton.show()
        self.confirmButton.hide()
        self.cancelButton.hide()

        self.setPreview()


    def showPopUpErrorWindow(self, errorForm):

        buttonReply = QMessageBox.question(self, 'Error message', "Register Error!" if errorForm == "register" else "Confirm Error!",
                                           QMessageBox.Ok, QMessageBox.Ok)

        if buttonReply == QMessageBox.Ok:
            pass

    def showPopUpSuccessWindow(self, successForm):

        buttonReply = QMessageBox.question(self, 'Success message',
                                           "Register Success!" if successForm == "register" else "Confirm Success!",
                                           QMessageBox.Ok, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            pass



if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
