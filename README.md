# steganografi-araci
Python ve LSB algoritması kullanarak resim piksellerine gizli metin mesajları saklayan ve çözen Steganografi (Veri Gizleme) aracı.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Library](https://img.shields.io/badge/Library-Pillow-green) ![Status](https://img.shields.io/badge/Status-Active-orange)

Bu proje, **LSB (Least Significant Bit)** algoritmasını kullanarak resim dosyalarının (piksel verilerinin) içine gizli metin mesajları saklayan ve şifreli resimlerden bu mesajları okuyan bir Python aracıdır.

##  Özellikler

* **LSB Algoritması:** Piksellerin renk kodlarının en son bitini değiştirerek veriyi insan gözünün göremeyeceği şekilde gizler.
* **Auto-Fix (Türkçe Karakter Desteği):** Standart ASCII dışındaki karakterlerin (ı, ş, ğ, vb.) bit kaymasına sebep olmasını önlemek için otomatik düzeltme algoritması içerir.
* **Format Koruması:** Veri kaybını önlemek için çıktıları otomatik olarak kayıpsız **PNG** formatına dönüştürür.
* **Akıllı Çözücü:** Mesajın bittiği yeri özel bir işaretleyici (`#####`) ile tespit eder ve gereksiz tarama yapmaz.

## 🛠️ Kurulum

Projeyi bilgisayarınıza klonlayın ve gerekli kütüphaneyi indirin:

bash
git clone [https://github.com/alirizagocerr/steganografi-araci.git]
cd steganografi-araci
pip install pillow


Kurulum yapıldıktan sonra kod ile mesajı eklemek istediğiniz aracı aynı klasörün içine ekleyip python steganografi.py kodunu yazmanız gerekmektedir ve terminalde seçimler yapacaksınız

 ## Uyarı
 
 İnternetteki diğer gizlenmiş fotoğrafları çözmek yerine bu araç ile oluşturduğunuz fotoğrafları çözer çünkü çözüm algoritması diğer gördüğünüz fotoğrafların içine mesajı gizleme algoritmasıyla aynı olmayabiliceğinden dolayı kesin çözebilicek bir
 değildir.
