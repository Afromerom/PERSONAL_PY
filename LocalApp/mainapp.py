from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QTableWidgetItem
import pandas as pd

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(913, 510)
        # Inicializar variables para almacenar los datos cargados
        self.mrna_data = None
        self.mirna_data = None
        
        self.Versionstate = QtWidgets.QLabel(Dialog)
        self.Versionstate.setGeometry(QtCore.QRect(370, 50, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Versionstate.setFont(font)
        self.Versionstate.setAlignment(QtCore.Qt.AlignCenter)
        self.Versionstate.setObjectName("Versionstate")
        self.Date = QtWidgets.QLabel(Dialog)
        self.Date.setGeometry(QtCore.QRect(440, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Date.setFont(font)
        self.Date.setAlignment(QtCore.Qt.AlignCenter)
        self.Date.setObjectName("Date")
        self.TITLE = QtWidgets.QLabel(Dialog)
        self.TITLE.setGeometry(QtCore.QRect(380, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE.setObjectName("TITLE")
        self.valor1 = QtWidgets.QLabel(Dialog)
        self.valor1.setGeometry(QtCore.QRect(330, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1.setFont(font)
        self.valor1.setText("")
        self.valor1.setObjectName("valor1")
        self.valor1_2 = QtWidgets.QLabel(Dialog)
        self.valor1_2.setGeometry(QtCore.QRect(250, 230, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_2.setFont(font)
        self.valor1_2.setText("")
        self.valor1_2.setObjectName("valor1_2")
        self.valor1_3 = QtWidgets.QLabel(Dialog)
        self.valor1_3.setGeometry(QtCore.QRect(250, 260, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_3.setFont(font)
        self.valor1_3.setText("")
        self.valor1_3.setObjectName("valor1_3")
        
        
        self.UPLOAD_MRNA = QtWidgets.QPushButton(Dialog)
        self.UPLOAD_MRNA.setGeometry(QtCore.QRect(380, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UPLOAD_MRNA.setFont(font)
        self.UPLOAD_MRNA.setObjectName("UPLOAD_MRNA")
        self.UPLOAD_MRNA.setText("UPLOAD MRNA")
        
        self.GRAF_MRNA = QTableWidget(Dialog)
        self.GRAF_MRNA.setGeometry(QtCore.QRect(20, 230, 421, 161))
        self.GRAF_MRNA.setObjectName("GRAF_MRNA")
        
        
        
        self.dataload1 = QtWidgets.QLabel(Dialog)
        self.dataload1.setGeometry(QtCore.QRect(130, 130, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.dataload1.setFont(font)
        self.dataload1.setObjectName("dataload1")
        
        
        self.progressBarmRNA = QtWidgets.QProgressBar(Dialog)
        self.progressBarmRNA.setGeometry(QtCore.QRect(500, 130, 118, 23))
        self.progressBarmRNA.setProperty("value", 0)
        self.progressBarmRNA.setObjectName("progressBarmRNA")
        
        
        self.CHECKSTATE = QtWidgets.QPushButton(Dialog)
        self.CHECKSTATE.setGeometry(QtCore.QRect(720, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CHECKSTATE.setFont(font)
        self.CHECKSTATE.setObjectName("CHECKSTATE")
        self.CHECKSTATE.setText("CHECK")
        
        
        self.dataload2 = QtWidgets.QLabel(Dialog)
        self.dataload2.setGeometry(QtCore.QRect(130, 160, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.dataload2.setFont(font)
        self.dataload2.setObjectName("dataload2")
        
        self.UPLOAD_MIRNA = QtWidgets.QPushButton(Dialog)
        self.UPLOAD_MIRNA.setGeometry(QtCore.QRect(380, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UPLOAD_MIRNA.setFont(font)
        self.UPLOAD_MIRNA.setObjectName("UPLOAD_MIRNA")
        self.UPLOAD_MIRNA.setText("UPLOAD miRNA")
        
        
        self.progressBarmiRNA = QtWidgets.QProgressBar(Dialog)
        self.progressBarmiRNA.setGeometry(QtCore.QRect(500, 160, 118, 23))
        self.progressBarmiRNA.setProperty("value", 0)
        self.progressBarmiRNA.setObjectName("progressBarmiRNA")
        
        self.GRAF_MIRNA = QTableWidget(Dialog)
        self.GRAF_MIRNA.setGeometry(QtCore.QRect(470, 230, 421, 161))
        self.GRAF_MIRNA.setObjectName("GRAF_MIRNA")
        
        self.CONFIRMATION1 = QtWidgets.QLabel(Dialog)
        self.CONFIRMATION1.setGeometry(QtCore.QRect(630, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.CONFIRMATION1.setFont(font)
        self.CONFIRMATION1.setText("")
        self.CONFIRMATION1.setObjectName("CONFIRMATION1")
        self.CONFIRMATION2 = QtWidgets.QLabel(Dialog)
        self.CONFIRMATION2.setGeometry(QtCore.QRect(630, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.CONFIRMATION2.setFont(font)
        self.CONFIRMATION2.setText("")
        self.CONFIRMATION2.setObjectName("CONFIRMATION2")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(470, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.Notification = QtWidgets.QLabel(Dialog)
        self.Notification.setGeometry(QtCore.QRect(20, 420, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.Notification.setFont(font)
        self.Notification.setObjectName("Notification")
        self.TIMECALC = QtWidgets.QLabel(Dialog)
        self.TIMECALC.setGeometry(QtCore.QRect(250, 420, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.TIMECALC.setFont(font)
        self.TIMECALC.setText("")
        self.TIMECALC.setAlignment(QtCore.Qt.AlignCenter)
        self.TIMECALC.setObjectName("TIMECALC")
        self.FINALSTATE = QtWidgets.QLabel(Dialog)
        self.FINALSTATE.setGeometry(QtCore.QRect(190, 460, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.FINALSTATE.setFont(font)
        self.FINALSTATE.setText("")
        self.FINALSTATE.setAlignment(QtCore.Qt.AlignCenter)
        self.FINALSTATE.setObjectName("FINALSTATE")
        self.ExportMessage = QtWidgets.QLabel(Dialog)
        self.ExportMessage.setGeometry(QtCore.QRect(510, 420, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.ExportMessage.setFont(font)
        self.ExportMessage.setObjectName("ExportMessage")
        self.SAVEFILE = QtWidgets.QPushButton(Dialog)
        self.SAVEFILE.setGeometry(QtCore.QRect(790, 410, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SAVEFILE.setFont(font)
        self.SAVEFILE.setObjectName("SAVEFILE")
        self.EXECUTE = QtWidgets.QPushButton(Dialog)
        self.EXECUTE.setGeometry(QtCore.QRect(720, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EXECUTE.setFont(font)
        self.EXECUTE.setObjectName("EXECUTE")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
         # Conectar los botones a sus funciones correspondientes
        self.UPLOAD_MRNA.clicked.connect(self.upload_mrna)
        self.UPLOAD_MIRNA.clicked.connect(self.upload_mirna)
        self.CHECKSTATE.clicked.connect(self.show_csv_data) 
        
        
    def upload_mrna(self):
        fileName, _ = QFileDialog.getOpenFileName(
            None, 
            "Select CSV File", 
            "", 
            "CSV Files (*.csv);;All Files (*)"
        )
        if fileName:
            print("mRNA file selected:", fileName)
            self.progressBarmRNA.setValue(0)
            self.mrna_data = pd.read_csv(fileName)
            self.simulate_progress(self.progressBarmRNA, self.CONFIRMATION1)

    def upload_mirna(self):
        fileName, _ = QFileDialog.getOpenFileName(
            None, 
            "Select CSV File", 
            "", 
            "CSV Files (*.csv);;All Files (*)"
        )
        if fileName:
            print("miRNA file selected:", fileName)
            self.progressBarmiRNA.setValue(0)
            self.mirna_data = pd.read_csv(fileName)
            self.simulate_progress(self.progressBarmiRNA, self.CONFIRMATION2)

    def simulate_progress(self, progressBar, confirmationLabel):
        # Simular la carga del archivo con un temporizador
        self.timer = QtCore.QTimer()
        self.progress_value = 0
        self.timer.timeout.connect(lambda: self.update_progress(progressBar, confirmationLabel))
        self.timer.start(100)  # Simular la carga cada 100ms

    def update_progress(self, progressBar, confirmationLabel):
        if self.progress_value < 100:
            self.progress_value += 10
            progressBar.setValue(self.progress_value)
        else:
            self.timer.stop()
            confirmationLabel.setText("loaded")
            confirmationLabel.setStyleSheet("color: green")

    def show_csv_data(self):
        # Mostrar las primeras 5 filas y 4 columnas del archivo mRNA
        if self.mrna_data is not None:
            mrna_preview = self.mrna_data.iloc[:5, :4]
            self.populate_table(self.GRAF_MRNA, mrna_preview)
        
        # Mostrar las primeras 5 filas y 4 columnas del archivo miRNA
        if self.mirna_data is not None:
            mirna_preview = self.mirna_data.iloc[:5, :4]
            self.populate_table(self.GRAF_MIRNA, mirna_preview)

    def populate_table(self, table_widget, data):
        # Configurar el número de filas y columnas del widget
        table_widget.setRowCount(data.shape[0])
        table_widget.setColumnCount(data.shape[1])
        
        # Insertar los encabezados de columna
        table_widget.setHorizontalHeaderLabels(data.columns)

        # Insertar los datos en la tabla
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                table_widget.setItem(i, j, QTableWidgetItem(str(data.iat[i, j])))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PTC"))
        self.Versionstate.setText(_translate("Dialog", "Version 1.1"))
        self.Date.setText(_translate("Dialog", "2024 "))
        self.TITLE.setText(_translate("Dialog", "PTC"))
        self.UPLOAD_MRNA.setText(_translate("Dialog", "UPLOAD"))
        self.dataload1.setText(_translate("Dialog", "CSV file upload of mRNA "))
        self.CHECKSTATE.setText(_translate("Dialog", "CHECK"))
        self.dataload2.setText(_translate("Dialog", "CSV file upload of miRNA "))
        self.UPLOAD_MIRNA.setText(_translate("Dialog", "UPLOAD"))
        self.label_23.setText(_translate("Dialog", "mRNA "))
        self.label_24.setText(_translate("Dialog", "miRNA "))
        self.Notification.setText(_translate("Dialog", "Estimated analysis time is : "))
        self.ExportMessage.setText(_translate("Dialog", " Download the list of predictors "))
        self.SAVEFILE.setText(_translate("Dialog", "SAVE"))
        self.EXECUTE.setText(_translate("Dialog", "RUN"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())