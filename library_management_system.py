class Library:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()  

    def kitap_ekle(self):
        kitap_adi = input("Kitap Adı:")
        yazar = input("Yazar:")
        yayin_tarihi = input("Yayın Tarihi:")
        sayfa_sayisi = input("Sayfa Sayısı:")
        yeni_kitap = f"{kitap_adi},{yazar},{yayin_tarihi},{sayfa_sayisi}\n"
        
        self.dosya.seek(0)
        if yeni_kitap in self.dosya.read():
            print("Bu kitap zaten listede mevcut.")
        else:
            self.dosya.write(yeni_kitap)
            
            print("Kitap listeye eklendi.")

    def kitap_sil(self, silinecek_kitap):
        dosya_icerigi = self.dosya.readlines()
        self.dosya.seek(0)
        dosya_yaz = []
        durum = False
        for satir in dosya_icerigi:
            if silinecek_kitap in satir:
                durum = True
            else:
                dosya_yaz.append(satir)
        self.dosya.truncate(0)
        self.dosya.writelines(dosya_yaz)
        if durum:
            print("Kitap silindi.")
        else:
            print("Silmek istediğiniz kitap bulunamadı.")

    def kitaplari_listele(self):
        self.dosya.seek(0)
        print("Kitaplar:")
        dosya_icerik = self.dosya.readlines()
        for sayi, satir in enumerate(dosya_icerik, 1):
            print(sayi, satir.strip())

lib = Library("books.txt")
while True:
    print("MENU")
    print("1- Kitapları Listele")
    print("2- Kitap Sil")
    print("3- Kitap Ekle")
    print("[Q] Çıkış")
    islem = input("İşlem seçimi yapınız:")
    if islem == "1":
        lib.kitaplari_listele()
    elif islem == "2":
        silinecek_kitap = input("Silmek istediğiniz kitabın adını giriniz:")
        lib.kitap_sil(silinecek_kitap)
    elif islem == "3":
        lib.kitap_ekle()
    elif islem.lower() == "q":
        break
    else:
        print("Geçersiz işlem seçimi, lütfen tekrar deneyin.")