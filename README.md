# n8n Tray Kontrol Paneli

Bu uygulama, Windows Sistem Tepsisinden (Bildirim Alanı) n8n ve Cloudflare tünelini yönetmenizi sağlayan bir masaüstü aracıdır.

## Özellikler

- **n8n Yönetimi**: n8n'i başlatın ve durdurun.
- **Cloudflare Tünel Yönetimi**: Cloudflare tünelini başlatın ve durdurun.
- **Sistem Tepsisi Entegrasyonu**: Arka planda çalışırken uygulamayı sistem tepsisinden kontrol edin.
- **Şık Arayüz**: Modern karanlık mod arayüzü.
- **Süreç İzleme**: Çalışan süreçlerin loglarını görüntüleyin.
- **Acil Durdurma**: Takılı kalan Node.js süreçlerini tek tıkla temizleyin.

## Gereksinimler

- Python 3.x
- `n8n` (Sistem PATH'ine eklenmiş olmalı)
- Cloudflare `cloudflared` (Varsayılan olarak `C:\Cloudflare\cloudflared.exe` konumunda beklenir)

## Kurulum

1. Depoyu klonlayın veya indirin:
```bash
git clone https://github.com/kullaniciadi/n8n-tray.git
cd n8n-tray
```

2. Gerekli Python kütüphanelerini yükleyin:
```bash
pip install -r requirements.txt
```

## Yapılandırma

### Cloudflare Tünel Yapılandırması

Uygulama, Cloudflare tüneli için `C:\Cloudflare\` dizininde aşağıdaki dosyaları arar:
- `C:\Cloudflare\cloudflared.exe` - Cloudflare tünel çalıştırılabilir dosyası
- `C:\Cloudflare\config.yml` - Tünel yapılandırma dosyası

**Önemli:** 
- Her iki dosya da `C:\Cloudflare\` dizininde olmalıdır. 
- Farklı bir konum kullanmak isterseniz, `process_manager.py` dosyasındaki ilgili satırları düzenlemeniz gerekir.
- **Cloudflare Tunnel ID'nizi değiştirmeyi unutmayın!** `process_manager.py` dosyasının 168. satırındaki tunnel ID'yi kendi tunnel ID'niz ile değiştirin.

## Çalıştırma

Uygulamayı başlatmak için:

```bash
python main.py
```

## Dosyalar

- `main.py`: Ana giriş noktası.
- `gui.py`: Grafiksel arayüz kodu.
- `process_manager.py`: Arka plan süreç yönetimi.
- `tray_manager.py`: Sistem tepsisi simgesi yönetimi.
- `styles.py`: Arayüz stilleri.
- `icon.ico`: Uygulama simgesi.

## EXE Dosyası Oluşturma

Uygulamayı tek bir çalıştırılabilir EXE dosyası olarak derlemek için:

### Gereksinimler
- PyInstaller kurulu olmalı: `pip install pyinstaller`

### Build

EXE dosyası oluşturmak için:
```bash
.\build.bat
```

Bu script otomatik olarak:
1. Eski build dosyalarını temizler
2. PyInstaller ile EXE derler (ikon dahil)

**Sonuç:**
- EXE dosyası: `dist/n8n-Tray.exe`

### Özellikler
- Tek dosya olarak çalışır, kurulum gerektirmez
- Uygulama ikonu dahildir
- Sistem tepsisinde düzgün görünür

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun
