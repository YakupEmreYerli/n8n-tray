"""
n8n Tray - GUI Modülü
Bu modül ana pencereyi ve tüm GUI bileşenlerini oluşturur.
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import styles
import ctypes
import sys


class MainWindow(QtWidgets.QWidget):
    """Ana pencere sınıfı"""
    
    def __init__(self, icon, process_manager):
        super().__init__()
        self.process_manager = process_manager
        self.init_ui(icon)
        
    def init_ui(self, icon):
        """Arayüzü başlat"""
        self.setWindowTitle("n8n Kontrol Paneli")
        self.setWindowIcon(icon)
        self.setFixedSize(600, 520)
        
        # Global stil ayarları (tüm diyaloglar için)
        app = QtWidgets.QApplication.instance()
        if app:
            app.setStyleSheet(styles.WINDOW_STYLE + styles.MESSAGEBOX_STYLE + 
                            styles.MENU_STYLE + styles.FILEDIALOG_STYLE)
        
        self.setStyleSheet(styles.WINDOW_STYLE)
        
        # Ana düzen
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)
        
        # Başlık
        self.create_header(layout)
        layout.addSpacing(10)
        
        # Durum göstergeleri
        self.create_status_indicators(layout)
        layout.addSpacing(12)
        
        # Butonlar
        self.create_buttons(layout)
        layout.addSpacing(8)
        
        # Acil Durdurma butonu
        self.create_emergency_button(layout)
        layout.addSpacing(10)
        
        # Log alanı
        self.create_log_area(layout)
        
        self.setLayout(layout)
        self.update_status()
    
    def enable_dark_titlebar(self):
        """Windows 11 başlık çubuğunu karanlık yap"""
        if sys.platform == "win32":
            try:
                hwnd = int(self.winId())
                # DWMWA_USE_IMMERSIVE_DARK_MODE = 20 (Windows 11)
                # DWMWA_USE_IMMERSIVE_DARK_MODE = 19 (Windows 10 build 19041+)
                DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                
                # Önce Windows 11 (20) deneyelim
                value = ctypes.c_int(1)
                result = ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, 
                    DWMWA_USE_IMMERSIVE_DARK_MODE,
                    ctypes.byref(value),
                    ctypes.sizeof(value)
                )
                
                # Başarısız olursa, Windows 10 (19) dene
                if result != 0:
                    DWMWA_USE_IMMERSIVE_DARK_MODE = 19
                    ctypes.windll.dwmapi.DwmSetWindowAttribute(
                        hwnd,
                        DWMWA_USE_IMMERSIVE_DARK_MODE,
                        ctypes.byref(value),
                        ctypes.sizeof(value)
                    )
            except Exception as e:
                print(f"Karanlık başlık çubuğu ayarlanamadı: {e}")
    
    def showEvent(self, event):
        """Pencere gösterildiğinde karanlık başlık çubuğunu etkinleştir"""
        super().showEvent(event)
        self.enable_dark_titlebar()
    
    def create_header(self, layout):
        """Başlık oluştur"""
        header = QtWidgets.QLabel("n8n Kontrol Paneli")
        header.setStyleSheet(styles.HEADER_STYLE)
        header.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(header)
    
    def create_status_indicators(self, layout):
        """Durum göstergelerini oluştur"""
        status_container = QtWidgets.QWidget()
        status_layout = QtWidgets.QHBoxLayout(status_container)
        status_layout.setSpacing(12)
        status_layout.setContentsMargins(0, 0, 0, 0)
        
        self.n8n_status = QtWidgets.QLabel()
        self.cf_status = QtWidgets.QLabel()
        
        status_layout.addWidget(self.n8n_status)
        status_layout.addWidget(self.cf_status)
        layout.addWidget(status_container)
    
    def create_buttons(self, layout):
        """Butonları oluştur"""
        button_container = QtWidgets.QWidget()
        button_layout = QtWidgets.QGridLayout(button_container)
        button_layout.setSpacing(10)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # n8n butonları
        btn_start_n8n = QtWidgets.QPushButton("n8n Başlat")
        btn_start_n8n.setStyleSheet(styles.BUTTON_STYLE_START)
        btn_start_n8n.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_start_n8n.clicked.connect(self.on_start_n8n)
        
        btn_stop_n8n = QtWidgets.QPushButton("n8n Durdur")
        btn_stop_n8n.setStyleSheet(styles.BUTTON_STYLE_STOP)
        btn_stop_n8n.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_stop_n8n.clicked.connect(self.on_stop_n8n)
        
        # Cloudflare butonları
        btn_start_cf = QtWidgets.QPushButton("Cloudflare Başlat")
        btn_start_cf.setStyleSheet(styles.BUTTON_STYLE_START)
        btn_start_cf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_start_cf.clicked.connect(self.on_start_cloudflare)
        
        btn_stop_cf = QtWidgets.QPushButton("Cloudflare Durdur")
        btn_stop_cf.setStyleSheet(styles.BUTTON_STYLE_STOP)
        btn_stop_cf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_stop_cf.clicked.connect(self.on_stop_cloudflare)
        
        # Izgaraya ekle
        button_layout.addWidget(btn_start_n8n, 0, 0)
        button_layout.addWidget(btn_stop_n8n, 0, 1)
        button_layout.addWidget(btn_start_cf, 1, 0)
        button_layout.addWidget(btn_stop_cf, 1, 1)
        
        layout.addWidget(button_container)
    
    def create_emergency_button(self, layout):
        """Acil durdurma butonu oluştur"""
        emergency_container = QtWidgets.QWidget()
        emergency_layout = QtWidgets.QHBoxLayout(emergency_container)
        emergency_layout.setContentsMargins(0, 0, 0, 0)
        emergency_layout.setSpacing(8)
        
        emergency_layout.addStretch()
        
        # Acil durdurma butonu - basit stil
        btn_emergency_kill = QtWidgets.QPushButton("Tüm Node.js'leri Durdur")
        btn_emergency_kill.setStyleSheet(styles.BUTTON_STYLE_EMERGENCY)
        btn_emergency_kill.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_emergency_kill.clicked.connect(self.on_emergency_kill)
        emergency_layout.addWidget(btn_emergency_kill)
        
        emergency_layout.addStretch()
        
        layout.addWidget(emergency_container)
    
    def on_emergency_kill(self):
        """Acil durdurma işlemi"""
        # Onay diyaloğunu göster
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle("Acil Node.js Durdurma")
        msg_box.setText(
            "Tüm Node.js süreçlerini zorla sonlandırmak istiyor musunuz?\n\n"
            "Bu işlem:\n"
            "• Tüm node.exe süreçlerini sonlandıracak\n"
            "• n8n ve diğer Node.js uygulamalarını kapatacak\n"
            "• Kaydedilmemiş veriler kaybolabilir\n\n"
            "NOT: Cloudflare tüneli etkilenmeyecektir.\n\n"
            "Devam etmek istiyor musunuz?"
        )
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
        msg_box.setStyleSheet(styles.MESSAGEBOX_STYLE)
        
        reply = msg_box.exec_()
        
        if reply == QtWidgets.QMessageBox.Yes:
            self.process_manager.emergency_kill_all()
            self.update_status()
    
    def create_log_area(self, layout):
        """Log alanı oluştur"""
        # Log başlığı ve butonları
        log_header_container = QtWidgets.QWidget()
        log_header_layout = QtWidgets.QHBoxLayout(log_header_container)
        log_header_layout.setContentsMargins(0, 0, 0, 0)
        log_header_layout.setSpacing(8)
        
        log_header = QtWidgets.QLabel("Aktivite Günlüğü")
        log_header.setStyleSheet(styles.LOG_HEADER_STYLE)
        log_header_layout.addWidget(log_header)
        
        log_header_layout.addStretch()
        
        # Temizle butonu
        btn_clear_log = QtWidgets.QPushButton("Temizle")
        btn_clear_log.setStyleSheet(styles.BUTTON_STYLE_LOG_UTILITY)
        btn_clear_log.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_clear_log.clicked.connect(self.clear_log)
        log_header_layout.addWidget(btn_clear_log)
        
        # Kaydet butonu
        btn_save_log = QtWidgets.QPushButton("Kaydet")
        btn_save_log.setStyleSheet(styles.BUTTON_STYLE_LOG_UTILITY)
        btn_save_log.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_save_log.clicked.connect(self.save_log)
        log_header_layout.addWidget(btn_save_log)
        
        layout.addWidget(log_header_container)
        
        self.log_text = QtWidgets.QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet(styles.LOG_TEXT_STYLE)
        self.log_text.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.log_text.customContextMenuRequested.connect(self.show_log_context_menu)
        layout.addWidget(self.log_text, 1)  # Genişleme faktörü
    
    def show_log_context_menu(self, position):
        """Log için bağlam menüsünü göster"""
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(styles.MENU_STYLE)
        
        copy_action = menu.addAction("Tümünü Kopyala")
        clear_action = menu.addAction("Günlüğü Temizle")
        menu.addSeparator()
        save_action = menu.addAction("Dosyaya Kaydet...")
        
        action = menu.exec_(self.log_text.mapToGlobal(position))
        
        if action == copy_action:
            self.copy_log()
        elif action == clear_action:
            self.clear_log()
        elif action == save_action:
            self.save_log()
    
    def clear_log(self):
        """Günlüğü temizle"""
        self.log_text.clear()
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] Günlük temizlendi")
    
    def copy_log(self):
        """Günlük içeriğini kopyala"""
        from PyQt5.QtWidgets import QApplication
        QApplication.clipboard().setText(self.log_text.toPlainText())
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] Günlük panoya kopyalandı")
    
    def save_log(self):
        """Günlüğü dosyaya kaydet"""
        from PyQt5.QtWidgets import QFileDialog
        from datetime import datetime
        
        default_name = f"n8n_gunluk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Günlük Dosyasını Kaydet",
            default_name,
            "Metin Dosyaları (*.txt);;Tüm Dosyalar (*.*)"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.log_text.toPlainText())
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.log_text.append(f"[{timestamp}] Günlük kaydedildi: {filename}")
            except Exception as e:
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.log_text.append(f"[{timestamp}] Hata: {str(e)}")
    
    def update_status(self):
        """Durum göstergelerini güncelle"""
        # n8n durumu
        if self.process_manager.is_n8n_running():
            self.n8n_status.setText("n8n: Çalışıyor")
            self.n8n_status.setStyleSheet(styles.STATUS_RUNNING_STYLE)
        else:
            self.n8n_status.setText("n8n: Durduruldu")
            self.n8n_status.setStyleSheet(styles.STATUS_STOPPED_STYLE)
        
        # Cloudflare durumu
        if self.process_manager.is_cloudflare_running():
            self.cf_status.setText("Cloudflare: Çalışıyor")
            self.cf_status.setStyleSheet(styles.STATUS_CF_RUNNING_STYLE)
        else:
            self.cf_status.setText("Cloudflare: Durduruldu")
            self.cf_status.setStyleSheet(styles.STATUS_STOPPED_STYLE)
    
    def show_window(self):
        """Pencereyi göster"""
        self.show()
        self.raise_()
        self.activateWindow()
        self.update_status()
    
    # Buton geri çağırmaları
    def on_start_n8n(self):
        try:
            self.process_manager.start_n8n()
            self.update_status()
        except Exception as e:
            from datetime import datetime
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_text.append(f"[{timestamp}] n8n başlatma hatası: {e}")
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Hata")
            msg.setText(f"n8n başlatılamadı: {e}")
            msg.setStyleSheet(styles.MESSAGEBOX_STYLE)
            msg.exec_()
    
    def on_stop_n8n(self):
        try:
            self.process_manager.stop_n8n()
            self.update_status()
        except Exception as e:
            from datetime import datetime
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_text.append(f"[{timestamp}] n8n durdurma hatası: {e}")
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Hata")
            msg.setText(f"n8n durdurulamadı: {e}")
            msg.setStyleSheet(styles.MESSAGEBOX_STYLE)
            msg.exec_()
    
    def on_start_cloudflare(self):
        try:
            self.process_manager.start_cloudflare()
            self.update_status()
        except Exception as e:
            from datetime import datetime
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_text.append(f"[{timestamp}] Cloudflare başlatma hatası: {e}")
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Hata")
            msg.setText(f"Cloudflare başlatılamadı: {e}")
            msg.setStyleSheet(styles.MESSAGEBOX_STYLE)
            msg.exec_()
    
    def on_stop_cloudflare(self):
        try:
            self.process_manager.stop_cloudflare()
            self.update_status()
        except Exception as e:
            from datetime import datetime
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_text.append(f"[{timestamp}] Cloudflare durdurma hatası: {e}")
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Hata")
            msg.setText(f"Cloudflare durdurulamadı: {e}")
            msg.setStyleSheet(styles.MESSAGEBOX_STYLE)
            msg.exec_()
