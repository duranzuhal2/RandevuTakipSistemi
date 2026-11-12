# Python ile Randevu Takip Sistemi

## Proje Hakkında

Bu proje, sağlıklı yaşam kompleksleri için geliştirilmiş Python tabanlı bir randevu takip sistemidir. Program terminal üzerinden çalışır.

Sistem sayesinde müşterilerin randevuları kaydedilebilir, listelenebilir, aranabilir, iptal edilebilir ve tamamlandı olarak işaretlenebilir.

## Projenin Özellikleri

- Randevu ekleme
- Randevuları listeleme
- Müşteri adına göre randevu arama
- Randevu iptal etme
- Randevu tamamlama
- Toplam gelir ve kâr hesaplama
- Ortalama hizmet ücreti hesaplama
- Hizmet türlerine göre gelir ve kâr raporu
- JSON dosyası ile kayıtları saklama

## Kullanılan Teknolojiler

- Python 3
- NumPy
- Pandas
- JSON
- Nesne Tabanlı Programlama (OOP)

## Dosyalar

- `main.py`: Ana program ve randevu işlemleri
- `models.py`: Sınıflar ve randevu bilgileri
- `randevular.json`: Randevu kayıtları
- `ornek_veri.py`: 20 örnek randevu oluşturma

## Kurulum

Gerekli kütüphaneleri yüklemek için terminale şu komut yazılır:

```bash
python -m pip install numpy pandas
```

## Programı Çalıştırma

Önce örnek kayıtları oluşturmak için:

```bash
python ornek_veri.py
```

Ardından programı başlatmak için:

```bash
python main.py
```

## Kullanım

Program açıldığında kullanıcıya bir menü sunulur. Menü üzerinden randevu ekleme, listeleme, arama, iptal etme, tamamlama ve gelir/kâr hesaplama işlemleri gerçekleştirilebilir.

Randevu bilgileri JSON dosyasına kaydedilir. Böylece program tekrar açıldığında kayıtlar korunur.

## Geliştirici

İleri Yazılım Teknikleri Dersi Ödevi
