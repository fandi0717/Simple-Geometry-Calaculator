from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QLineEdit, QSizePolicy, QComboBox, QMenu, QMessageBox, QStatusBar
from PySide6.QtCore import Qt, QTimer, QSize, QChildEvent, QEvent
from PySide6.QtGui import QPixmap, QAction, QIcon, QFont, QImage, QGuiApplication
import numpy as np



class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Program Sederhana Aplikasi Matematika")
        # self.setFixedSize(800,600)
        self.setMinimumSize(800, 600)
        
        
        
        
        #TODO : Add menuBar
        # menu_bar = self.menuBar()
        # File_menu = menu_bar.addMenu("Edit")
        # copy = File_menu.addAction("Copy")
        
        

        self.combo_box_2_D = QComboBox()
        self.combo_box_2_D.addItem("km")
        self.combo_box_2_D.addItem("hm")
        self.combo_box_2_D.addItem("dam")
        self.combo_box_2_D.addItem("m")
        self.combo_box_2_D.addItem("dm")
        self.combo_box_2_D.addItem("cm")
        self.combo_box_2_D.addItem("mm")
        self.combo_box_2_D.setCurrentIndex(5)


        #SetStatusTip
        self.label_tip_2 = "Mencari Luas dan Keliling"
        self.label_tip_3 = "Mencari Volume dan Luas Permukaan"
        self.label_tip_shortcut = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tShortcut :"

        # Adding toolbar in left side
        toolbar = QToolBar("My Main Toolbar")
        toolbar.setIconSize(QSize(37,37))
        self.addToolBar(Qt.LeftToolBarArea, toolbar) # SETTING SUPAYA TOOLBAR DI SEBELAH KIRI


        persegi = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_persegi.png"), "Persegi", self)
        persegi.setShortcut("Ctrl+1")
        persegi.triggered.connect(self.toolbar_persegi)
        persegi.setStatusTip(f"{self.label_tip_2} Persegi {self.label_tip_shortcut} Ctrl + 1")
        toolbar.addAction(persegi)

        
        persegi_panjang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_persegi_panjang.png"), "Persegi Panjang", self)
        persegi_panjang.setShortcut("Ctrl+2")
        persegi_panjang.triggered.connect(self.toolbar_persegi_panjang)
        persegi_panjang.setStatusTip(f"{self.label_tip_2} Persegi Panjang {self.label_tip_shortcut} Ctrl + 2")
        toolbar.addAction(persegi_panjang)

        
        lingkaran = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/icon_lingkaran.png"), "Lingkaran", self)
        lingkaran.setShortcut("Ctrl+3")
        lingkaran.triggered.connect(self.toolbar_lingkaran)
        lingkaran.setStatusTip(f"{self.label_tip_2} Lingkaran {self.label_tip_shortcut} Ctrl + 3")
        toolbar.addAction(lingkaran)
        


        layang_layang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/kite2.png"), "Layang - Layang", self)
        layang_layang.setShortcut("Ctrl+4")
        layang_layang.triggered.connect(self.toolbar_layang_layang)
        layang_layang.setStatusTip(f"{self.label_tip_2} Layang - Layang {self.label_tip_shortcut} Ctrl + 4")
        toolbar.addAction(layang_layang)

        
        segitiga = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/segitiga.png"), "Segitiga", self)
        segitiga.setShortcut("Ctrl+5")
        segitiga.triggered.connect(self.toolbar_segitiga)
        segitiga.setStatusTip(f"{self.label_tip_2} Segitiga {self.label_tip_shortcut} Ctrl + 5")
        toolbar.addAction(segitiga)


        belah_ketupat = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/belah_ketupat.png"), "Belah Ketupat", self)
        belah_ketupat.setShortcut("Ctrl+6")
        belah_ketupat.triggered.connect(self.toolbar_belah_ketupat)
        belah_ketupat.setStatusTip(f"{self.label_tip_2} Belah Ketupat {self.label_tip_shortcut} Ctrl + 6")
        toolbar.addAction(belah_ketupat)

        trapesium = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium.png"), "Trapesium", self)
        # trapesium.setShortcut("Ctrl+7")
        # trapesium.setShortcut("Ctrl+8")
        trapesium.setStatusTip(f"{self.label_tip_2} Trapesium {self.label_tip_shortcut} Ctrl + 7 | Ctrl + 8")
        trapesium.setMenu(self.createTrapesiumMenu())
        toolbar.addAction(trapesium)

        jajar_genjang = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/jajar_genjang.png"), "Jajar Genjang", self)
        jajar_genjang.setShortcut("Ctrl+9")
        jajar_genjang.triggered.connect(self.toolbar_jajar_genjang)
        jajar_genjang.setStatusTip(f"{self.label_tip_2} Jajar Genjang {self.label_tip_shortcut} Ctrl + 9")
        toolbar.addAction(jajar_genjang)


        kubus = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/kubus.png"), "Kubus", self)
        kubus.setStatusTip(f"{self.label_tip_3} Kubus {self.label_tip_shortcut} Ctrl + Shift + 1")
        kubus.setShortcut("Ctrl+Shift+1")
        kubus.triggered.connect(self.toolbar_kubus)
        toolbar.addAction(kubus)

        balok = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/balok.png"), "Balok", self)
        balok.setStatusTip(f"{self.label_tip_3} Balok {self.label_tip_shortcut} Ctrl + Shift + 2")
        balok.setShortcut("Ctrl+Shift+2")
        balok.triggered.connect(self.toolbar_balok)
        toolbar.addAction(balok)


        tabung = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/tabung.png"), "Tabung", self)
        tabung.setStatusTip(f"{self.label_tip_3} Tabung {self.label_tip_shortcut} Ctrl + Shift + 3")
        tabung.setShortcut("Ctrl+Shift+3")
        tabung.triggered.connect(self.toolbar_tabung)
        toolbar.addAction(tabung)

        bola = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/bola.png"), "Bola", self)
        bola.setStatusTip(f"{self.label_tip_3} Bola {self.label_tip_shortcut} Ctrl + Shift + 4")
        bola.setShortcut("Ctrl+Shift+4")
        bola.triggered.connect(self.toolbar_bola)
        toolbar.addAction(bola)


        prisma = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma.png"), "Prisma", self)
        prisma.setStatusTip(f"{self.label_tip_3} Prisma {self.label_tip_shortcut} Ctrl + Shift + 5 | Ctrl + Shift + 6 | Ctrl + Shift + 7 | Ctrl + Shift + 8")
        # prisma.setShortcut("Ctrl+Shift+5")
        # prisma.setShortcut("Ctrl+Shift+6")
        # prisma.setShortcut("Ctrl+Shift+7")
        # prisma.setShortcut("Ctrl+Shift+8")
        prisma.setMenu(self.createPrismaMenu())
        toolbar.addAction(prisma)

        
    
        self.my_font = QFont()
        self.my_font.setPointSize(20)


        self.setStatusBar(QStatusBar(self))



    def createTrapesiumMenu(self):
        trapesium_menu = QMenu(self)

        trapesium_sama_kaki = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium.png"),'Trapesium Sama Kaki', self)
        trapesium_sama_kaki.setStatusTip(f"{self.label_tip_2} Trapesium Sama Kaki {self.label_tip_shortcut} Ctrl + 7")
        trapesium_sama_kaki.setShortcut("Ctrl+7")
        trapesium_sama_kaki.triggered.connect(self.toolbar_trapesium_sama_kaki)
        trapesium_menu.addAction(trapesium_sama_kaki)

        trapesium_siku_siku = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/trapesium_1.png"),'Trapesium Siku - Siku', self)
        trapesium_siku_siku.setStatusTip(f"{self.label_tip_2} Trapesium Siku - Siku {self.label_tip_shortcut} Ctrl + 8")
        trapesium_siku_siku.setShortcut("Ctrl+8")
        trapesium_siku_siku.triggered.connect(self.toolbar_trapesium_siku_siku)
        trapesium_menu.addAction(trapesium_siku_siku)

        return trapesium_menu


    def createPrismaMenu(self):
        Prisma_menu = QMenu(self)

        prisma_segitiga = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_3.png"), "Prisma Segitiga", self)
        prisma_segitiga.setStatusTip(f"{self.label_tip_3} Prisma Segitiga {self.label_tip_shortcut} Ctrl + Shift + 5")
        prisma_segitiga.setShortcut("Ctrl+Shift+5")
        prisma_segitiga.triggered.connect(self.toolbar_prisma_segitiga)
        Prisma_menu.addAction(prisma_segitiga)

        prisma_segilima = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segilima_10.png"), "Prisma Segilima", self)
        prisma_segilima.setStatusTip(f"{self.label_tip_3} Prisma Segilima {self.label_tip_shortcut} Ctrl + Shift + 6")
        prisma_segilima.setShortcut("Ctrl+Shift+6")
        prisma_segilima.triggered.connect(self.toolbar_prisma_segilima)
        Prisma_menu.addAction(prisma_segilima)


        prisma_segienam = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segilima_3.png"), "Prisma Segienam", self)
        prisma_segienam.setStatusTip(f"{self.label_tip_3} Prisma Segienam {self.label_tip_shortcut} Ctrl + Shift + 7")
        prisma_segienam.setShortcut("Ctrl+Shift+7")
        prisma_segienam.triggered.connect(self.toolbar_prisma_segienam)
        Prisma_menu.addAction(prisma_segienam)

        prisma_segidelapan = QAction(QIcon("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/prisma_segidelapan.jpg"), "Prisma Segidelapan", self)
        prisma_segidelapan.setStatusTip(f"{self.label_tip_3} Prisma Segidelapan {self.label_tip_shortcut} Ctrl + Shift + 8")
        prisma_segidelapan.setShortcut("Ctrl+Shift+8")
        prisma_segidelapan.triggered.connect(self.toolbar_prisma_segidelapan)
        Prisma_menu.addAction(prisma_segidelapan)

        return Prisma_menu

    
    

    def toolbar_persegi(self):
        qwidget = QWidget()
    
        text_s = QLabel("panjang s :")
        self.input_s = QLineEdit()

        # text_s.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        # self.input_s.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_s = QHBoxLayout()
        layout_1_h_s.addWidget(text_s)
        layout_1_h_s.addWidget(self.input_s)
        layout_1_h_s.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.persegi)
        

        
        self.text_param_persegi = QLabel("Persegi")
        self.text_param_persegi.setAlignment(Qt.AlignHCenter)
        self.text_param_persegi.setFont(self.my_font)
        self.text_param_persegi.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_persegi.png"))
        
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        
        layout_2_v_s = QVBoxLayout()
        layout_2_v_s.addWidget(self.text_param_persegi)
        layout_2_v_s.addWidget(label)
        layout_2_v_s.addLayout(layout_1_h_s)
        layout_2_v_s.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_s = QVBoxLayout()
        layout_2_v_s.addLayout(self.layout_v_answer_s)

        qwidget.setLayout(layout_2_v_s)

        self.setCentralWidget(qwidget)

    def persegi(self):
        try:
            if self.input_s.text() == "":
                s = 0
            else:
                s = float(self.input_s.text())

            luas = s**2
            keliling = 4*s

            self.answer_label_2 = QLabel("Luas Persegi : ")
            self.jawab = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")
            self.answer_label_3 = QLabel("Keliling Persegi : ")
            self.jawab_2 = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_s.count():
                item = self.layout_v_answer_s.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            self.layout_v_answer_s.addWidget(self.answer_label_2)
            self.layout_v_answer_s.addWidget(self.jawab)
            self.layout_v_answer_s.addWidget(self.answer_label_3)
            self.layout_v_answer_s.addWidget(self.jawab_2)


        except ValueError:
            self.error_input()


        

        


    def toolbar_persegi_panjang(self):
        qwidget = QWidget()

        text_r_p = QLabel("Masukkan panjang\t:")
        text_r_l = QLabel("Masukkan lebar\t\t:")
        self.input_r_p = QLineEdit()
        self.input_r_l = QLineEdit()

        text_r_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_r_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_r_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_r_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_r = QHBoxLayout()
        layout_1_h_r.addWidget(text_r_p)
        layout_1_h_r.addWidget(self.input_r_p)

        layout_2_h_r = QHBoxLayout()
        layout_2_h_r.addWidget(text_r_l)
        layout_2_h_r.addWidget(self.input_r_l)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.persegi_panjang)

        layout_3_h_r = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_r.addWidget(label_satuan)
        layout_3_h_r.addLayout(self.layout_combo_box)

        self.text_param_persegi_panjang = QLabel("Persegi Panjang")
        self.text_param_persegi_panjang.setAlignment(Qt.AlignHCenter)
        self.text_param_persegi_panjang.setFont(self.my_font)
        self.text_param_persegi_panjang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_persegi_panjang.jpg"))
        label.setPixmap(QPixmap("label_persegi_panjang.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_3_v_r = QVBoxLayout()
        layout_3_v_r.addWidget(self.text_param_persegi_panjang)
        layout_3_v_r.addWidget(label)
        layout_3_v_r.addLayout(layout_1_h_r)
        layout_3_v_r.addLayout(layout_2_h_r)
        layout_3_v_r.addLayout(layout_3_h_r)
        layout_3_v_r.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_r = QVBoxLayout()
        layout_3_v_r.addLayout(self.layout_v_answer_r)

        qwidget.setLayout(layout_3_v_r)

        self.setCentralWidget(qwidget)


    def persegi_panjang(self):
        try:
            if self.input_r_p.text() == "" or self.input_r_l.text() == "":
                p = 0
                l = 0
            else:
                p = float(self.input_r_p.text())
                l = float(self.input_r_l.text())

            luas = p*l
            keliling = 2*(p+l)

            #Luas
            self.answer_label_luas_rect = QLabel("Luas Persegi Panjang : ")
            self.jawab_luas_rect = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keliling
            self.answer_label_kel_rect = QLabel("Keliling Persegi Panjang : ")
            self.jawab_kel_rect = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_r.count():
                item = self.layout_v_answer_r.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_r.addWidget(self.answer_label_luas_rect)
            self.layout_v_answer_r.addWidget(self.jawab_luas_rect)
            self.layout_v_answer_r.addWidget(self.answer_label_kel_rect)
            self.layout_v_answer_r.addWidget(self.jawab_kel_rect)

        except ValueError:
            self.error_input()

        

        
    def toolbar_lingkaran(self):
        qwidget = QWidget()

        text_j = QLabel("Masukkan jari - jari (Radius)\t:")
        self.input_j = QLineEdit()

        text_j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_j.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_c = QHBoxLayout()
        layout_1_h_c.addWidget(text_j)
        layout_1_h_c.addWidget(self.input_j)
        layout_1_h_c.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.lingkaran)

        self.text_param_lingkaran = QLabel("Lingkaran")
        self.text_param_lingkaran.setAlignment(Qt.AlignHCenter)
        self.text_param_lingkaran.setFont(self.my_font)
        self.text_param_lingkaran.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_lingkaran2.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_c = QVBoxLayout()
        layout_2_v_c.addWidget(self.text_param_lingkaran)
        layout_2_v_c.addWidget(label)
        layout_2_v_c.addLayout(layout_1_h_c)
        layout_2_v_c.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_c = QVBoxLayout()
        layout_2_v_c.addLayout(self.layout_v_answer_c)

        qwidget.setLayout(layout_2_v_c)

        self.setCentralWidget(qwidget)

    def lingkaran(self):
        try:
            if self.input_j.text() == "":
                r = 0
            else:
                r = float(self.input_j.text())

            luas = np.pi * (r**2)
            keliling = np.pi*(2*r)
            

            self.answer_label_luas_circle = QLabel("Luas Lingkaran : ")
            self.jawab_luas_circle = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²\t({str(np.round(luas))} {self.combo_box_2_D.currentText()}²)")
            self.answer_label_kel_circle = QLabel("Keliling Lingkaran : ")
            self.jawab_kel_circle = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}\t({str(np.round(keliling))} {self.combo_box_2_D.currentText()})")

            while self.layout_v_answer_c.count():
                item = self.layout_v_answer_c.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            self.layout_v_answer_c.addWidget(self.answer_label_luas_circle)
            self.layout_v_answer_c.addWidget(self.jawab_luas_circle)
            self.layout_v_answer_c.addWidget(self.answer_label_kel_circle)
            self.layout_v_answer_c.addWidget(self.jawab_kel_circle)

        except ValueError:
            self.error_input()

    
    def toolbar_layang_layang(self):
        qwidget = QWidget()

        text_kite_luas = QLabel("Mencari Luas")
        text_kite_d1 = QLabel("Masukkan panjang d1\t\t:")
        text_kite_d2 = QLabel("Masukkan panjang d2\t\t:")
        text_kite_keliling = QLabel("Mencari keliling Diketahui [a] dan [b]")
        text_kite_a = QLabel("Masukkan panjang a\t\t:")
        text_kite_b = QLabel("Masukkan panjang b\t\t:")



        self.input_kite_d1 = QLineEdit()
        self.input_kite_d2 = QLineEdit()
        self.input_kite_a = QLineEdit()
        self.input_kite_b = QLineEdit()

        text_kite_luas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_keliling.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_kite_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.input_kite_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_kite_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_kite = QHBoxLayout()
        layout_1_h_kite.addWidget(text_kite_d1)
        layout_1_h_kite.addWidget(self.input_kite_d1)

        layout_2_h_kite = QHBoxLayout()
        layout_2_h_kite.addWidget(text_kite_d2)
        layout_2_h_kite.addWidget(self.input_kite_d2)

        layout_3_h_kite = QHBoxLayout()
        layout_3_h_kite.addWidget(text_kite_a)
        layout_3_h_kite.addWidget(self.input_kite_a)

        layout_4_h_kite = QHBoxLayout()
        layout_4_h_kite.addWidget(text_kite_b)
        layout_4_h_kite.addWidget(self.input_kite_b)


        layout_5_h_kite = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_5_h_kite.addWidget(label_satuan)
        layout_5_h_kite.addLayout(self.layout_combo_box)


        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.layang_layang)

        label_kosong = QLabel()

        self.text_param_layang_layang = QLabel("Layang - Layang")
        self.text_param_layang_layang.setAlignment(Qt.AlignHCenter)
        self.text_param_layang_layang.setFont(self.my_font)
        self.text_param_layang_layang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_layang-layang.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_6_v_kite = QVBoxLayout()
        layout_6_v_kite.addWidget(self.text_param_layang_layang)
        layout_6_v_kite.addWidget(label)
        layout_6_v_kite.addWidget(text_kite_luas)
        layout_6_v_kite.addLayout(layout_1_h_kite)
        layout_6_v_kite.addLayout(layout_2_h_kite)
        layout_6_v_kite.addWidget(label_kosong)
        layout_6_v_kite.addWidget(text_kite_keliling)
        layout_6_v_kite.addLayout(layout_3_h_kite)
        layout_6_v_kite.addLayout(layout_4_h_kite)
        layout_6_v_kite.addWidget(label_kosong)
        layout_6_v_kite.addLayout(layout_5_h_kite)
        layout_6_v_kite.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_kite = QVBoxLayout()
        layout_6_v_kite.addLayout(self.layout_v_answer_kite)

        qwidget.setLayout(layout_6_v_kite)

        self.setCentralWidget(qwidget)



    def layang_layang(self):
        try: 
            global d1, d2, a, b
            if self.input_kite_d1.text() == "" or self.input_kite_d2.text() == "":
                d1 = 0
                d2 = 0

            elif self.input_kite_d1.text() != "" or self.input_kite_d2.text() != "":
                d1 = float(self.input_kite_d1.text())
                d2 = float(self.input_kite_d2.text())
            


            if self.input_kite_a.text() == "" or self.input_kite_b.text() == "":
                a = 0
                b = 0

            elif self.input_kite_a.text() != "" or self.input_kite_b.text() != "":
                a = float(self.input_kite_a.text())
                b = float(self.input_kite_b.text())
                
            
            luas = 1/2* (d1 * d2)
            keliling = (a * 2) + (b * 2)

            #Luas
            self.answer_label_luas_kite = QLabel("Luas Layang - layang\t:")
            self.jawab_luas_kite = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keliling
            self.answer_label_kel_kite = QLabel("Keliling layang - layang\t:")
            self.jawab_kel_kite = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")


            while self.layout_v_answer_kite.count():
                item = self.layout_v_answer_kite.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_kite.addWidget(self.answer_label_luas_kite)
            self.layout_v_answer_kite.addWidget(self.jawab_luas_kite)
            self.layout_v_answer_kite.addWidget(self.answer_label_kel_kite)
            self.layout_v_answer_kite.addWidget(self.jawab_kel_kite)

        except ValueError:
            self.error_input()




    def toolbar_segitiga(self):
        qwidget = QWidget()

        text_t_a = QLabel("Masukkan alas\t:")
        text_t_t = QLabel("Masukkan tinggi\t:")
        self.input_t_a = QLineEdit()
        self.input_t_t = QLineEdit()

        text_t_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_t_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_t_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_t_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_t = QHBoxLayout()
        layout_1_h_t.addWidget(text_t_a)
        layout_1_h_t.addWidget(self.input_t_a)

        layout_2_h_t = QHBoxLayout()
        layout_2_h_t.addWidget(text_t_t)
        layout_2_h_t.addWidget(self.input_t_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.segitiga)

        layout_3_h_t = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_t.addWidget(label_satuan)
        layout_3_h_t.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_segitiga = QLabel("Segitiga")
        self.text_param_segitiga.setAlignment(Qt.AlignHCenter)
        self.text_param_segitiga.setFont(self.my_font)
        self.text_param_segitiga.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_segitiga.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_3_v_segitiga = QVBoxLayout()
        layout_3_v_segitiga.addWidget(self.text_param_segitiga)
        layout_3_v_segitiga.addWidget(label)
        layout_3_v_segitiga.addLayout(layout_1_h_t)
        layout_3_v_segitiga.addLayout(layout_2_h_t)
        layout_3_v_segitiga.addWidget(label_kosong)
        layout_3_v_segitiga.addLayout(layout_3_h_t)
        layout_3_v_segitiga.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_triangle = QVBoxLayout()
        layout_3_v_segitiga.addLayout(self.layout_v_answer_triangle)

        qwidget.setLayout(layout_3_v_segitiga)

        self.setCentralWidget(qwidget)


    def segitiga(self):
        try:
            if self.input_t_a.text() == "" or self.input_t_t.text() == "":
                a = 0
                t = 0

            else:
                a = float(self.input_t_a.text())
                t = float(self.input_t_t.text())

            luas = 1/2 * (a * t)
            keliling = ((np.sqrt((a**2) + (t**2))) * 2) + a

            #Luas
            self.answer_label_luas_triangle = QLabel("Luas Segitiga : ")
            self.jawab_luas_triangle = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keliling
            self.answer_label_kel_triangle = QLabel("Keliling Segitiga : ")
            self.jawab_kel_triangle = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_triangle.count():
                item = self.layout_v_answer_triangle.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_triangle.addWidget(self.answer_label_luas_triangle)
            self.layout_v_answer_triangle.addWidget(self.jawab_luas_triangle)
            self.layout_v_answer_triangle.addWidget(self.answer_label_kel_triangle)
            self.layout_v_answer_triangle.addWidget(self.jawab_kel_triangle)

        except ValueError:
            self.error_input()


    def toolbar_belah_ketupat(self):
        qwidget = QWidget()

        text_belahKetupat_d1 = QLabel("Masukkan panjang d1\t:")
        text_belahKetupat_d2 = QLabel("Masukkan panjang d2\t:")
        self.input_belahKetupat_d1 = QLineEdit()
        self.input_belahKetupat_d2 = QLineEdit()

        text_belahKetupat_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_belahKetupat_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_belahKetupat_d1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_belahKetupat_d2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_belahKetupat = QHBoxLayout()
        layout_1_h_belahKetupat.addWidget(text_belahKetupat_d1)
        layout_1_h_belahKetupat.addWidget(self.input_belahKetupat_d1)

        layout_2_h_belahKetupat = QHBoxLayout()
        layout_2_h_belahKetupat.addWidget(text_belahKetupat_d2)
        layout_2_h_belahKetupat.addWidget(self.input_belahKetupat_d2)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.belah_ketupat)

        layout_3_h_belahKetupat = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_belahKetupat.addWidget(label_satuan)
        layout_3_h_belahKetupat.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_belah_ketupat = QLabel("Belah Ketupat")
        self.text_param_belah_ketupat.setAlignment(Qt.AlignHCenter)
        self.text_param_belah_ketupat.setFont(self.my_font)
        self.text_param_belah_ketupat.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_belah_ketupat.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_3_v_belahKetupat = QVBoxLayout()
        layout_3_v_belahKetupat.addWidget(self.text_param_belah_ketupat)
        layout_3_v_belahKetupat.addWidget(label)
        layout_3_v_belahKetupat.addLayout(layout_1_h_belahKetupat)
        layout_3_v_belahKetupat.addLayout(layout_2_h_belahKetupat)
        layout_3_v_belahKetupat.addWidget(label_kosong)
        layout_3_v_belahKetupat.addLayout(layout_3_h_belahKetupat)
        layout_3_v_belahKetupat.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_belahKetupat = QVBoxLayout()
        layout_3_v_belahKetupat.addLayout(self.layout_v_answer_belahKetupat)

        qwidget.setLayout(layout_3_v_belahKetupat)

        self.setCentralWidget(qwidget)


    def belah_ketupat(self):
        try:
            if self.input_belahKetupat_d1.text() == "" or self.input_belahKetupat_d2.text() == "":
                d1 = 0
                d2 = 0

            else:
                d1 = float(self.input_belahKetupat_d1.text())
                d2 = float(self.input_belahKetupat_d2.text())

            luas = 1/2 * (d1 * d2)
            keliling = 4 * (np.sqrt(((d2 // 2) **2) + ((d1 // 2) **2)))

            #Luas
            self.answer_label_luas_belahKetupat = QLabel("Luas Belah Ketupat : ")
            self.jawab_luas_belahKetupat = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keliling
            self.answer_label_kel_belahKetupat = QLabel("Keliling Belah Ketupat : ")
            self.jawab_kel_belahKetupat = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_belahKetupat.count():
                item = self.layout_v_answer_belahKetupat.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_belahKetupat.addWidget(self.answer_label_luas_belahKetupat)
            self.layout_v_answer_belahKetupat.addWidget(self.jawab_luas_belahKetupat)
            self.layout_v_answer_belahKetupat.addWidget(self.answer_label_kel_belahKetupat)
            self.layout_v_answer_belahKetupat.addWidget(self.jawab_kel_belahKetupat)

        except ValueError:
            self.error_input()


    def toolbar_trapesium_sama_kaki(self):
        qwidget = QWidget()

        text_trapesiumSamaKaki_a = QLabel("Masukkan panjang a\t:")
        text_trapesiumSamaKaki_b = QLabel("Masukkan panjang b\t:")
        text_trapesiumSamaKaki_t = QLabel("Masukkan tinggi\t\t:")
        self.input_trapesiumSamaKaki_a = QLineEdit()
        self.input_trapesiumSamaKaki_b = QLineEdit()
        self.input_trapesiumSamaKaki_t = QLineEdit()

        text_trapesiumSamaKaki_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSamaKaki_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSamaKaki_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSamaKaki_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_trapesiumSamaKaki = QHBoxLayout()
        layout_1_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_a)
        layout_1_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_a)

        layout_2_h_trapesiumSamaKaki = QHBoxLayout()
        layout_2_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_b)
        layout_2_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_b)

        layout_3_h_trapesiumSamaKaki = QHBoxLayout()
        layout_3_h_trapesiumSamaKaki.addWidget(text_trapesiumSamaKaki_t)
        layout_3_h_trapesiumSamaKaki.addWidget(self.input_trapesiumSamaKaki_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.trapesiumSamaKaki)

        layout_4_h_trapesiumSamaKaki = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_trapesiumSamaKaki.addWidget(label_satuan)
        layout_4_h_trapesiumSamaKaki.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_trapesium_sama_kaki = QLabel("Trapesium Sama Kaki")
        self.text_param_trapesium_sama_kaki.setAlignment(Qt.AlignHCenter)
        self.text_param_trapesium_sama_kaki.setFont(self.my_font)
        self.text_param_trapesium_sama_kaki.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_trapesium_sama_kaki.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_trapesiumSamaKaki = QVBoxLayout()
        layout_5_v_trapesiumSamaKaki.addWidget(self.text_param_trapesium_sama_kaki)
        layout_5_v_trapesiumSamaKaki.addWidget(label)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_1_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_2_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_3_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addWidget(label_kosong)
        layout_5_v_trapesiumSamaKaki.addLayout(layout_4_h_trapesiumSamaKaki)
        layout_5_v_trapesiumSamaKaki.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_trapesiumSamaKaki = QVBoxLayout()
        layout_5_v_trapesiumSamaKaki.addLayout(self.layout_v_answer_trapesiumSamaKaki)

        qwidget.setLayout(layout_5_v_trapesiumSamaKaki)

        self.setCentralWidget(qwidget)


    def trapesiumSamaKaki(self):
        try:
            if self.input_trapesiumSamaKaki_a.text() == "" or self.input_trapesiumSamaKaki_b.text() == "" or self.input_trapesiumSamaKaki_t.text() == "":
                a = 0
                b = 0
                t = 0
            else:
                a = float(self.input_trapesiumSamaKaki_a.text())
                b = float(self.input_trapesiumSamaKaki_b.text())
                t = float(self.input_trapesiumSamaKaki_t.text())

            luas = 1/2 * (a + b) * t

            sisa_b_min_a = b - a
            sisi_miring = np.sqrt(((sisa_b_min_a ** 2) + (t ** 2))) 
            keliling = a + b + (sisi_miring * 2)

            #luas
            self.answer_label_luas_TrapesiumSamaKaki = QLabel("Luas Trapesium Sama Kaki : ")
            self.jawab_luas_TrapesiumSamaKaki = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keiling
            self.answer_label_kel_TrapesiumSamaKaki = QLabel("Keliling Trapesium Sama Kaki : ")
            self.jawab_kel_TrapesiumSamaKaki = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_trapesiumSamaKaki.count():
                item = self.layout_v_answer_trapesiumSamaKaki.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.answer_label_luas_TrapesiumSamaKaki)
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.jawab_luas_TrapesiumSamaKaki)
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.answer_label_kel_TrapesiumSamaKaki)
            self.layout_v_answer_trapesiumSamaKaki.addWidget(self.jawab_kel_TrapesiumSamaKaki)

        except ValueError:
            self.error_input()


    def toolbar_trapesium_siku_siku(self):
        qwidget = QWidget()

        text_trapesiumSikuSiku_a = QLabel("Masukkan panjang a\t:")
        text_trapesiumSikuSiku_b = QLabel("Masukkan panjang b\t:")
        text_trapesiumSikuSiku_t = QLabel("Masukkan tinggi\t\t:")
        self.input_trapesiumSikuSiku_a = QLineEdit()
        self.input_trapesiumSikuSiku_b = QLineEdit()
        self.input_trapesiumSikuSiku_t = QLineEdit()

        text_trapesiumSikuSiku_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSikuSiku_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_trapesiumSikuSiku_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_trapesiumSikuSiku_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_trapesiumSikuSiku = QHBoxLayout()
        layout_1_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_a)
        layout_1_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_a)

        layout_2_h_trapesiumSikuSiku = QHBoxLayout()
        layout_2_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_b)
        layout_2_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_b)

        layout_3_h_trapesiumSikuSiku = QHBoxLayout()
        layout_3_h_trapesiumSikuSiku.addWidget(text_trapesiumSikuSiku_t)
        layout_3_h_trapesiumSikuSiku.addWidget(self.input_trapesiumSikuSiku_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.trapesiumSikuSiku)

        layout_4_h_trapesiumSikuSiku = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_trapesiumSikuSiku.addWidget(label_satuan)
        layout_4_h_trapesiumSikuSiku.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_trapesium_siku_siku = QLabel("Trapesium Siku - Siku")
        self.text_param_trapesium_siku_siku.setAlignment(Qt.AlignHCenter)
        self.text_param_trapesium_siku_siku.setFont(self.my_font)
        self.text_param_trapesium_siku_siku.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_trapesium_siku_siku.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_trapesiumSikuSiku = QVBoxLayout()
        layout_5_v_trapesiumSikuSiku.addWidget(self.text_param_trapesium_siku_siku)
        layout_5_v_trapesiumSikuSiku.addWidget(label)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_1_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_2_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_3_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addWidget(label_kosong)
        layout_5_v_trapesiumSikuSiku.addLayout(layout_4_h_trapesiumSikuSiku)
        layout_5_v_trapesiumSikuSiku.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_trapesiumSikuSiku = QVBoxLayout()
        layout_5_v_trapesiumSikuSiku.addLayout(self.layout_v_answer_trapesiumSikuSiku)

        qwidget.setLayout(layout_5_v_trapesiumSikuSiku)

        self.setCentralWidget(qwidget)


    def trapesiumSikuSiku(self):
        try:
            if self.input_trapesiumSikuSiku_a.text() == "" or self.input_trapesiumSikuSiku_b.text() == "" or self.input_trapesiumSikuSiku_t.text() == "":
                a = 0
                b = 0
                t = 0
            else:
                a = float(self.input_trapesiumSikuSiku_a.text())
                b = float(self.input_trapesiumSikuSiku_b.text())
                t = float(self.input_trapesiumSikuSiku_t.text())

            luas = 1/2 * (a + b) * t

            sisa_b_min_a = b - a
            sisi_miring = np.sqrt(((sisa_b_min_a ** 2) + (t ** 2))) 
            keliling = a + b + sisi_miring + t

            #luas
            self.answer_label_luas_trapesiumSikuSiku = QLabel("Luas Trapesium Siku - Siku : ")
            self.jawab_luas_trapesiumSikuSiku = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keiling
            self.answer_label_kel_trapesiumSikuSiku = QLabel("Keliling Trapesium Siku - Siku : ")
            self.jawab_kel_trapesiumSikuSiku = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")

            while self.layout_v_answer_trapesiumSikuSiku.count():
                item = self.layout_v_answer_trapesiumSikuSiku.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.answer_label_luas_trapesiumSikuSiku)
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.jawab_luas_trapesiumSikuSiku)
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.answer_label_kel_trapesiumSikuSiku)
            self.layout_v_answer_trapesiumSikuSiku.addWidget(self.jawab_kel_trapesiumSikuSiku)

        except ValueError:
            self.error_input()



    def toolbar_jajar_genjang(self):
        qwidget = QWidget()

        text_jajarGenjang_luas = QLabel("Mencari Luas")
        text_jajarGenjang_a = QLabel("Masukkan panjang a (alas)\t\t:")
        text_jajarGenjang_t = QLabel("Masukkan tinggi\t\t\t:")
        text_jajarGenjang_keliling = QLabel("Mencari keliling Diketahui [a] dan [b]")
        text_jajarGenjang_a_2 = QLabel("Masukkan panjang a (alas)\t\t:")
        text_jajarGenjang_b = QLabel("Masukkan panjang b\t\t:")



        self.input_jajarGenjang_a = QLineEdit()
        self.input_jajarGenjang_t = QLineEdit()
        self.input_jajarGenjang_a_2 = QLineEdit()
        self.input_jajarGenjang_b = QLineEdit()

        text_jajarGenjang_luas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_keliling.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_a_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_jajarGenjang_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.input_jajarGenjang_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_a_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_jajarGenjang_b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_jajarGenjang = QHBoxLayout()
        layout_1_h_jajarGenjang.addWidget(text_jajarGenjang_a)
        layout_1_h_jajarGenjang.addWidget(self.input_jajarGenjang_a)

        layout_2_h_jajarGenjang = QHBoxLayout()
        layout_2_h_jajarGenjang.addWidget(text_jajarGenjang_t)
        layout_2_h_jajarGenjang.addWidget(self.input_jajarGenjang_t)

        layout_3_h_jajarGenjang = QHBoxLayout()
        layout_3_h_jajarGenjang.addWidget(text_jajarGenjang_a_2)
        layout_3_h_jajarGenjang.addWidget(self.input_jajarGenjang_a_2)

        layout_4_h_jajarGenjang = QHBoxLayout()
        layout_4_h_jajarGenjang.addWidget(text_jajarGenjang_b)
        layout_4_h_jajarGenjang.addWidget(self.input_jajarGenjang_b)


        layout_5_h_jajarGenjang = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_5_h_jajarGenjang.addWidget(label_satuan)
        layout_5_h_jajarGenjang.addLayout(self.layout_combo_box)


        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.jajar_genjang)

        label_kosong = QLabel()

        self.text_param_jajar_genjang = QLabel("Jajar Genjang")
        self.text_param_jajar_genjang.setAlignment(Qt.AlignHCenter)
        self.text_param_jajar_genjang.setFont(self.my_font)
        self.text_param_jajar_genjang.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_jajar_genjang.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_6_v_jajarGenjang = QVBoxLayout()
        layout_6_v_jajarGenjang.addWidget(self.text_param_jajar_genjang)
        layout_6_v_jajarGenjang.addWidget(label)
        layout_6_v_jajarGenjang.addWidget(text_jajarGenjang_luas)
        layout_6_v_jajarGenjang.addLayout(layout_1_h_jajarGenjang)
        layout_6_v_jajarGenjang.addLayout(layout_2_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(label_kosong)
        layout_6_v_jajarGenjang.addWidget(text_jajarGenjang_keliling)
        layout_6_v_jajarGenjang.addLayout(layout_3_h_jajarGenjang)
        layout_6_v_jajarGenjang.addLayout(layout_4_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(label_kosong)
        layout_6_v_jajarGenjang.addLayout(layout_5_h_jajarGenjang)
        layout_6_v_jajarGenjang.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_jajarGenjang = QVBoxLayout()
        layout_6_v_jajarGenjang.addLayout(self.layout_v_answer_jajarGenjang)

        qwidget.setLayout(layout_6_v_jajarGenjang)

        self.setCentralWidget(qwidget)



    def jajar_genjang(self):   
        try:
            if self.input_jajarGenjang_a.text() == "" or self.input_jajarGenjang_t.text() == "":
                a = 0
                t = 0

            elif self.input_jajarGenjang_a.text() != "" or self.input_jajarGenjang_t.text() != "":
                a = float(self.input_jajarGenjang_a.text())
                t = float(self.input_jajarGenjang_t.text())
            


            if self.input_jajarGenjang_a_2.text() == "" or self.input_jajarGenjang_b.text() == "":
                a2 = 0
                b = 0

            elif self.input_jajarGenjang_a_2.text() != "" or self.input_jajarGenjang_b.text() != "":
                a2 = float(self.input_jajarGenjang_a_2.text())
                b = float(self.input_jajarGenjang_b.text())
                
            
            luas = a * t
            keliling = 2 * (a2 + b)

            #Luas
            self.answer_label_luas_jajarGenjang = QLabel("Luas Jajar Genjang\t:")
            self.jawab_luas_jajarGenjang = QLabel(f"{str(luas)} {self.combo_box_2_D.currentText()}²")


            #Keliling
            self.answer_label_kel_jajarGenjang = QLabel("Keliling Jajar Genjang\t:")
            self.jawab_kel_jajarGenjang = QLabel(f"{str(keliling)} {self.combo_box_2_D.currentText()}")


            while self.layout_v_answer_jajarGenjang.count():
                item = self.layout_v_answer_jajarGenjang.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_jajarGenjang.addWidget(self.answer_label_luas_jajarGenjang)
            self.layout_v_answer_jajarGenjang.addWidget(self.jawab_luas_jajarGenjang)
            self.layout_v_answer_jajarGenjang.addWidget(self.answer_label_kel_jajarGenjang)
            self.layout_v_answer_jajarGenjang.addWidget(self.jawab_kel_jajarGenjang)

        except ValueError:
            self.error_input()



    def toolbar_kubus(self):
        qwidget = QWidget()

        text_cubic = QLabel("Masukkan s :")
        self.input_cubic = QLineEdit()

        text_cubic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_cubic.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_cubic = QHBoxLayout()
        layout_1_h_cubic.addWidget(text_cubic)
        layout_1_h_cubic.addWidget(self.input_cubic)
        layout_1_h_cubic.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.kubus)

        self.text_param_kubus = QLabel("Kubus")
        self.text_param_kubus.setAlignment(Qt.AlignHCenter)
        self.text_param_kubus.setFont(self.my_font)
        self.text_param_kubus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_kubus.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_cubic = QVBoxLayout()
        layout_2_v_cubic.addWidget(self.text_param_kubus)
        layout_2_v_cubic.addWidget(label)
        layout_2_v_cubic.addLayout(layout_1_h_cubic)
        layout_2_v_cubic.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_cubic = QVBoxLayout()
        layout_2_v_cubic.addLayout(self.layout_v_answer_cubic)

        qwidget.setLayout(layout_2_v_cubic)

        self.setCentralWidget(qwidget)

    def kubus(self):
        try:
            if self.input_cubic.text() == "":
                s = 0

            else:
                s = float(self.input_cubic.text())

            volume = s**3
            luas_permukaan = 6*(s**2)

            self.answer_label_vol_cubic = QLabel("Volume Persegi : ")
            self.jawab_vol_cubic = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")
            self.answer_label_lp_cubic = QLabel("Luas permukaan Persegi : ")
            self.jawab_lp_cubic = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_cubic.count():
                item = self.layout_v_answer_cubic.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            self.layout_v_answer_cubic.addWidget(self.answer_label_vol_cubic)
            self.layout_v_answer_cubic.addWidget(self.jawab_vol_cubic )
            self.layout_v_answer_cubic.addWidget(self.answer_label_lp_cubic)
            self.layout_v_answer_cubic.addWidget(self.jawab_lp_cubic)

        except ValueError:
            self.error_input()





    def toolbar_balok(self):
        qwidget = QWidget()

        text_balok_p = QLabel("Masukkan panjang\t:")
        text_balok_l = QLabel("Masukkan lebar\t\t:")
        text_balok_t = QLabel("Masukkan tinggi\t\t:")
        self.input_balok_p = QLineEdit()
        self.input_balok_l = QLineEdit()
        self.input_balok_t = QLineEdit()

        text_balok_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_balok_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_balok_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_p.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_l.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_balok_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_balok = QHBoxLayout()
        layout_1_h_balok.addWidget(text_balok_p)
        layout_1_h_balok.addWidget(self.input_balok_p)

        layout_2_h_balok = QHBoxLayout()
        layout_2_h_balok.addWidget(text_balok_l)
        layout_2_h_balok.addWidget(self.input_balok_l)

        layout_3_h_balok = QHBoxLayout()
        layout_3_h_balok.addWidget(text_balok_t)
        layout_3_h_balok.addWidget(self.input_balok_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.balok)

        layout_4_h_balok = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_balok.addWidget(label_satuan)
        layout_4_h_balok.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_balok = QLabel("Balok")
        self.text_param_balok.setAlignment(Qt.AlignHCenter)
        self.text_param_balok.setFont(self.my_font)
        self.text_param_balok.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_balok.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_5_v_balok = QVBoxLayout()
        layout_5_v_balok.addWidget(self.text_param_balok)
        layout_5_v_balok.addWidget(label)
        layout_5_v_balok.addLayout(layout_1_h_balok)
        layout_5_v_balok.addLayout(layout_2_h_balok)
        layout_5_v_balok.addLayout(layout_3_h_balok)
        layout_5_v_balok.addWidget(label_kosong)
        layout_5_v_balok.addLayout(layout_4_h_balok)
        layout_5_v_balok.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_balok = QVBoxLayout()
        layout_5_v_balok.addLayout(self.layout_v_answer_balok)

        qwidget.setLayout(layout_5_v_balok)

        self.setCentralWidget(qwidget)


    def balok(self):
        try:
            if self.input_balok_p.text() == "" or self.input_balok_l.text() == "" or self.input_balok_t.text() == "":
                p = 0
                l = 0
                t = 0
            else:
                p = float(self.input_balok_p.text())
                l = float(self.input_balok_l.text())
                t = float(self.input_balok_t.text())

            volume = p*l*t
            luas_permukaan = 2*((p*l) + (p*t) + (l*t))

            #volume
            self.answer_label_vol_balok = QLabel("Volume Balok : ")
            self.jawab_vol_balok = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")


            #luas permukaan
            self.answer_label_lp_balok = QLabel("Luas permukaan Balok : ")
            self.jawab_lp_balok = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_balok.count():
                item = self.layout_v_answer_balok.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_balok.addWidget(self.answer_label_vol_balok)
            self.layout_v_answer_balok.addWidget(self.jawab_vol_balok)
            self.layout_v_answer_balok.addWidget(self.answer_label_lp_balok)
            self.layout_v_answer_balok.addWidget(self.jawab_lp_balok)

        except ValueError:
            self.error_input()

    def toolbar_tabung(self):
        qwidget = QWidget()

        text_tabung_r = QLabel("Masukkan radius\t:")
        text_tabung_t = QLabel("Masukkan tinggi\t:")
        self.input_tabung_r = QLineEdit()
        self.input_tabung_t = QLineEdit()

        text_tabung_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_tabung_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_tabung_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_tabung_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_tabung = QHBoxLayout()
        layout_1_h_tabung.addWidget(text_tabung_r)
        layout_1_h_tabung.addWidget(self.input_tabung_r)

        layout_2_h_tabung = QHBoxLayout()
        layout_2_h_tabung.addWidget(text_tabung_t)
        layout_2_h_tabung.addWidget(self.input_tabung_t)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.tabung)

        layout_3_h_tabung = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_tabung.addWidget(label_satuan)
        layout_3_h_tabung.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_tabung = QLabel("Tabung")
        self.text_param_tabung.setAlignment(Qt.AlignHCenter)
        self.text_param_tabung.setFont(self.my_font)
        self.text_param_tabung.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_tabung.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_3_v_tabung = QVBoxLayout()
        layout_3_v_tabung.addWidget(self.text_param_tabung)
        layout_3_v_tabung.addWidget(label)
        layout_3_v_tabung.addLayout(layout_1_h_tabung)
        layout_3_v_tabung.addLayout(layout_2_h_tabung)
        layout_3_v_tabung.addWidget(label_kosong)
        layout_3_v_tabung.addLayout(layout_3_h_tabung)
        layout_3_v_tabung.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_tabung = QVBoxLayout()
        layout_3_v_tabung.addLayout(self.layout_v_answer_tabung)

        qwidget.setLayout(layout_3_v_tabung)

        self.setCentralWidget(qwidget)


    def tabung(self):
        try:
            if self.input_tabung_r.text() == "" or self.input_tabung_t.text() == "":
                r = 0
                t = 0

            else:
                r = float(self.input_tabung_r.text())
                t = float(self.input_tabung_t.text())

            volume = (np.pi * r**2) * t
            luas_permukaan = 2 * np.pi * r * (r + t)

            #volume
            self.answer_label_vol_tabung = QLabel("Volume Tabung : ")
            self.jawab_vol_tabung = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³\t({str(np.round(volume))} {self.combo_box_2_D.currentText()}³)")


            #luas Permukaan
            self.answer_label_lp_tabung = QLabel("Luas Permukaan Tabung : ")
            self.jawab_lp_tabung = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²\t({str(np.round(luas_permukaan))} {self.combo_box_2_D.currentText()}²)")

            while self.layout_v_answer_tabung.count():
                item = self.layout_v_answer_tabung.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_tabung.addWidget(self.answer_label_vol_tabung)
            self.layout_v_answer_tabung.addWidget(self.jawab_vol_tabung)
            self.layout_v_answer_tabung.addWidget(self.answer_label_lp_tabung)
            self.layout_v_answer_tabung.addWidget(self.jawab_lp_tabung)

        except ValueError:
            self.error_input()


    def toolbar_bola(self):
        qwidget = QWidget()

        text_bola_r = QLabel("Masukkan radius\t:")
        self.input_bola_r = QLineEdit()

        text_bola_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_bola_r.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_bola = QHBoxLayout()
        layout_1_h_bola.addWidget(text_bola_r)
        layout_1_h_bola.addWidget(self.input_bola_r)
        layout_1_h_bola.addLayout(self.layout_combo_box)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.bola)

        self.text_param_bola = QLabel("Bola")
        self.text_param_bola.setAlignment(Qt.AlignHCenter)
        self.text_param_bola.setFont(self.my_font)
        self.text_param_bola.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_bola.jpg"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_2_v_bola = QVBoxLayout()
        layout_2_v_bola.addWidget(self.text_param_bola)
        layout_2_v_bola.addWidget(label)
        layout_2_v_bola.addLayout(layout_1_h_bola)
        layout_2_v_bola.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_bola = QVBoxLayout()
        layout_2_v_bola.addLayout(self.layout_v_answer_bola)

        qwidget.setLayout(layout_2_v_bola)

        self.setCentralWidget(qwidget)

    def bola(self):
        try:
            if self.input_bola_r.text() == "":
                r = 0

            else:
                r = float(self.input_bola_r.text())

            volume = 4/3 * np.pi * (r**3)
            luas_permukaan = 4 * np.pi * (r**2)

            self.answer_label_vol_bola = QLabel("Volume Bola : ")
            self.jawab_vol_bola = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³\t({str(np.round(volume))} {self.combo_box_2_D.currentText()}³)")
            self.answer_label_lp_bola = QLabel("Luas permukaan Bola : ")
            self.jawab_lp_bola = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²\t({str(np.round(luas_permukaan))} {self.combo_box_2_D.currentText()}²)")

            while self.layout_v_answer_bola.count():
                item = self.layout_v_answer_bola.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_s
            self.layout_v_answer_bola.addWidget(self.answer_label_vol_bola)
            self.layout_v_answer_bola.addWidget(self.jawab_vol_bola )
            self.layout_v_answer_bola.addWidget(self.answer_label_lp_bola)
            self.layout_v_answer_bola.addWidget(self.jawab_lp_bola)

        except ValueError:
            self.error_input()


    


    def toolbar_prisma_segitiga(self):
        qwidget = QWidget()

        text_prismaSegitiga_a = QLabel("Masukkan panjang alas segitiga\t:")
        text_prismaSegitiga_t = QLabel("Masukkan tinggi segitiga\t\t:")
        text_prismaSegitiga_tPS = QLabel("Masukkan tinggi Prisma\t\t:")
        self.input_prismaSegitiga_a = QLineEdit()
        self.input_prismaSegitiga_t = QLineEdit()
        self.input_prismaSegitiga_tPS = QLineEdit()

        text_prismaSegitiga_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegitiga_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegitiga_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegitiga_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_prismaSegitiga = QHBoxLayout()
        layout_1_h_prismaSegitiga.addWidget(text_prismaSegitiga_a)
        layout_1_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_a)

        layout_2_h_prismaSegitiga = QHBoxLayout()
        layout_2_h_prismaSegitiga.addWidget(text_prismaSegitiga_t)
        layout_2_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_t)

        layout_3_h_prismaSegitiga = QHBoxLayout()
        layout_3_h_prismaSegitiga.addWidget(text_prismaSegitiga_tPS)
        layout_3_h_prismaSegitiga.addWidget(self.input_prismaSegitiga_tPS)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.prismaSegitiga)

        layout_4_h_prismaSegitiga = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_prismaSegitiga.addWidget(label_satuan)
        layout_4_h_prismaSegitiga.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegitiga = QLabel("Prisma Segitiga")
        self.text_param_Prismasegitiga.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegitiga.setFont(self.my_font)
        self.text_param_Prismasegitiga.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segitiga_2.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_5_v_prismaSegitiga = QVBoxLayout()
        layout_5_v_prismaSegitiga.addWidget(self.text_param_Prismasegitiga)
        layout_5_v_prismaSegitiga.addWidget(label)
        layout_5_v_prismaSegitiga.addLayout(layout_1_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addLayout(layout_2_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addLayout(layout_3_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addWidget(label_kosong)
        layout_5_v_prismaSegitiga.addLayout(layout_4_h_prismaSegitiga)
        layout_5_v_prismaSegitiga.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegitiga = QVBoxLayout()
        layout_5_v_prismaSegitiga.addLayout(self.layout_v_answer_prismaSegitiga)

        qwidget.setLayout(layout_5_v_prismaSegitiga)

        self.setCentralWidget(qwidget)


    def prismaSegitiga(self): 
        try:
            if self.input_prismaSegitiga_a.text() == "" or self.input_prismaSegitiga_t.text() == "" or self.input_prismaSegitiga_tPS.text() == "":
                a = 0
                t = 0
                tPS = 0

            
            else:
                a = float(self.input_prismaSegitiga_a.text())
                t = float(self.input_prismaSegitiga_t.text())
                tPS = float(self.input_prismaSegitiga_tPS.text())


            volume = (1/2 * a * t) * tPS
            sisi_miring_alas = np.sqrt((a**2 + t**2))
            luas_permukaan = (2* (1/2 * a * t)) + ((a + t + sisi_miring_alas) * tPS)

            #volume
            self.answer_label_vol_prismaSegitiga = QLabel("Volume prisma Segitiga : ")
            self.jawab_vol_prismaSegitiga = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")

            


            #luas permukaan
            self.answer_label_lp_prismaSegitiga = QLabel("Luas permukaan prisma Segitiga : ")
            self.jawab_lp_prismaSegitiga = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_prismaSegitiga.count():
                item = self.layout_v_answer_prismaSegitiga.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_prismaSegitiga.addWidget(self.answer_label_vol_prismaSegitiga)
            self.layout_v_answer_prismaSegitiga.addWidget(self.jawab_vol_prismaSegitiga)
            self.layout_v_answer_prismaSegitiga.addWidget(self.answer_label_lp_prismaSegitiga)
            self.layout_v_answer_prismaSegitiga.addWidget(self.jawab_lp_prismaSegitiga)

        except ValueError:
            self.error_input()




    def toolbar_prisma_segilima(self):
        qwidget = QWidget()

        text_prismaSegilima_a = QLabel("Masukkan panjang alas Segitiga\t\t:")
        text_prismaSegilima_t = QLabel("Masukkan tinggi segitiga\t\t\t:")
        text_prismaSegilima_tPS = QLabel("Masukkan tinggi Prisma Segilima\t\t:")
        self.input_prismaSegilima_a = QLineEdit()
        self.input_prismaSegilima_t = QLineEdit()
        self.input_prismaSegilima_tPS = QLineEdit()

        text_prismaSegilima_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegilima_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegilima_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegilima_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_prismaSegilima = QHBoxLayout()
        layout_1_h_prismaSegilima.addWidget(text_prismaSegilima_a)
        layout_1_h_prismaSegilima.addWidget(self.input_prismaSegilima_a)

        layout_2_h_prismaSegilima = QHBoxLayout()
        layout_2_h_prismaSegilima.addWidget(text_prismaSegilima_t)
        layout_2_h_prismaSegilima.addWidget(self.input_prismaSegilima_t)

        layout_3_h_prismaSegilima = QHBoxLayout()
        layout_3_h_prismaSegilima.addWidget(text_prismaSegilima_tPS)
        layout_3_h_prismaSegilima.addWidget(self.input_prismaSegilima_tPS)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.prismaSegilima)

        layout_4_h_prismaSegilima = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_4_h_prismaSegilima.addWidget(label_satuan)
        layout_4_h_prismaSegilima.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegilima = QLabel("Prisma Segilima")
        self.text_param_Prismasegilima.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegilima.setFont(self.my_font)
        self.text_param_Prismasegilima.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segilima.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)


        layout_5_v_prismaSegilima = QVBoxLayout()
        layout_5_v_prismaSegilima.addWidget(self.text_param_Prismasegilima)
        layout_5_v_prismaSegilima.addWidget(label)
        layout_5_v_prismaSegilima.addLayout(layout_1_h_prismaSegilima)
        layout_5_v_prismaSegilima.addLayout(layout_2_h_prismaSegilima)
        layout_5_v_prismaSegilima.addLayout(layout_3_h_prismaSegilima)
        layout_5_v_prismaSegilima.addWidget(label_kosong)
        layout_5_v_prismaSegilima.addLayout(layout_4_h_prismaSegilima)
        layout_5_v_prismaSegilima.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegilima = QVBoxLayout()
        layout_5_v_prismaSegilima.addLayout(self.layout_v_answer_prismaSegilima)

        qwidget.setLayout(layout_5_v_prismaSegilima)

        self.setCentralWidget(qwidget)


    def prismaSegilima(self): 
        try:
            if self.input_prismaSegilima_a.text() == "" or self.input_prismaSegilima_t.text() == "" or self.input_prismaSegilima_tPS.text() == "":
                a = 0
                t = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegilima_a.text())
                t = float(self.input_prismaSegilima_t.text())
                tPS = float(self.input_prismaSegilima_tPS.text())

            volume = ((1/2 * a * t) * 5)  * tPS
            luas_permukaan = (2 * ((1/2 * a * t) * 5)) + (5 * (a * tPS))
            #volume
            self.answer_label_vol_prismaSegilima = QLabel("Volume prisma Segilima : ")
            self.jawab_vol_prismaSegilima = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")


            #luas permukaan
            self.answer_label_lp_prismaSegilima = QLabel("Luas permukaan prisma Segilima : ")
            self.jawab_lp_prismaSegilima = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_prismaSegilima.count():
                item = self.layout_v_answer_prismaSegilima.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_prismaSegilima.addWidget(self.answer_label_vol_prismaSegilima)
            self.layout_v_answer_prismaSegilima.addWidget(self.jawab_vol_prismaSegilima)
            self.layout_v_answer_prismaSegilima.addWidget(self.answer_label_lp_prismaSegilima)
            self.layout_v_answer_prismaSegilima.addWidget(self.jawab_lp_prismaSegilima)

        except ValueError:
            self.error_input()



    def toolbar_prisma_segienam(self):
        qwidget = QWidget()

        text_prismaSegienam_a = QLabel("Masukkan panjang alas Segitiga\t\t:")
        text_prismaSegienam_tPS = QLabel("Masukkan tinggi Prisma Segienam\t\t:")
        self.input_prismaSegienam_a = QLineEdit()
        self.input_prismaSegienam_tPS = QLineEdit()

        text_prismaSegienam_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegienam_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegienam_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.input_prismaSegienam_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_prismaSegienam = QHBoxLayout()
        layout_1_h_prismaSegienam.addWidget(text_prismaSegienam_a)
        layout_1_h_prismaSegienam.addWidget(self.input_prismaSegienam_a)

        layout_2_h_prismaSegienam = QHBoxLayout()
        layout_2_h_prismaSegienam.addWidget(text_prismaSegienam_tPS)
        layout_2_h_prismaSegienam.addWidget(self.input_prismaSegienam_tPS)


        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.prismaSegienam)

        layout_3_h_prismaSegienam = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_prismaSegienam.addWidget(label_satuan)
        layout_3_h_prismaSegienam.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegienam = QLabel("Prisma Segienam")
        self.text_param_Prismasegienam.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegienam.setFont(self.my_font)
        self.text_param_Prismasegienam.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segienam.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        layout_4_v_prismaSegienam = QVBoxLayout()
        layout_4_v_prismaSegienam.addWidget(self.text_param_Prismasegienam)
        layout_4_v_prismaSegienam.addWidget(label)
        layout_4_v_prismaSegienam.addLayout(layout_1_h_prismaSegienam)
        layout_4_v_prismaSegienam.addLayout(layout_2_h_prismaSegienam)
        layout_4_v_prismaSegienam.addWidget(label_kosong)
        layout_4_v_prismaSegienam.addLayout(layout_3_h_prismaSegienam)
        layout_4_v_prismaSegienam.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegienam = QVBoxLayout()
        layout_4_v_prismaSegienam.addLayout(self.layout_v_answer_prismaSegienam)

        qwidget.setLayout(layout_4_v_prismaSegienam)

        self.setCentralWidget(qwidget)


    def prismaSegienam(self):
        try: 
            if self.input_prismaSegienam_a.text() == "" or self.input_prismaSegienam_tPS.text() == "":
                a = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegienam_a.text())
                tPS = float(self.input_prismaSegienam_tPS.text())

            sisi_miring = np.sqrt(((a**2) - ((a / 2)**2)))
            luas_alas = (1/2 * a * sisi_miring) * 6
            volume = luas_alas * tPS
            luas_permukaan = (luas_alas * 2) + ((a * tPS) * 6)
            #volume
            self.answer_label_vol_prismaSegienam = QLabel("Volume prisma Segilima : ")
            self.jawab_vol_prismaSegienam = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")


            #luas permukaan
            self.answer_label_lp_prismaSegienam = QLabel("Luas permukaan prisma Segilima : ")
            self.jawab_lp_prismaSegienam = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_prismaSegienam.count():
                item = self.layout_v_answer_prismaSegienam.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_prismaSegienam.addWidget(self.answer_label_vol_prismaSegienam)
            self.layout_v_answer_prismaSegienam.addWidget(self.jawab_vol_prismaSegienam)
            self.layout_v_answer_prismaSegienam.addWidget(self.answer_label_lp_prismaSegienam)
            self.layout_v_answer_prismaSegienam.addWidget(self.jawab_lp_prismaSegienam)

        except ValueError:
            self.error_input()




    def toolbar_prisma_segidelapan(self):
        qwidget = QWidget()

        text_prismaSegidelapan_a = QLabel("Masukkan panjang sisi alas Segidelapan\t\t:")
        text_prismaSegidelapan_tPS = QLabel("Masukkan tinggi Prisma Segidelapan\t\t:")
        self.input_prismaSegidelapan_a = QLineEdit()
        self.input_prismaSegidelapan_tPS = QLineEdit()

        text_prismaSegidelapan_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_prismaSegidelapan_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_prismaSegidelapan_a.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.input_prismaSegidelapan_tPS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout_combo_box = QVBoxLayout()
        self.layout_combo_box.addWidget(self.combo_box_2_D)

        layout_1_h_prismaSegidelapan = QHBoxLayout()
        layout_1_h_prismaSegidelapan.addWidget(text_prismaSegidelapan_a)
        layout_1_h_prismaSegidelapan.addWidget(self.input_prismaSegidelapan_a)

        layout_2_h_prismaSegidelapan = QHBoxLayout()
        layout_2_h_prismaSegidelapan.addWidget(text_prismaSegidelapan_tPS)
        layout_2_h_prismaSegidelapan.addWidget(self.input_prismaSegidelapan_tPS)


        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.prismaSegidelapan)

        layout_3_h_prismaSegidelapan = QHBoxLayout()
        label_satuan = QLabel("Satuan")
        layout_3_h_prismaSegidelapan.addWidget(label_satuan)
        layout_3_h_prismaSegidelapan.addLayout(self.layout_combo_box)

        label_kosong = QLabel()

        self.text_param_Prismasegidelapan = QLabel("Prisma Segidelapan")
        self.text_param_Prismasegidelapan.setAlignment(Qt.AlignHCenter)
        self.text_param_Prismasegidelapan.setFont(self.my_font)
        self.text_param_Prismasegidelapan.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        label = QLabel() 
        label.setPixmap(QPixmap("D:/Data_C2/Users/Documents/Tutorial_Python/pyside6/projek/img_project/label_prisma_segidelapan.jpg"))
        # label.setPixmap(QPixmap("label_prisma_segienam.png"))
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)



        layout_4_v_prismaSegidelapan = QVBoxLayout()
        layout_4_v_prismaSegidelapan.addWidget(self.text_param_Prismasegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(label)
        layout_4_v_prismaSegidelapan.addLayout(layout_1_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addLayout(layout_2_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(label_kosong)
        layout_4_v_prismaSegidelapan.addLayout(layout_3_h_prismaSegidelapan)
        layout_4_v_prismaSegidelapan.addWidget(self.button_submit)

        # Create a new QVBoxLayout for the answer label
        self.layout_v_answer_prismaSegidelapan = QVBoxLayout()
        layout_4_v_prismaSegidelapan.addLayout(self.layout_v_answer_prismaSegidelapan)

        qwidget.setLayout(layout_4_v_prismaSegidelapan)

        self.setCentralWidget(qwidget)


    def prismaSegidelapan(self): 
        try:
            if self.input_prismaSegidelapan_a.text() == "" or self.input_prismaSegidelapan_tPS.text() == "":
                a = 0
                tPS = 0
            else:
                a = float(self.input_prismaSegidelapan_a.text())
                tPS = float(self.input_prismaSegidelapan_tPS.text())

            sisi_miring = np.sqrt(((a**2) - ((a / 2)**2)))
            luas_alas = (2 + (2*np.sqrt(2))) * a**2
            volume = luas_alas * tPS
            luas_permukaan = (luas_alas * 2) + ((a * tPS) * 8)
            #volume
            self.answer_label_vol_prismaSegidelapan = QLabel("Volume prisma Segidelapan : ")
            self.jawab_vol_prismaSegidelapan = QLabel(f"{str(volume)} {self.combo_box_2_D.currentText()}³")


            #luas permukaan
            self.answer_label_lp_prismaSegidelapan = QLabel("Luas permukaan prisma Segidelapan : ")
            self.jawab_lp_prismaSegidelapan = QLabel(f"{str(luas_permukaan)} {self.combo_box_2_D.currentText()}²")

            while self.layout_v_answer_prismaSegidelapan.count():
                item = self.layout_v_answer_prismaSegidelapan.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

            # Add the answer label to the new layout_v_answer_r
            self.layout_v_answer_prismaSegidelapan.addWidget(self.answer_label_vol_prismaSegidelapan)
            self.layout_v_answer_prismaSegidelapan.addWidget(self.jawab_vol_prismaSegidelapan)
            self.layout_v_answer_prismaSegidelapan.addWidget(self.answer_label_lp_prismaSegidelapan)
            self.layout_v_answer_prismaSegidelapan.addWidget(self.jawab_lp_prismaSegidelapan)

        except ValueError:
            self.error_input()


    

    def error_input(self) -> QMessageBox.critical:
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Error Message!!!")
        message.setText("Input Invalid")
        message.setInformativeText("Input yang Anda Masukkan tidak sesuai.\nInput harus berupa :\n1. Bilangan Bulat       --> e.g. (1)\n2. Bilangan Desimal  --> e.g. (1.2)\n3. None")
        message.setIcon(QMessageBox.Critical)
        # message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)     # menampilkan 2 button click
        message.setStandardButtons(QMessageBox.Ok)                        # menampilkan 1 button click
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            None

    
    #TODO : Add Bangun Ruang 3 Dimensi : Kerucut, Limas