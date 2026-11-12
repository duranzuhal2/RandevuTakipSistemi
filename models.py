
class Musteri:
    def __init__(self, ad, telefon=""):
        self.ad = ad
        self.telefon = telefon


class Randevu(Musteri):
    def __init__(self, ad, tarih, saat, hizmet, ucret, telefon=""):
        super().__init__(ad, telefon)

        self.tarih = tarih
        self.saat = saat
        self.hizmet = hizmet
        self.ucret = ucret
        self.durum = "Aktif"

    def bilgileri_goster(self):
        print("Müşteri:", self.ad)
        print("Telefon:", self.telefon)
        print("Tarih:", self.tarih)
        print("Saat:", self.saat)
        print("Hizmet:", self.hizmet)
        print("Ücret:", self.ucret, "TL")
        print("Durum:", self.durum)

    def sozluk_yap(self):
        return {
            "ad": self.ad,
            "telefon": self.telefon,
            "tarih": self.tarih,
            "saat": self.saat,
            "hizmet": self.hizmet,
            "ucret": self.ucret,
            "durum": self.durum
        }
    def randevu_aktif_mi(self):
        return self.durum == "Aktif"
