#BTK PYTHON NOTLARIM#
# Ekrana yazdırma
print("Merhaba")

# Kullanıcıdan girdi alma
isim = input("Adınız: ")
print("Merhaba", isim)

#Değişkenler ve Veri Tipleri#
#Değişken tanımlama
isim = "Ece"
yas = 23
boy = 1.90
ogrenci_mi = True

#String (Metin)
isim = "Mehmet"
soyisim = 'Yılmaz'
tam_isim = isim + " " + soyisim  # Mehmet Yılmaz

#Integer (Tam Sayı)
sayi = 42
negatif = -20

#Float (Ondalıklı Sayı)
pi = 3.14
sicaklik = 34.6

#Boolean (Mantıksal)
dogru = True
yanlis = False

#Tip Dönüşümleri#
# String'den int'e
sayi = int("42")        # 42

# Int'den string'e
metin = str(42)         # "42"

# Float'tan int'e
tam = int(3.7)          # 3

# String'den float'a
ondalik = float("3.14") # 3.14

#Veri Tipini Öğrenme# => type komutu kullanılır
type(42)        # <class 'int'>
type("merhaba") # <class 'str'>
type(3.14)      # <class 'float'>
type(True)      # <class 'bool'>


#Listeler#
# Boş liste
bos_liste = []

# Sayı listesi
sayilar = [1, 2, 3, 4, 5]

# String listesi
isimler = ["Ahmet", "Buğra", "Ece"]

# Karışık tipli liste
karisik = [1, "beş", 3.0, True]

#Liste Elemanlarına Erişim#
meyveler = ["karpuz", "ananas", "muz", "çilek"]

#İndeks ile erişim (0'dan başlar)
print(meyveler[0])   # karpuz
print(meyveler[2])   # muz

#Negatif indeks (sondan başlar)
print(meyveler[-1])  # çilek
print(meyveler[-2])  # muz

#Liste Dilimleme (Slicing)
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#liste[başlangıç:bitiş:adım]
print(sayilar[2:5])      # [2, 3, 4](2'den 5'e yazdırır)
print(sayilar[:5])       # [0, 1, 2, 3, 4] (5'ten öncekiler)
print(sayilar[5:])       # [5, 6, 7, 8, 9](5 ve sonrakiler)
print(sayilar[::2])      # [0, 2, 4, 6, 8](2şer saydırır)
print(sayilar[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0](sondan başa tek tek yazdırır)


#String Metotları#

#upper() - Büyük harfe çevirir
kelime = "python"
print(kelime.upper())  # PYTHON

#lower() - Küçük harfe çevirir
kelime = "PYTHON"
print(kelime.lower())  # python

#capitalize() - İlk harfi büyük yapar
kelime = "python"
print(kelime.capitalize())  # Python

#title() - Her kelimenin ilk harfini büyük yapar
cumle = "python programlama dili"
print(cumle.title())  # Python Programlama Dili

#strip() - Baştaki ve sondaki boşlukları temizler
metin = "  merhaba  "
print(metin.strip())  # "merhaba"

#replace() - Değiştirir
metin = "Python güzel"
yeni_metin = metin.replace("güzel", "harika")
print(yeni_metin)  # Python harika

#split() - Ayırır (liste döndürür)
cumle = "Python programlama dili"
kelimeler = cumle.split()
print(kelimeler)  # ["Python", "programlama", "dili"]

#join() - Birleştirir
kelimeler = ["Python", "programlama", "dili"]
cumle = " ".join(kelimeler)
print(cumle)  # Python programlama dili

#find() - Bulur (indeks döndürür)
metin = "Python programlama"
indeks = metin.find("pro")
print(indeks)  # 7

#count() - Sayar
metin = "merhaba dünya merhaba"
adet = metin.count("merhaba")
print(adet)  # 2

#startswith() - ... ile başlıyor mu diye bakmak için
kelime = "Python"
print(kelime.startswith("Py"))  # True

#endswith() - ... ile bitiyor mu diye bakmak için
kelime = "Python"
print(kelime.endswith("on"))  # True

#String Formatlama#

#f-string
isim = "Gül"
yas = 23
print(f"Benim adım {isim} ve {yas} yaşındayım")

#format() metodu
print("Benim adım {} ve {} yaşındayım".format("Gül", 23))

#% operatörü 
print("Benim adım %s ve %d yaşındayım" % ("Gül", 23))

#String Kontrolleri#
# isalpha() - Sadece harf olup olmadığı kontrol edilir
print("Python".isalpha())   # True
print("Python3".isalpha())  # False

# isdigit() - Sadece rakam olup olmadığı kontrol edilir
print("123".isdigit())      # True
print("12a".isdigit())      # False

# isalnum() - Harf veya rakam mı kontrolü için kullanılır
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False

# isspace() - Sadece boşluk mu bulundurur kontrolü için
print("   ".isspace())      # True
print(" a ".isspace())      # False

#String Örnekleri#
# Örnek 1: Palindrome kontrolü
def palindrome_mi(kelime):
    return kelime == kelime[::-1]

print(palindrome_mi("aba"))   # True
print(palindrome_mi("merhaba"))  # False

# Örnek 2: Sesli harf sayısı
def sesli_harf_sayisi(metin):
    sesli_harfler = "aeıioöuü"
    sayac = 0
    for harf in metin.lower():
        if harf in sesli_harfler:
            sayac += 1
    return sayac

print(sesli_harf_sayisi("Merhaba"))  # 3

# Örnek 3: Kelimeleri ters çevir
def kelimeleri_ters_cevir(cumle):
    kelimeler = cumle.split()
    ters_kelimeler = []
    for kelime in kelimeler:
        ters_kelimeler.append(kelime[::-1])
    return " ".join(ters_kelimeler)

print(kelimeleri_ters_cevir("Python programlama"))
# nohtyP amalmagorp

# Örnek 4: String uzunluğu (len kullanmadan)
def string_uzunlugu(metin):
    sayac = 0
    for harf in metin:
        sayac += 1
    return sayac

print(string_uzunlugu("Python"))  # 6


#Liste Metotları#

#append() -> Sona eleman ekle
liste = [1, 2, 3]
liste.append(4)
print(liste)  # [1, 2, 3, 4]

#insert() -> Belirli konuma ekle
liste = [1, 2, 4]
liste.insert(2, 3)  # 2. indekse 3'ü ekle
print(liste)  # [1, 2, 3, 4]

#remove() -> Değere göre sil
liste = [1, 2, 3, 4]
liste.remove(3)
print(liste)  # [1, 2, 4]

#pop() -> İndekse göre sil ve döndür
liste = [1, 2, 3, 4]
eleman = liste.pop(2)  # 2. indeksteki elemanı sil
print(eleman)  # 3
print(liste)   # [1, 2, 4]

#extend() -> Listeyi başka liste ile birleştir
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste1.extend(liste2)
print(liste1)  # [1, 2, 3, 4, 5, 6]

#sort() -> Listeyi sırala
#Küçükten büyüğe
sayilar = [3, 1, 4, 1, 5, 9]
sayilar.sort()
print(sayilar)  # [1, 1, 3, 4, 5, 9]

#Büyükten küçüğe
sayilar.sort(reverse=True)
print(sayilar)  # [9, 5, 4, 3, 1, 1]

#reverse() -> Listeyi ters çevir
liste = [1, 2, 3, 4]
liste.reverse()
print(liste)  # [4, 3, 2, 1]

#Liste İşlemleri#

#Uzunluk - len()
liste = [1, 2, 3, 4, 5]
print(len(liste))  # 5

#Toplam - sum()
sayilar = [1, 2, 3, 4, 5]
print(sum(sayilar))  # 15

#Maksimum - max()
sayilar = [3, 7, 2, 9, 1]
print(max(sayilar))  # 9

#Minimum - min()
sayilar = [3, 7, 2, 9, 1]
print(min(sayilar))  # 1

#Eleman varlığı - in
meyveler = ["elma", "armut", "muz"]
print("elma" in meyveler)     # True
print("çilek" in meyveler)    # False

#Liste Örnekleri#
# Örnek 1: Listedeki çift sayıları bulma
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []

for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print(cift_sayilar)  # [2, 4, 6, 8, 10]

# Örnek 2: Listedeki elemanları 2 ile çarp
sayilar = [1, 2, 3, 4, 5]
iki_katlar = []

for sayi in sayilar:
    iki_katlar.append(sayi * 2)

print(iki_katlar)  # [2, 4, 6, 8, 10]

# Örnek 3: Liste elemanlarının toplamı
def liste_toplam(liste):
    toplam = 0
    for eleman in liste:
        toplam += eleman
    return toplam

print(liste_toplam([1, 2, 3, 4, 5]))  # 15

# Örnek 4: Ortanca değer bulma
def ortanca_deger(liste):
    indeks = len(liste) // 2
    return liste[indeks]

print(ortanca_deger([3, 42, 2, 14, 32]))  # 2


#Aritmetik Operatörler#
# Toplama
5 + 3       # 8

# Çıkarma
5 - 3       # 2

# Çarpma
5 * 3       # 15

# Bölme
10 / 3      # 3.333

# Tam Bölme (ondalık kısmı atar)
10 // 3     # 3

# Mod (Kalan)
10 % 3      # 1

# Üs Alma
2 ** 3      # 8 (2 üzeri 3)

#Karşılaştırma Operatörleri#
5 == 5      # True (eşit)
5 != 3      # True (eşit değil)
5 > 3       # True (büyük)
5 < 3       # False (küçük)
5 >= 5      # True (eşittir veya büyüktür)
5 <= 3      # False (küçüktür veya eşittir)

#Mantıksal Operatörler#
# and (ve) -> Her ikisi de True olmalı
True and True   # True
True and False  # False

# or (veya) -> En az biri True olmalı
True or False   # True
False or False  # False

# not (değil) -> Tersini alır
not True        # False
not False       # True

#Atama Operatörleri#
x = 5       # x'e 5 ata
x += 3      # x = x + 3  (x'i 3 arttır)
x -= 2      # x = x - 2  (x'i 2 azalt)
x *= 2      # x = x * 2  (x'i 2 ile çarp)
x /= 2      # x = x / 2  (x'i 2'ye böl)

#Koşullu İfadeler (if-elif-else)#

#İf Yapısı
yas = 18

if yas >= 18:
    print("Yetişkinsiniz")

#if-else Yapısı
yas = 15

if yas >= 18:
    print("Yetişkinsiniz")
else:
    print("Çocuksunuz")

#if-elif-else Yapısı
not_degeri = 75

if not_degeri >= 85:
    print("AA")
elif not_degeri >= 70:
    print("BA")
elif not_degeri >= 60:
    print("BB")
elif not_degeri >= 50:
    print("CC")
else:
    print("FF")

#İç İçe if Yapısı
yas = 20
ehliyet = True

if yas >= 18:
    if ehliyet:
        print("Araba kullanabilirsiniz")
    else:
        print("Ehliyet almanız gerekiyor")
else:
    print("Yaşınız tutmuyor")

#Çoklu Koşullar
yas = 20
ogrenci = True

# and kullanımı
if yas >= 18 and ogrenci:
    print("Yetişkin öğrenci")

# or kullanımı
if yas < 18 or ogrenci:
    print("İndirim hakkı var")

#İf-Elif-Else Örnekleri#
# Örnek 1: Çift mi Tek mi?
sayi = 7
if sayi % 2 == 0:
    print("Çift")
else:
    print("Tek")

# Örnek 2: Pozitif mi Negatif mi?
sayi = -5
if sayi >= 0:
    print("Pozitif")
else:
    print("Negatif")

# Örnek 3: Sınav Durumu
not_degeri = 65
if not_degeri >= 50:
    print("Geçti")
else:
    print("Kaldı")

#Döngüler (for-while)#


#for Döngüsü
# 0'dan 4'e kadar (5 dahil değil)
for i in range(5):
    print(i)
# Çıktı: 0, 1, 2, 3, 4

#range() Fonksiyonu
# range(başlangıç, bitiş, adım)

# 1'den 10'a kadar
for i in range(1, 11):
    print(i)

# 0'dan 10'a kadar 2'şer 2'şer
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# 10'dan 1'e kadar geriye
for i in range(10, 0, -1):
    print(i)

#Liste Üzerinde Döngü
meyveler = ["elma", "armut", "muz"]

for meyve in meyveler:
    print(meyve)

#String Üzerinde Döngü
kelime = "Python"

for harf in kelime:
    print(harf)
# P, y, t, h, o, n

#for Döngüsü Örnekleri
# Örnek 1: 1-10 arası sayıların toplamı
toplam = 0
for i in range(1, 11):
    toplam += i
print(toplam)  # 55

# Örnek 2: Çarpım tablosu
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Örnek 3: Faktöriyel hesaplama
n = 5
faktoriyel = 1
for i in range(1, n + 1):
    faktoriyel *= i
print(faktoriyel)  # 120

#While Döngüsü
sayac = 0

while sayac < 5:
    print(sayac)
    sayac += 1
# Çıktı: 0, 1, 2, 3, 4

#while True (Sonsuz Döngü)
while True:
    cevap = input("Devam etmek istiyor musunuz? (e/h): ")
    if cevap == "h":
        break  # Döngüyü kır
    print("Devam ediliyor...")

#while Döngüsü Örnekleri#
# Örnek 1: Kullanıcı doğru cevap verene kadar sor
sifre = "1234"
girilen = ""

while girilen != sifre:
    girilen = input("Şifre: ")
print("Giriş başarılı!")

# Örnek 2: Sayıların toplamı (10'a ulaşana kadar)
toplam = 0
sayi = 1

while toplam < 10:
    toplam += sayi
    sayi += 1
print(toplam)

#break ve continue

#break - Döngüyü Sonlandırır
for i in range(10):
    if i == 5:
        break  # i 5 olduğunda döngü biter
    print(i)
# Çıktı: 0, 1, 2, 3, 4

#continue - O adımı atlar, devam eder
for i in range(10):
    if i % 2 == 0:
        continue  # Çift sayıları atla
    print(i)
# Çıktı: 1, 3, 5, 7, 9

#İç İçe Döngüler
# Çarpım tablosu (1-5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("---")

#Fonksiyonlar#
def selamla():
    print("Merhaba!")

#Fonksiyonu çağırma
selamla()  # Çıktı: Merhaba!

#Parametreli Fonksiyonlar
def selamla(isim):
    print(f"Merhaba {isim}!")

selamla("Gül")  # Çıktı: Merhaba Gül!

#Birden Fazla Parametre
def topla(a, b):
    sonuc = a + b
    print(f"{a} + {b} = {sonuc}")

topla(5, 3)  # Çıktı: 5 + 3 = 8

#Değer Döndüren Fonksiyonlar (return)
def topla(a, b):
    return a + b

sonuc = topla(5, 3)
print(sonuc)  # 8

#Varsayılan Parametreler
def selamla(isim="Ziyaretçi"):
    print(f"Merhaba {isim}!")

selamla()        # Merhaba Ziyaretçi!
selamla("Can")   # Merhaba Can!

#Fonksiyon Örnekleri
# Örnek 1: Çift mi kontrol et
def cift_mi(sayi):
    if sayi % 2 == 0:
        return True
    else:
        return False

print(cift_mi(4))   # True
print(cift_mi(7))   # False

# Örnek 2: Faktöriyel hesaplama
def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))  # 120

# Örnek 3: Üs alma
def us_al(taban, us):
    sonuc = 1
    for i in range(us):
        sonuc *= taban
    return sonuc

print(us_al(2, 3))  # 8

# Örnek 4: Ortalama hesaplama
def ortalama_hesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam / len(sayilar)

print(ortalama_hesapla([80, 90, 85]))  # 85.0

# Örnek 5: Palindrome kontrolü
def palindrome_mi(kelime):
    return kelime == kelime[::-1]

print(palindrome_mi("aba"))   # True
print(palindrome_mi("merhaba"))  # False

#Lambda Fonksiyonları
# Normal fonksiyon
def kare(x):
    return x ** 2

# Lambda fonksiyonu
kare = lambda x: x ** 2

print(kare(5))  # 25

#Nesne Tabanlı Programlama#
#Sınıf yapısı
class Araba:
    # __init__ metodu (constructor/yapıcı metot)
    def __init__(self, marka, model, yil):
        self.marka = marka    # Öznitelik
        self.model = model    # Öznitelik
        self.yil = yil        # Öznitelik
    
    # Metot (fonksiyon)
    def bilgi_goster(self):
        print(f"{self.marka} {self.model} - {self.yil}")

# Nesne oluşturma
araba1 = Araba("Toyota", "Corolla", 2020)
araba2 = Araba("Honda", "Civic", 2021)

# Metot çağırma
araba1.bilgi_goster()  # Toyota Corolla - 2020
araba2.bilgi_goster()  # Honda Civic - 2021

class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim  # self ile öznitelik tanımlama
        self.yas = yas
    
    def selamla(self):
        # self ile özniteliklere erişim
        print(f"Merhaba, ben {self.isim}")

#Öznitelikler (Attributes)
class Kisi:
    def __init__(self, isim, yas, sehir):
        self.isim = isim      # Öznitelik
        self.yas = yas        # Öznitelik
        self.sehir = sehir    # Öznitelik

kisi1 = Kisi("Ali", 25, "İstanbul")

#Özniteliklere erişim
print(kisi1.isim)   # Ali
print(kisi1.yas)    # 25
print(kisi1.sehir)  # İstanbul

#Öznitelikleri değiştirme
kisi1.yas = 26
print(kisi1.yas)    # 26

#Metotlar (Methods)
class Hesap_Makinesi:
    def topla(self, a, b):
        return a + b
    
    def cikar(self, a, b):
        return a - b
    
    def carp(self, a, b):
        return a * b
    
    def bol(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Sıfıra bölünemez"

hesap = Hesap_Makinesi()
print(hesap.topla(5, 3))   # 8
print(hesap.cikar(10, 4))  # 6
print(hesap.carp(3, 4))    # 12
print(hesap.bol(10, 2))    # 5.0

#Sınıf Örnekleri

#Örnek 1: Çalışan Sınıfı
class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas
    
    def maas_arttir(self):
        self.maas += 1000
        print(f"{self.isim} maaşı arttırıldı: {self.maas} TL")
    
    def maas_azalt(self):
        if self.maas - 1000 < 0:
            print("Azaltma işlevi başarısız")
        else:
            self.maas -= 1000
            print(f"{self.isim} maaşı azaltıldı: {self.maas} TL")
    
    def bilgi_goster(self):
        print(f"Çalışan: {self.isim}, Maaş: {self.maas} TL")

calisan1 = Calisan("Ahmet", 5000)
calisan1.bilgi_goster()     # Çalışan: Ahmet, Maaş: 5000 TL
calisan1.maas_arttir()      # Ahmet maaşı arttırıldı: 6000 TL
calisan1.maas_azalt()       # Ahmet maaşı azaltıldı: 5000 TL

#Örnek 2: Banka Hesabı Sınıfı
class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye
    
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
    
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
    
    def bakiye_goster(self):
        print(f"{self.hesap_sahibi} - Bakiye: {self.bakiye} TL")


hesap = BankaHesabi("Mehmet", 1000)
hesap.bakiye_goster()        # Mehmet - Bakiye: 1000 TL
hesap.para_yatir(500)        # 500 TL yatırıldı...
hesap.para_cek(200)          # 200 TL çekildi...
hesap.bakiye_goster()        # Mehmet - Bakiye: 1300 TL

#Örnek 3: Öğrenci Sınıfı
class Ogrenci:
    def __init__(self, ad, numara, notlar=[]):
        self.ad = ad
        self.numara = numara
        self.notlar = notlar if notlar else []
    
    def not_ekle(self, not_degeri):
        if 0 <= not_degeri <= 100:
            self.notlar.append(not_degeri)
            print(f"Not eklendi: {not_degeri}")
        else:
            print("Geçersiz not! (0-100 arası olmalı)")
    
    def ortalama_hesapla(self):
        if len(self.notlar) == 0:
            return 0
        return sum(self.notlar) / len(self.notlar)
    
    def durum_goster(self):
        ortalama = self.ortalama_hesapla()
        durum = "Geçti" if ortalama >= 50 else "Kaldı"
        print(f"{self.ad} - Ortalama: {ortalama:.2f} - {durum}")

ogrenci = Ogrenci("Ayşe", "12345")
ogrenci.not_ekle(80)
ogrenci.not_ekle(75)
ogrenci.not_ekle(90)
ogrenci.durum_goster()  # Ayşe - Ortalama: 81.67 - Geçti

#Örnek 4: Dikdörtgen Sınıfı
class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    def alan_hesapla(self):
        return self.genislik * self.yukseklik
    
    def cevre_hesapla(self):
        return 2 * (self.genislik + self.yukseklik)
    
    def bilgi_goster(self):
        print(f"Genişlik: {self.genislik}")
        print(f"Yükseklik: {self.yukseklik}")
        print(f"Alan: {self.alan_hesapla()}")
        print(f"Çevre: {self.cevre_hesapla()}")

#Örnek 5: Karakter Hareket Sistemi
class Karakter:
    def __init__(self, isim):
        self.isim = isim
        self.x = 0
        self.y = 0
    
    def yukari_git(self):
        self.y += 1
        print(f"{self.isim} yukarı gitti")
    
    def asagi_git(self):
        self.y -= 1
        print(f"{self.isim} aşağı gitti")
    
    def sag_git(self):
        self.x += 1
        print(f"{self.isim} sağa gitti")
    
    def sol_git(self):
        self.x -= 1
        print(f"{self.isim} sola gitti")
    
    def konum_goster(self):
        print(f"{self.isim} konumu: X={self.x}, Y={self.y}")


karakter = Karakter("Kahraman")
karakter.konum_goster()  # X=0, Y=0
karakter.sag_git()
karakter.yukari_git()
karakter.konum_goster()  # X=1, Y=1

# Sınıf vs Nesne
# Sınıf =>
class Araba:
    def __init__(self, marka):
        self.marka = marka

# Nesneler => Şablondan üretilen örnekler
araba1 = Araba("Toyota")   # Nesne 1
araba2 = Araba("Honda")    # Nesne 2
araba3 = Araba("Ford")     # Nesne 3

# Her nesne bağımsızdır
print(araba1.marka)  # Toyota
print(araba2.marka)  # Honda
print(araba3.marka)  # Ford

#Örnek#
class Personel:
    def __init__(self, ad, departman, maas):
        self.ad = ad
        self.departman = departman
        self.maas = maas
    
    def bilgileri_goster(self):
        print(f"Personel: {self.ad} | Departman: {self.departman} | Maaş: {self.maas}")

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari
        print(f"Yeni maaş: {self.maas}")

class Yonetici(Personel):
    def __init__(self, ad, departman, maas, kisi_sayisi):
        super().__init__(ad, departman, maas)
        self.kisi_sayisi = kisi_sayisi
        
calisan1 = Personel("Ali", "Bilişim", 30000)
calisan1.zam_yap(5000)

mudur = Yonetici("Ayşe", "Yazılım", 50000, 10)
mudur.bilgileri_goster()