
import json
import os
from models import Randevu

DOSYA_ADI = "randevular.json"

ornek_randevular = [
    ("Ayşe Yılmaz", "05551234567", "13.11.2026", "09:00", "Masaj", 1000, "Tamamlandı"),
    ("Mehmet Demir", "05551234568", "13.11.2026", "10:00", "Cilt Bakımı", 800, "Tamamlandı"),
    ("Zeynep Kaya", "05551234569", "13.11.2026", "11:00", "Fizik Tedavi", 1200, "Tamamlandı"),
    ("Ali Çelik", "05551234570", "13.11.2026", "12:00", "Spor Danışmanlığı", 600, "Aktif"),
    ("Elif Şahin", "05551234571", "14.11.2026", "09:00", "Masaj", 1000, "Tamamlandı"),
    ("Can Yıldız", "05551234572", "14.11.2026", "10:00", "Cilt Bakımı", 800, "Tamamlandı"),
    ("Merve Aydın", "05551234573", "14.11.2026", "11:00", "Fizik Tedavi", 1200, "İptal Edildi"),
    ("Burak Arslan", "05551234574", "14.11.2026", "12:00", "Spor Danışmanlığı", 600, "Aktif"),
    ("Fatma Koç", "05551234575", "15.11.2026", "09:00", "Masaj", 1000, "Tamamlandı"),
    ("Emre Kurt", "05551234576", "15.11.2026", "10:00", "Cilt Bakımı", 800, "Tamamlandı"),
    ("Seda Özkan", "05551234577", "15.11.2026", "11:00", "Fizik Tedavi", 1200, "Tamamlandı"),
    ("Ahmet Polat", "05551234578", "15.11.2026", "12:00", "Masaj", 1000, "Aktif"),
    ("Derya Aksoy", "05551234579", "16.11.2026", "09:00", "Spor Danışmanlığı", 600, "Tamamlandı"),
    ("Kerem Aslan", "05551234580", "16.11.2026", "10:00", "Masaj", 1000, "Tamamlandı"),
    ("Büşra Güneş", "05551234581", "16.11.2026", "11:00", "Cilt Bakımı", 800, "İptal Edildi"),
    ("Onur Yalçın", "05551234582", "16.11.2026", "12:00", "Fizik Tedavi", 1200, "Aktif"),
    ("Ece Doğan", "05551234583", "17.11.2026", "09:00", "Masaj", 1000, "Tamamlandı"),
    ("Murat Tekin", "05551234584", "17.11.2026", "10:00", "Cilt Bakımı", 800, "İptal Edildi"),
    ("Selin Yıldırım", "05551234585", "17.11.2026", "11:00", "Fizik Tedavi", 1200, "Tamamlandı"),
    ("Okan Şimşek", "05551234586", "17.11.2026", "12:00", "Spor Danışmanlığı", 600, "İptal Edildi")
]


def ornek_verileri_olustur():
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            mevcut_veriler = json.load(dosya)

        if mevcut_veriler:
            print("JSON dosyasında zaten kayıt bulunuyor.")
            print("Mevcut kayıtlar korunmuştur.")
            return

    randevular = []

    for veri in ornek_randevular:
        ad, telefon, tarih, saat, hizmet, ucret, durum = veri

        randevu = Randevu(ad, tarih, saat, hizmet, ucret, telefon)
        randevu.durum = durum
        randevular.append(randevu.sozluk_yap())

    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(randevular, dosya, ensure_ascii=False, indent=4)

    print(f"{len(randevular)} örnek randevu başarıyla oluşturuldu!")


if __name__ == "__main__":
    ornek_verileri_olustur()
