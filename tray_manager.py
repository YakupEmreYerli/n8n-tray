"""
n8n Tray - Sistem Tepsisi Yönetimi
Bu modül sistem tepsisi simgesini ve menüsünü yönetir.
"""

from PyQt5 import QtWidgets, QtGui


def create_tray(app, icon, process_manager, show_window_callback):
    """Sistem tepsisi simgesi ve menüsünü oluştur"""
    
    tray = QtWidgets.QSystemTrayIcon(icon, parent=app)
    tray.setToolTip("n8n Kontrol Paneli")
    
    menu = QtWidgets.QMenu()
    menu.addAction("Çağır", show_window_callback)
    menu.addSeparator()
    menu.addAction("n8n Başlat", process_manager.start_n8n)
    menu.addAction("n8n Durdur", process_manager.stop_n8n)
    menu.addSeparator()
    menu.addAction("Cloudflare Başlat", process_manager.start_cloudflare)
    menu.addAction("Cloudflare Durdur", process_manager.stop_cloudflare)
    menu.addSeparator()
    emergency_action = menu.addAction("Tüm Node.js'leri Durdur", process_manager.emergency_kill_all)
    menu.addSeparator()
    menu.addAction("Çıkış", app.quit)
    
    tray.setContextMenu(menu)
    tray.activated.connect(
        lambda reason: show_window_callback() if reason == QtWidgets.QSystemTrayIcon.DoubleClick else None
    )
    
    tray.show()
    return tray
