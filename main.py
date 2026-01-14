"""
n8n Tray - Ana Uygulama
Sistem tepsisinden n8n ve Cloudflare tünellerini yöneten uygulama.
"""

import os
import sys

def resource_path(relative_path):
    """ Kaynağa mutlak yol al, geliştirme ve PyInstaller için çalışır """
    try:
        # PyInstaller geçici bir klasör oluşturur ve yolu _MEIPASS'ta saklar
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# __pycache__ oluşturulmasını engelle
sys.dont_write_bytecode = True

from PyQt5 import QtWidgets, QtGui, QtCore, QtNetwork

# Kendi modüllerimiz
from process_manager import ProcessManager
from gui import MainWindow
from tray_manager import create_tray


def main():
    """Ana uygulama"""
    
    # Qt Uygulaması
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("n8n-tray")
    
    # Tek Örnek kontrolü - Sadece bir örnek çalışabilir
    server_name = "n8n_tray_single_instance"
    socket = QtNetwork.QLocalSocket()
    socket.connectToServer(server_name)
    
    # Başka bir örnek varsa, ona sinyal gönder ve çık
    if socket.waitForConnected(500):
        # Diğer örneğe mesaj gönder (pencereyi göster)
        socket.write(b"show")
        socket.flush()
        socket.waitForBytesWritten(1000)
        socket.disconnectFromServer()
        sys.exit(0)
    
    # İlk örnek - Sunucu oluştur
    local_server = QtNetwork.QLocalServer()
    local_server.removeServer(server_name)  # Varsa eski sunucuyu temizle
    local_server.listen(server_name)
    
    # Sistem tepsisi desteklenmiyorsa uyar (Opsiyonel ama iyi bir kontrol)
    if not QtWidgets.QSystemTrayIcon.isSystemTrayAvailable():
        QtWidgets.QMessageBox.critical(None, "Hata", "Bu sistemde sistem tepsisi desteklenmiyor.")
        sys.exit(1)

    app.setQuitOnLastWindowClosed(False) # Pencere kapandığında uygulamanın kapanmasını engelle (Tepsi için önemli)
    app.setStyle('Fusion')  # Modern görünüm
    
    # Karanlık Tema Paleti - Modern
    dark_palette = QtGui.QPalette()
    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(30, 30, 30))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(232, 232, 232))
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(37, 37, 37))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(56, 56, 56))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(232, 232, 232))
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(56, 56, 56))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(232, 232, 232))
    app.setPalette(dark_palette)
    
    # İkonu yükle (kaynak yolu ile)
    icon_path = resource_path("icon.ico")
    icon = QtGui.QIcon(icon_path)
    app.setWindowIcon(icon) # Uygulama ikonu
    
    # Süreç yöneticisi örneğini oluştur
    process_manager = ProcessManager()
    
    # Ana pencereyi oluştur
    window = MainWindow(icon, process_manager)
    
    # Süreç yöneticisine GUI referanslarını ver
    process_manager.set_gui_references(
        window.log_text,
        None,  # Tepsi henüz oluşturulmadı
        window.update_status
    )
    
    # Sistem tepsisini oluştur
    tray = create_tray(app, icon, process_manager, window.show_window)
    
    # Süreç yöneticisine tepsi referansını ver
    process_manager.tray = tray
    
    # Diğer örneklerden gelen istekleri dinle
    def on_new_connection():
        client = local_server.nextPendingConnection()
        if client and client.waitForReadyRead(1000):
            message = client.readAll().data()
            if message == b"show":
                # Pencereyi göster
                window.show_window()
    
    local_server.newConnection.connect(on_new_connection)
    
    # Uygulama başlatıldığında pencereyi göster
    window.show_window()
    
    # Uygulamayı başlat
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
