
from models import Randevu
from datetime import datetime
import json
import os
import numpy as np
import pandas as pd

randevular = []

DOSYA_ADI = "randevular.json"

hizmetler = {
    "Masaj": {"ucret": 1000, "maliyet": 400},
    "Cilt Bakımı": {"ucret": 800, "maliyet": 300},
    "Spor Danışmanlığı": {"ucret": 600, "maliyet": 200},
    "Fizik Tedavi": {"ucret": 1200, "maliyet": 500}
}


def dosyaya_kaydet():
    veriler = [r.sozluk_yap() for r in randevular]

    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, ensure_ascii=False, indent=4)


def dosyadan_yukle():
    global randevular

    if not os.path.exists(DOSYA_ADI):
        return

    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            veriler = json.load(dosya)

        for veri in veriler:
            randevu = Randevu(
                veri["ad"],
                veri["tarih"],
                veri["saat"],
                veri["hizmet"],
                veri["ucret"],
                veri.get("telefon", "")
            )

            randevu.durum = veri["durum"]
            randevular.append(randevu)

    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Kayıt dosyası okunamadı!")


def randevu_ekle():
    print("\n--- RANDEVU EKLE ---")

    try:
        ad = input("Müşteri adı: ").strip()

        if not ad:
            print("Müşteri adı boş olamaz!")
            return

        telefon = input("Telefon: ").strip()

        tarih = input("Tarih (GG.AA.YYYY): ")
        girilen_tarih = datetime.strptime(tarih, "%d.%m.%Y")

        saat = input("Saat (SS:DD): ")
        datetime.strptime(saat, "%H:%M")

        if girilen_tarih.date() < datetime.today().date():
            print("Geçmiş bir tarihe randevu oluşturulamaz!")
            return

        print("\nHizmetler:")

        for hizmet, bilgiler in hizmetler.items():
            print(f"{hizmet}: {bilgiler['ucret']} TL")

        secim = input("\nAlınacak hizmet: ").strip().title()

        if secim not in hizmetler:
            print("Geçersiz hizmet seçimi!")
            return

        for randevu in randevular:
            if (randevu.tarih == tarih
                    and randevu.saat == saat
                    and randevu.durum == "Aktif"):
                print("Bu tarih ve saatte başka bir randevu var!")
                return

        yeni_randevu = Randevu(
            ad,
            tarih,
            saat,
            secim,
            hizmetler[secim]["ucret"],
            telefon
        )

        randevular.append(yeni_randevu)
        dosyaya_kaydet()

        print("Randevu başarıyla eklendi!")

    except ValueError:
        print("Hatalı tarih veya saat girdiniz!")


def randevulari_listele():
    print("\n--- RANDEVU LİSTESİ ---")

    if not randevular:
        print("Henüz kayıtlı randevu bulunmuyor.")
        return

    for sira, randevu in enumerate(randevular, start=1):
        print(f"\nRANDEVU {sira}")
        randevu.bilgileri_goster()


def randevu_ara():
    print("\n--- RANDEVU ARA ---")

    ad = input("Aranacak müşteri adı: ").strip().lower()

    if not ad:
        print("Arama alanı boş olamaz!")
        return

    bulunanlar = [
        r for r in randevular
        if ad in r.ad.lower()
    ]

    if not bulunanlar:
        print("Randevu bulunamadı.")
        return

    for sira, randevu in enumerate(bulunanlar, start=1):
        print(f"\nRANDEVU {sira}")
        randevu.bilgileri_goster()


def randevu_iptal():
    print("\n--- RANDEVU İPTAL ET ---")

    randevulari_listele()

    if not randevular:
        return

    try:
        sira = int(input("\nİptal edilecek randevu numarası: "))

        if sira < 1 or sira > len(randevular):
            print("Geçersiz randevu numarası!")
            return

        randevu = randevular[sira - 1]

        if randevu.durum != "Aktif":
            print("Bu randevu iptal edilemez!")
            return

        randevu.durum = "İptal Edildi"
        dosyaya_kaydet()

        print("Randevu başarıyla iptal edildi!")

    except ValueError:
        print("Lütfen geçerli bir numara giriniz!")


def randevu_tamamla():
    print("\n--- RANDEVU TAMAMLA ---")

    randevulari_listele()

    if not randevular:
        return

    try:
        sira = int(input("\nTamamlanacak randevu numarası: "))

        if sira < 1 or sira > len(randevular):
            print("Geçersiz randevu numarası!")
            return

        randevu = randevular[sira - 1]

        if randevu.durum != "Aktif":
            print("Bu randevu tamamlanamaz!")
            return

        randevu.durum = "Tamamlandı"
        dosyaya_kaydet()

        print("Randevu tamamlandı olarak işaretlendi!")

    except ValueError:
        print("Lütfen geçerli bir numara giriniz!")


def gelir_kar_hesapla():
    print("\n--- GELİR VE KÂR RAPORU ---")

    tamamlananlar = [
        r for r in randevular
        if r.durum == "Tamamlandı"
    ]

    if not tamamlananlar:
        print("Henüz tamamlanmış randevu bulunmuyor.")
        return

    gelir = sum(r.ucret for r in tamamlananlar)

    maliyet = sum(
        hizmetler[r.hizmet]["maliyet"]
        for r in tamamlananlar
    )

    kar = gelir - maliyet
    kar_yuzdesi = (kar / gelir) * 100 if gelir > 0 else 0

    ucretler = np.array([r.ucret for r in tamamlananlar])
    ortalama = np.mean(ucretler)

    print(f"Tamamlanan randevu sayısı: {len(tamamlananlar)}")
    print(f"Toplam gelir: {gelir} TL")
    print(f"Toplam maliyet: {maliyet} TL")
    print(f"Toplam kâr: {kar} TL")
    print(f"Kâr yüzdesi: %{kar_yuzdesi:.2f}")
    print(f"Ortalama hizmet ücreti: {ortalama:.2f} TL")

    veriler = []

    for r in tamamlananlar:
        veriler.append({
            "Hizmet": r.hizmet,
            "Gelir": r.ucret,
            "Maliyet": hizmetler[r.hizmet]["maliyet"],
            "Kar": r.ucret - hizmetler[r.hizmet]["maliyet"]
        })

    tablo = pd.DataFrame(veriler)

    rapor = tablo.groupby("Hizmet").agg(
        Randevu_Sayisi=("Hizmet", "count"),
        Toplam_Gelir=("Gelir", "sum"),
        Toplam_Maliyet=("Maliyet", "sum"),
        Toplam_Kar=("Kar", "sum")
    )

    print("\n--- HİZMET TÜRLERİNE GÖRE RAPOR ---")
    print(rapor.to_string())


def ana_menu():
    while True:
        print("\n================================")
        print("       RANDEVU TAKİP SİSTEMİ")
        print("================================")
        print("1- Randevu Ekle")
        print("2- Randevuları Listele")
        print("3- Randevu Ara")
        print("4- Randevu İptal Et")
        print("5- Randevu Tamamla")
        print("6- Gelir / Kâr Hesapla")
        print("0- Çıkış")

        secim = input("\nSeçiminiz: ")

        if secim == "1":
            randevu_ekle()

        elif secim == "2":
            randevulari_listele()

        elif secim == "3":
            randevu_ara()

        elif secim == "4":
            randevu_iptal()

        elif secim == "5":
            randevu_tamamla()

        elif secim == "6":
            gelir_kar_hesapla()

        elif secim == "0":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Hatalı seçim! Tekrar deneyiniz.")


dosyadan_yukle()
ana_menu()
