from PIL import Image
import os

# --- TÜRKÇE KARAKTER DÜZELTİCİ ---
def turkce_duzelt(metin):
    degisimler = {
        'ı': 'i', 'İ': 'I', 'ş': 's', 'Ş': 'S', 
        'ğ': 'g', 'Ğ': 'G', 'ü': 'u', 'Ü': 'U', 
        'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C'
    }
    for tr, eng in degisimler.items():
        metin = metin.replace(tr, eng)
    return metin

def binary_cevir(mesaj):
    # Artık garanti 8 bitlik (ASCII) veri üretiyoruz
    return ''.join(format(ord(i), '08b') for i in mesaj)

def gizle(resim_adi, mesaj, yeni_isim):
    try:
        img = Image.open(resim_adi)
    except:
        print(f"❌ HATA: '{resim_adi}' dosyası açılamadı.")
        return

    img = img.convert('RGB')
    
    if not yeni_isim.endswith(".png"):
        yeni_isim += ".png"

    data = img.load()
    
    # MESAJI OTOMATİK DÜZELTİYORUZ
    mesaj = turkce_duzelt(mesaj)
    
    mesaj += "#####" 
    binary_mesaj = binary_cevir(mesaj)
    uzunluk = len(binary_mesaj)
    
    index = 0
    width, height = img.size
    
    if uzunluk > width * height:
        print("❌ HATA: Mesaj çok uzun, daha büyük resim kullan!")
        return

    print("⏳ Pikseller bükülüyor...")
    
    try:
        for y in range(height):
            for x in range(width):
                if index < uzunluk:
                    r, g, b = data[x, y]
                    r = (r & ~1) | int(binary_mesaj[index])
                    data[x, y] = (r, g, b)
                    index += 1
                else:
                    break
        
        img.save(yeni_isim)
        print(f"✅ BAŞARILI! Mesaj '{yeni_isim}' dosyasına gizlendi.")
        
    except Exception as e:
        print(f"❌ Hata: {e}")

def coz(resim_adi):
    try:
        img = Image.open(resim_adi)
    except:
        print(f"❌ HATA: '{resim_adi}' bulunamadı.")
        return

    img = img.convert('RGB')
    data = img.load()
    width, height = img.size
    
    binary_veri = ""
    print("🔓 Şifre taranıyor...")
    
    tum_yazi = ""
    
    try:
        for y in range(height):
            for x in range(width):
                r, g, b = data[x, y]
                binary_veri += str(r & 1)
                
                if len(binary_veri) >= 8:
                    byte = binary_veri[:8]
                    binary_veri = binary_veri[8:]
                    
                    karakter_kodu = int(byte, 2)
                    
                    # ASCII sınırları dışındaysa (Gürültü) atla
                    if karakter_kodu > 127: 
                        continue
                        
                    char = chr(karakter_kodu)
                    tum_yazi += char
                    
                    if tum_yazi.endswith("#####"):
                        print("\n" + "="*40)
                        print(f"🕵️ GİZLİ MESAJ: {tum_yazi[:-5]}")
                        print("="*40 + "\n")
                        return
    except Exception as e:
        print(f"Hata: {e}")
    
    print("❌ HATA: Gizli mesaj bulunamadı.")

# --- ANA PROGRAM ---
print("\n--- 🕵️ MAVİ EKRAN BÜKÜCÜ v3.0 (Auto-Fix) ---")

while True:
    secim = input("\n1- Gizle\n2- Oku\n3- Çıkış\nSeçiminiz: ")

    if secim == '1':
        kaynak = input("Resim adı (Örn: kedi.jpg): ")
        if os.path.exists(kaynak):
            mesaj = input("Mesajı Yaz: ")
            hedef = input("Yeni dosya adı: ")
            gizle(kaynak, mesaj, hedef)
        else:
            print("❌ Dosya yok!")

    elif secim == '2':
        hedef = input("Çözülecek dosya (Örn: secretcat.png): ")
        coz(hedef)
    
    elif secim == '3':
        print("Görüşürüz Bükücü! 👋")
        break