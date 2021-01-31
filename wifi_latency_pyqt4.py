import PyQt4, sys, socket, faulthandler, time

from PyQt4.QtGui import *

from PyQt4.QtCore import QTimer

from datetime import datetime

class latency(QWidget):
    #def datad_function(self, parent=None):
    #    dw.scratchpad2.setText("datad_function called")    
    #    mylog()
            
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        faulthandler.enable()
        
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Arduino, ESP8266 Latency Test')

        myfont = PyQt4.QtGui.QFont('SansSerif', 13)
        
        button=QPushButton('start', self)
        button.setFont(myfont)
        button.setGeometry(150, 10, 200, 40)
        button.clicked.connect(self.time_function)
        
        label_start=QLabel('time start', self)
        label_start.setFont(myfont)
        label_start.setGeometry(10, 60, 100, 40)
        
        label_stop=QLabel('time return', self)
        label_stop.setFont(myfont)
        label_stop.setGeometry(10, 110, 100, 40)
        
        label_diff=QLabel('interval (ms)', self)
        label_diff.setFont(myfont)
        label_diff.setGeometry(10, 160, 100, 40)
        
        self.start_field=QLineEdit(self)
        self.start_field.setFont(myfont)
        self.start_field.setGeometry(150, 60, 200, 40)
        self.start_field.setText("time: start")
        
        self.stop_field=QLineEdit(self)
        self.stop_field.setFont(myfont)
        self.stop_field.setGeometry(150, 110, 200, 40)
        self.stop_field.setText("time: stop")
        
        self.int_field=QLineEdit(self)
        self.int_field.setFont(myfont)
        self.int_field.setGeometry(150, 160, 200, 40)
        self.int_field.setText("time: interval")
        
        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.time_function)
        self.timer.start()
        
    def time_function(self):
        tb = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H-%M-%S", tb)
        self.start_field.setText(time_str)
        
        now_b = datetime.now()
        
        HOST='192.168.1.116'
        PORT=80
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))#connect to 192.168.1.121, Arduino 2
        s.sendto("**dump2".encode(), (HOST, PORT))
        message = s.recv(60)
        
        time_return=message.decode('utf-8')
        s.close()
    
        ta = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H-%M-%S", tb)
        #time_str=time_return
        self.stop_field.setText(time_str)
        
        now_a = datetime.now()
        #self.int_field.setText(now_a-now_b)
        self.int_field.setText("%0.2f" % (now_a-now_b).total_seconds())
        
        
app=QApplication(sys.argv)

lt=latency()
lt.show()
sys.exit(app.exec_())