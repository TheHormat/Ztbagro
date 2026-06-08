# Deployment Guide — DigitalOcean Droplet

## Gereksinimler
- Ubuntu 22.04 Droplet (minimum 1GB RAM önerilir, 2GB ideal)
- Domain DNS'i Droplet IP'ye yönlendirilmiş olmalı (ztbagro.az → Droplet IP)

---

## 1. Droplet'e bağlan

```bash
ssh root@DROPLET_IP
```

---

## 2. Docker ve Docker Compose kur

```bash
curl -fsSL https://get.docker.com | sh
apt install docker-compose -y

# Docker'ın çalıştığını doğrula
docker --version
docker-compose --version
```

---

## 3. Proje dosyalarını yükle

### Seçenek A — SCP ile local'den yükle (önerilen, git yoksa)

Local bilgisayarda proje klasöründe bu komutu çalıştır:

```powershell
scp -r . root@DROPLET_IP:/opt/teserrufat
```

### Seçenek B — Git ile çek

```bash
git clone <repo-url> /opt/teserrufat
```

---

## 4. Proje klasörüne gir

```bash
cd /opt/teserrufat
```

---

## 5. .env dosyasını oluştur

`.env` dosyası git'te yok, elle oluşturman gerekiyor:

```bash
nano .env
```

İçine şunları yapıştır (şifreyi değiştirmek istersen burada değiştir):

```
DEBUG=False
SECRET_KEY=Ts3rr-Pr0d-S3cr3t-K3y-2024-ZtbAgr0-Secure!#

POSTGRES_DB=teserrufat_db
POSTGRES_USER=teserrufat_user
POSTGRES_PASSWORD=Ztb_Agro_PgSQL_2024#Secure!
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Kaydet: `Ctrl+X` → `Y` → `Enter`

---

## 6. Container'ları başlat

```bash
docker-compose up -d --build
```

Build ve migrate otomatik çalışır. Logları izlemek için:

```bash
docker-compose logs -f web
```

Şunu görürsen hazır demektir:
```
PostgreSQL is ready.
Running migrations...
Collecting static files...
spawned uWSGI master process
```

---

## 7. Superuser oluştur

```bash
docker-compose exec web /venv/bin/python manage.py createsuperuser
```

Kullanıcı adı, email ve şifre gir.

---

## 8. Admin panelden site içeriğini doldur

`http://DROPLET_IP:8000/akm1n/` adresine git ve login ol.

Sırayla şu kayıtları oluştur (anasayfa 500 vermemesi için zorunlu):

1. **Index Config** → header logo, footer logo, favicon yükle
2. **Index Slider** → en az 1 slider görseli ekle
3. **Title Description** → sayfalar için başlık/açıklamalar

---

## 9. Domain ile erişim (ztbagro.az)

Site şu an `http://DROPLET_IP:8000` adresinde çalışıyor.
`ztbagro.az` üzerinden erişim için nginx kurulumu gerekiyor.

### Nginx kur

```bash
apt install nginx -y
```

### Nginx config oluştur

```bash
nano /etc/nginx/sites-available/ztbagro
```

İçerik:

```nginx
server {
    listen 80;
    server_name ztbagro.az www.ztbagro.az;

    client_max_body_size 50M;

    location /static/ {
        alias /opt/teserrufat/static/;
    }

    location /media/ {
        alias /opt/teserrufat/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 300;
    }
}
```

Kaydet ve aktive et:

```bash
ln -s /etc/nginx/sites-available/ztbagro /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

Artık `http://ztbagro.az` çalışır.

---

## 10. SSL (HTTPS) — Let's Encrypt

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d ztbagro.az -d www.ztbagro.az
```

Email gir, şartları kabul et. Certbot nginx config'i otomatik günceller.
Sertifika 90 günde bir otomatik yenilenir.

---

## Yararlı Komutlar

```bash
# Container durumlarını gör
docker-compose ps

# Logları izle
docker-compose logs -f web
docker-compose logs -f db

# Web container'ı yeniden başlat (kod değişikliği sonrası)
docker-compose restart web

# Tamamen durdur
docker-compose down

# Durdur + volume sil (DB sıfırlanır — dikkatli!)
docker-compose down -v

# Django management komutları
docker-compose exec web /venv/bin/python manage.py migrate
docker-compose exec web /venv/bin/python manage.py collectstatic --no-input
docker-compose exec web /venv/bin/python manage.py createsuperuser
```

---

## Güncelleme (kod değişikliği sonrası)

```bash
cd /opt/teserrufat

# Yeni dosyaları çek (git kullanıyorsan)
git pull

# Veya SCP ile tekrar yükle (git yoksa)
# local'de: scp -r . root@DROPLET_IP:/opt/teserrufat

# Container'ı yeniden başlat
docker-compose restart web
```

Migration içeren güncelleme varsa:

```bash
docker-compose exec web /venv/bin/python manage.py migrate
```
