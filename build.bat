@echo off
echo ========================================
echo n8n-Tray Derleme Scripti
echo ========================================
echo.

REM Eski build ve dist klasorlerini temizle
echo [1/3] Eski build dosyalari temizleniyor...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo Temizlendi!
echo.

REM PyInstaller ile exe olustur
echo [2/3] PyInstaller ile exe olusturuluyor...
pyinstaller n8n-Tray.spec
if %errorlevel% neq 0 (
    echo.
    echo HATA: PyInstaller basarisiz oldu!
    pause
    exit /b 1
)
echo Exe olusturuldu!
echo.

REM Exe dosyasinin varligini kontrol et
if not exist "dist\n8n-Tray.exe" (
    echo.
    echo HATA: Exe dosyasi olusturulamadi!
    pause
    exit /b 1
)

echo [3/3] Tamamlandi!
echo ========================================
echo.
echo Exe dosyasi: dist\n8n-Tray.exe
echo.
echo ========================================
pause
