"""
n8n Tray - Stil Tanımlamaları
Bu modül tüm CSS stillerini ve renk paletini içerir.
"""

# Renk Paleti - Modern & Sade (#121212 Bazlı)
COLORS = {
    'bg_primary': '#121212',
    'bg_secondary': '#1a1a1a',
    'bg_card': '#1f1f1f',
    'border': '#2a2a2a',
    'text_primary': '#e8e8e8',
    'text_secondary': '#a8a8a8',
    'accent_green': '#2e6f40',
    'accent_red': '#fa003f',
}

# Ana Pencere Stili
WINDOW_STYLE = """
    QWidget {
        background-color: #121212;
        color: #e8e8e8;
        font-family: 'Segoe UI', -apple-system, system-ui, sans-serif;
    }
"""

# Header Stili - Modern
HEADER_STYLE = """
    font-size: 18px;
    font-weight: 600;
    color: #e8e8e8;
    padding: 12px 0;
    border-bottom: 1px solid #1f1f1f;
    letter-spacing: -0.3px;
"""

# Status Indicator - Çalışıyor (Yeşil) - Modern Card
STATUS_RUNNING_STYLE = """
    color: #2e6f40;
    font-size: 13px;
    font-weight: 500;
    padding: 10px 14px;
    background: #1a1a1a;
    border: 1px solid #2e6f40;
    border-radius: 6px;
"""

# Status Indicator - Kapalı (Kırmızı) - Modern Card
STATUS_STOPPED_STYLE = """
    color: #fa003f;
    font-size: 13px;
    font-weight: 500;
    padding: 10px 14px;
    background: #1a1a1a;
    border: 1px solid #fa003f;
    border-radius: 6px;
"""

# Status Indicator - Cloudflare Çalışıyor
STATUS_CF_RUNNING_STYLE = STATUS_RUNNING_STYLE

# Buton Stili - Modern Minimal
BUTTON_STYLE_START = """
    QPushButton {
        background: #1f1f1f;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
        padding: 10px 16px;
        font-size: 13px;
        font-weight: 500;
        min-height: 34px;
    }
    QPushButton:hover {
        background: #252525;
        border: 1px solid #333333;
    }
    QPushButton:pressed {
        background: #1a1a1a;
    }
"""

BUTTON_STYLE_STOP = BUTTON_STYLE_START

# Log Header Stili
LOG_HEADER_STYLE = """
    font-size: 13px;
    font-weight: 600;
    color: #a8a8a8;
    padding: 6px 0;
    letter-spacing: -0.2px;
"""

# Log Text Area Stili - Modern
LOG_TEXT_STYLE = """
    QTextEdit {
        background-color: #181818;
        color: #d4d4d4;
        border: 1px solid #222222;
        border-radius: 6px;
        padding: 10px;
        font-family: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
        font-size: 11px;
        line-height: 1.6;
    }
    QScrollBar:vertical {
        background: #181818;
        width: 12px;
        border-radius: 6px;
    }
    QScrollBar::handle:vertical {
        background: #2a2a2a;
        border-radius: 6px;
        min-height: 30px;
    }
    QScrollBar::handle:vertical:hover {
        background: #333333;
    }
"""

# Emergency Kill Button Stili
BUTTON_STYLE_EMERGENCY = """
    QPushButton {
        background: #1f1f1f;
        color: #b0b0b0;
        border: 1px solid #2a2a2a;
        border-radius: 4px;
        padding: 6px 14px;
        font-size: 11px;
    }
    QPushButton:hover {
        background: #252525;
        border: 1px solid #333333;
    }
    QPushButton:pressed {
        background: #181818;
    }
"""

# Log Utility Button Stili (Clear, Save vb.)
BUTTON_STYLE_LOG_UTILITY = """
    QPushButton {
        background: #1f1f1f;
        color: #b0b0b0;
        border: 1px solid #2a2a2a;
        border-radius: 3px;
        padding: 4px 12px;
        font-size: 11px;
    }
    QPushButton:hover {
        background: #252525;
    }
"""

# QMessageBox (Dialog) Stili - Modern Dark Theme
MESSAGEBOX_STYLE = """
    QMessageBox {
        background-color: #121212;
        color: #e8e8e8;
        font-family: 'Segoe UI', -apple-system, system-ui, sans-serif;
    }
    QMessageBox QLabel {
        color: #e8e8e8;
        background-color: transparent;
        font-size: 13px;
    }
    QMessageBox QPushButton {
        background: #1f1f1f;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 4px;
        padding: 6px 20px;
        font-size: 12px;
        font-weight: 500;
        min-width: 70px;
        min-height: 24px;
    }
    QMessageBox QPushButton:hover {
        background: #252525;
        border: 1px solid #333333;
    }
    QMessageBox QPushButton:pressed {
        background: #1a1a1a;
    }
    QMessageBox QPushButton:default {
        background: #1f1f1f;
        border: 1px solid #2e6f40;
    }
    QMessageBox QPushButton:default:hover {
        background: #252525;
        border: 1px solid #2e6f40;
    }
"""

# QMenu (Context Menu) Stili - Modern Dark Theme
MENU_STYLE = """
    QMenu {
        background-color: #1a1a1a;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
        padding: 4px;
        font-size: 12px;
    }
    QMenu::item {
        background-color: transparent;
        padding: 6px 24px 6px 12px;
        border-radius: 3px;
    }
    QMenu::item:selected {
        background-color: #252525;
    }
    QMenu::item:disabled {
        color: #666666;
    }
    QMenu::separator {
        height: 1px;
        background: #2a2a2a;
        margin: 4px 8px;
    }
"""

# QFileDialog Stili - Modern Dark Theme
FILEDIALOG_STYLE = """
    QFileDialog {
        background-color: #121212;
        color: #e8e8e8;
    }
    QFileDialog QLabel {
        color: #e8e8e8;
    }
    QFileDialog QPushButton {
        background: #1f1f1f;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 4px;
        padding: 6px 16px;
        font-size: 12px;
    }
    QFileDialog QPushButton:hover {
        background: #252525;
    }
    QFileDialog QTreeView, QFileDialog QListView {
        background-color: #181818;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 4px;
    }
    QFileDialog QLineEdit {
        background-color: #1f1f1f;
        color: #e8e8e8;
        border: 1px solid #2a2a2a;
        border-radius: 4px;
        padding: 4px 8px;
    }
"""

