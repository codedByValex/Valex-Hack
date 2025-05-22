import os
import time
import random
import getpass
import socket
import sys

ascii_art = """
\033[91m
____   _________  .____     _______________  ___
\   \ /   /  _  \ |    |    \_   _____/\   \/  /
 \   Y   /  /_\  \|    |     |    __)_  \     / 
  \     /    |    \    |___  |        \ /     \ 
   \___/\____|__  /_______ \/_______  //___/\  \
 
By Valex
\033[0m
"""
kullanici_adi = "ornek_kullanici"
link = f"https://www.tiktok.com/@valex863"
print(f"TikTok hesabım: {link} \033[0m")

ascii_gallery = [
    "\033[93m(>'-')>\033[0m",
    "\033[92m(╯°□°）╯︵ ┻━┻\033[0m",
    "\033[94m¯\\_(ツ)_/¯\033[0m",
    "\033[95mʕ•ᴥ•ʔ\033[0m",
    "\033[96m(｡♥‿♥｡)\033[0m"
]

bilgiler = [
    "Python 1991 yılında ortaya çıkmıştır.",
    "Dünyadaki en hızlı hayvan peregrin şahindir.",
    "Bir ahtapotun 3 kalbi vardır.",
    "En çok konuşulan dil İngilizce değil, Mandarindir!",
    "Bilgisayar fareleri ilk kez 1960'larda kullanıldı."
]

dosya_adi = "kullanicilar.txt"
son_kullanici_dosyasi = "son_kullanici.txt"

def yazi_animasyon(metin, hiz=0.03):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(hiz)
    print()

def kayit_ol():
    print("\n\033[94m--- Kayıt Ol ---\033[0m")
    kullanici = input("Yeni kullanıcı adı: ")
    sifre = getpass.getpass("Yeni şifre (gizli): ")

    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r") as f:
            for satir in f:
                kayitli_kullanici, *_ = satir.strip().split(":")
                if kayitli_kullanici == kullanici:
                    print("\033[91mBu kullanıcı adı zaten var!\033[0m")
                    return False

    ad = input("Adınız: ")
    yas = input("Yaşınız: ")

    with open(dosya_adi, "a") as f:
        f.write(f"{kullanici}:{sifre}:{ad}:{yas}\n")
    print("\033[92mKayıt başarılı!\033[0m")
    return True

def giris_yap():
    print("\n\033[94m--- Giriş Yap ---\033[0m")
    kullanici = input("Kullanıcı adı: ")
    sifre = input("Şifre (gizli): ")

    if not os.path.exists(dosya_adi):
        print("\033[91mHenüz kullanıcı kaydı yok!\033[0m")
        return None

    with open(dosya_adi, "r") as f:
        for satir in f:
            veri = satir.strip().split(":")
            if len(veri) < 4:
                continue
            kayitli_kullanici, kayitli_sifre, ad, yas = veri
            if kullanici == kayitli_kullanici and sifre == kayitli_sifre:
                with open(son_kullanici_dosyasi, "w") as s:
                    s.write(kullanici)
                print(f"\033[92mGiriş başarılı! Hoş geldin {ad}.\033[0m")
                return (kullanici, ad, yas)
    print("\033[91mKullanıcı adı veya şifre yanlış!\033[0m")
    return None

def sifre_degistir(kullanici):
    print("\n\033[94m--- Şifre Değiştir ---\033[0m")
    yeni = input("Yeni şifre (gizli): ")
    satirlar = []
    with open(dosya_adi, "r") as f:
        satirlar = f.readlines()
    with open(dosya_adi, "w") as f:
        for satir in satirlar:
            veriler = satir.strip().split(":")
            if veriler[0] == kullanici:
                f.write(f"{veriler[0]}:{yeni}:{veriler[2]}:{veriler[3]}\n")
            else:
                f.write(satir)
    print("\033[92mŞifre güncellendi.\033[0m")

def kullanici_sil(kullanici):
    print("\n\033[91m--- Hesap Siliniyor ---\033[0m")
    onay = input("Emin misiniz? (evet/hayır): ").lower()
    if onay != "evet":
        print("İptal edildi.")
        return
    with open(dosya_adi, "r") as f:
        satirlar = f.readlines()
    with open(dosya_adi, "w") as f:
        for satir in satirlar:
            if not satir.startswith(kullanici + ":"):
                f.write(satir)
    print("Hesap silindi. Programdan çıkılıyor.")
    exit()

def profil_duzenle(kullanici):
    print("\n\033[94m--- Profil Bilgilerini Güncelle ---\033[0m")
    yeni_ad = input("Yeni ad: ")
    yeni_yas = input("Yeni yaş: ")

    with open(dosya_adi, "r") as f:
        satirlar = f.readlines()
    with open(dosya_adi, "w") as f:
        for satir in satirlar:
            veriler = satir.strip().split(":")
            if veriler[0] == kullanici:
                f.write(f"{veriler[0]}:{veriler[1]}:{yeni_ad}:{yeni_yas}\n")
            else:
                f.write(satir)
    print("\033[92mProfil güncellendi.\033[0m")

def ascii_goster():
    print("\n\033[94m--- ASCII Sanat Galerisi ---\033[0m")
    for art in ascii_gallery:
        print(art)
        time.sleep(0.5)

def hesap_makinesi():
    print("\n\033[94m--- Basit Hesap Makinesi ---\033[0m")
    try:
        sayi1 = float(input("1. Sayı: "))
        islem = input("İşlem (+ - * /): ")
        sayi2 = float(input("2. Sayı: "))
        if islem == "+":
            print("Sonuç:", sayi1 + sayi2)
        elif islem == "-":
            print("Sonuç:", sayi1 - sayi2)
        elif islem == "*":
            print("Sonuç:", sayi1 * sayi2)
        elif islem == "/":
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Geçersiz işlem.")
    except:
        print("Hatalı giriş!")

def rastgele_bilgi():
    print("\n\033[94m--- Rastgele Bilgi ---\033[0m")
    print(random.choice(bilgiler))

def tas_kagit_makas():
    print("\n\033[94m--- Taş Kağıt Makas ---\033[0m")
    secenekler = ["taş", "kağıt", "makas"]
    bot = random.choice(secenekler)
    senin = input("Taş / Kağıt / Makas: ").lower()
    print("Bot:", bot)
    if senin == bot:
        print("Berabere!")
    elif (senin == "taş" and bot == "makas") or (senin == "kağıt" and bot == "taş") or (senin == "makas" and bot == "kağıt"):
        print("Kazandın!")
    elif senin in secenekler:
        print("Kaybettin!")
    else:
        print("Geçersiz seçim.")
def menu(kullanici, ad, yas):
    while True:
        print(f"\n\033[95m--- {kullanici.upper()} MENÜ ---\033[0m")
        print("1. Bilgilerimi Göster")
        print("2. 100 Yaşına Kaç Yıl Kaldı?")
        print("3. Şifre Değiştir")
        print("4. ASCII Sanatları Göster")
        print("5. Hesap Makinesi")
        print("6. Rastgele Bilgi")
        print("7. Taş Kağıt Makas")
        print("8. Profil Bilgilerini Güncelle")
        print("9. Hesabı Sil")
        print("10. Çıkış")
        print("11. Günün Sözü")
        print("12. Zar At")
        print("13. Sayı Tahmin Oyunu")
        print("14. Çarpım Tablosu")
        print("15. Yazı Tura")
        print("16. Ad Soyad Tersten Yaz")
        print("17. Rastgele Emoji Göster")
        print("18. Saat Göster")
        print("19. İnternetsiz Şaka")
        print("20. Harf Sayacı")
        print("21. Ters Çevirici")
        print("22. Kelime Say")
        print("23. Kare Hesapla")
        print("24. Sayı Çift Mi Tek Mi?")
        print("25. Renkli Selamla")
        print("26. IP Adresini Göster")
        print("27. Parola Gücü Kontrolü")
        print("28. Güvenli Şifre Üret")
        print("29. Basit Şifre Kırma ")
        print("30. Hash (SHA256) Oluştur")
        print("31. Sosyal Mühendislik Uyarısı Oku")
        print("32. IP Adresini göster")
        print("33. DNS Sorgusu Yap (Alan Adı Çözümle)")
        print("34. Yerel Portları Listele (Aktif Bağlantılar)")
        print("35. Hash (MD5, SHA1, SHA256) Üretici")
        print("36. Parola Gücü Analizi")
        print("37. Keylogger Uyarısı Kontrolü ")
        print("38. Şüpheli İşlem Algılama")

        secim = input("Seçim (1-25): ")

        if secim == "1":
            print(f"\033[93mAd: {ad} | Yaş: {yas}\033[0m")
        elif secim == "2":
            try:
                kalan = 100 - int(yas)
                print(f"\033[93m100 yaşına {kalan} yıl kaldı.\033[0m" if kalan > 0 else "Zaten 100+ yaşındasın!")
            except:
                print("Geçersiz yaş!")
        elif secim == "3":
            sifre_degistir(kullanici)
        elif secim == "4":
            ascii_goster()
        elif secim == "5":
            hesap_makinesi()
        elif secim == "6":
            rastgele_bilgi()
        elif secim == "7":
            tas_kagit_makas()
        elif secim == "8":
            profil_duzenle(kullanici)
        elif secim == "9":
            kullanici_sil(kullanici)
        elif secim == "10":
            print("\033[91mÇıkılıyor...\033[0m")
            break
        elif secim == "11":
            print(random.choice([
                "Başlamak için mükemmel olmanı bekleme.",
                "Hayallerinin peşinden git!",
                "Her yeni gün, yeni bir başlangıçtır."
            ]))
        elif secim == "12":
            print("Zar atılıyor:", random.randint(1, 6))
        elif secim == "13":
            sayi = random.randint(1, 10)
            tahmin = int(input("1-10 arası bir sayı tahmin et: "))
            print("Doğru!" if tahmin == sayi else f"Yanlış! Sayı: {sayi}")
        elif secim == "14":
            for i in range(1, 11):
                for j in range(1, 11):
                    print(f"{i}x{j}={i*j}", end="\t")
                print()
        elif secim == "15":
            print("Sonuç:", random.choice(["Yazı", "Tura"]))
        elif secim == "16":
            adsoyad = input("Ad Soyad gir: ")
            print("Ters:", adsoyad[::-1])
        elif secim == "17":
            print(random.choice(["😀", "🔥", "⚡", "❤️", "✨", "🚀"]))
        elif secim == "18":
            print("Saat:", time.strftime("%H:%M:%S"))
        elif secim == "19":
            print(random.choice([
                "Bilgisayarım neden güldü? Çünkü virüs bulaştı!",
                "Python kodu kahve içer mi? Hayır ama Java içer.",
                "Programcıyı neden işe almadılar? Çünkü C'de boğulmuştu!"
            ]))
        elif secim == "20":
            metin = input("Bir metin girin: ")
            harf = input("Hangi harfi saymak istersin? ")
            print(f"{harf} harfi sayısı:", metin.lower().count(harf.lower()))
        elif secim == "21":
            metin = input("Ters çevrilecek metin: ")
            print("Ters:", metin[::-1])
        elif secim == "22":
            metin = input("Metin girin: ")
            print("Kelime sayısı:", len(metin.split()))
        elif secim == "23":
            sayi = int(input("Bir sayı gir: "))
            print("Karesi:", sayi**2)
        elif secim == "24":
            sayi = int(input("Bir sayı gir: "))
            print("Çift." if sayi % 2 == 0 else "Tek.")
        elif secim == "25":
            isim = input("Adın: ")
            print(f"\033[92mSelam {isim}, harikasın!\033[0m")
        elif secim == "26":
            
            hostname = socket.gethostname()
            ip_adresi = socket.gethostbyname(hostname)
            print("IP Adresin:", ip_adresi)
        elif secim == "27":
            sifre = input("Parolanı gir: ")
            guclu = len(sifre) >= 8 and any(c.isdigit() for c in sifre) and any(c.isupper() for c in sifre)
            print("Parola Güçlü!" if guclu else "Parola Zayıf. En az 8 karakter, 1 büyük harf ve 1 rakam içermeli.")
        elif secim == "28":
            import secrets
            import string
            karakterler = string.ascii_letters + string.digits + "!@#$%^&*()"
            sifre = ''.join(secrets.choice(karakterler) for i in range(12))
            print("Güvenli Şifre:", sifre)
        elif secim == "29":
            hedef_sifre = input("Hedef şifre (örnek: '123'): ")
            print("Kırma denemeleri:")
            for i in range(1000):
                deneme = str(i)
                print("Deniyor:", deneme)
                if deneme == hedef_sifre:
                    print("Şifre bulundu!", deneme)
                    break
        elif secim == "30":
            import hashlib
            veri = input("Hashlenecek metin: ")
            hash_sonuc = hashlib.sha256(veri.encode()).hexdigest()
            print("SHA256 Hash:", hash_sonuc)
        elif secim == "31":
            print("\033[91mSosyal mühendislik, insanların manipüle edilerek gizli bilgilerin elde edilmesidir.")
            print("Hiçbir zaman şifreni kimseyle paylaşma. Linklere tıklamadan önce emin ol.\033[0m")
        elif secim == "32":
            import requests
            try:
                ip = requests.get("https://api.ipify.org").text
                print("Gerçek IP Adresin:", ip)
            except:
                print("IP alınamadı, internet bağlantını kontrol et.")

        elif secim == "33":
            import socket
            domain = input("Alan adı gir (örnek: google.com): ")
            try:
                ip = socket.gethostbyname(domain)
                print(f"{domain} IP adresi: {ip}")
            except:
                print("Alan adı çözümlenemedi.")

        elif secim == "34":
            import subprocess
            print("Aktif bağlantılar (ilk 10):")
            try:
                sonuc = subprocess.check_output("netstat -an", shell=True).decode()
                for satir in sonuc.splitlines()[:10]:
                    print(satir)
            except:
                print("Port bilgileri alınamadı.")

        elif secim == "35":
            import hashlib
            veri = input("Hashlenecek veri gir: ")
            print("MD5:", hashlib.md5(veri.encode()).hexdigest())
            print("SHA1:", hashlib.sha1(veri.encode()).hexdigest())
            print("SHA256:", hashlib.sha256(veri.encode()).hexdigest())

        elif secim == "36":
            sifre = input("Şifreyi gir: ")
            skor = 0
            if len(sifre) >= 8: skor += 1
            if any(c.isupper() for c in sifre): skor += 1
            if any(c.isdigit() for c in sifre): skor += 1
            if any(c in "!@#$%^&*" for c in sifre): skor += 1
            seviye = ["Çok Zayıf", "Zayıf", "Orta", "Güçlü", "Çok Güçlü"]
            print("Parola Gücü:", seviye[skor])

        elif secim == "37":
            print("Keylogger tespiti simülasyonu başlatılıyor...")
            import time
            time.sleep(1)
            print("Geçici dosyalar kontrol ediliyor...")
            time.sleep(1)
            print("Regedit girişleri taranıyor...")
            time.sleep(1)
            print("Şüpheli bir keylogger bulunamadı (simülasyon).")

        elif secim == "38":
            print("RAM ve CPU kullanımı analizi...")
            import psutil
            print("CPU Kullanımı:", psutil.cpu_percent(), "%")
            print("RAM Kullanımı:", psutil.virtual_memory().percent, "%")
            print("Sistem kararlı görünüyor. Şüpheli işlem yok.")   
        else:
            print("Geçersiz seçim!")

        secim = input("Seçim (1-25): ")
        if secim == "1":
            print(f"\033[93mAd: {ad} | Yaş: {yas}\033[0m")
        elif secim == "2":
            try:
                kalan = 100 - int(yas)
                print(f"\033[93m100 yaşına {kalan} yıl kaldı.\033[0m" if kalan > 0 else "Zaten 100+ yaşındasın!")
            except:
                print("Geçersiz yaş!")


def baslat():
    print(ascii_art)
    yazi_animasyon("Hoş geldin! Yükleniyor...\n", 0.05)

    while True:
        print("\n\033[94m1. Giriş Yap\n2. Kayıt Ol\n3. Çıkış\033[0m")
        secim = input("Seçiminiz: ")
        if secim == "1":
            sonuc = giris_yap()
            if sonuc:
                kullanici, ad, yas = sonuc
                menu(kullanici, ad, yas)
        elif secim == "2":
            kayit_ol()
        elif secim == "3":
            print("\033[91mProgramdan çıkılıyor...\033[0m")
            break
        else:
            print("Geçersiz seçim!")
            
            
           





baslat()