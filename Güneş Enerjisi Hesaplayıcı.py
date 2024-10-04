import math

class GunesEnerjisiHesaplayici:
    def __init__(self):
        self.panel_alani = 0
        self.panel_verimi = 0
        self.performans_orani = 0
        self.gunes_isigi_verileri = []

    def kullanici_girisi_al(self):
        print("Güneş Enerjisi Hesaplayıcısına Hoş Geldiniz!")
        
        while True:
            try:
                self.panel_alani = float(input("Güneş paneli alanını (m²) girin: "))
                if self.panel_alani <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Lütfen geçerli bir pozitif sayı girin.")

        while True:
            try:
                self.panel_verimi = float(input("Güneş paneli verimini (%) girin: "))
                if not 0 < self.panel_verimi <= 100:
                    raise ValueError
                self.panel_verimi /= 100  # Yüzdeyi ondalık sayıya çevir
                break
            except ValueError:
                print("Lütfen 0 ile 100 arasında geçerli bir sayı girin.")

        while True:
            try:
                self.performans_orani = float(input("Sistem performans oranını (genellikle 0.75 ile 0.85 arası) girin: "))
                if not 0 < self.performans_orani <= 1:
                    raise ValueError
                break
            except ValueError:
                print("Lütfen 0 ile 1 arasında geçerli bir sayı girin.")

        print("\nŞimdi 12 ay için ortalama günlük güneş ışınımı verilerini girelim.")
        aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 
                 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
        
        for ay in aylar:
            while True:
                try:
                    isinim = float(input(f"{ay} ayı için ortalama günlük güneş ışınımını (kWh/m²/gün) girin: "))
                    if isinim < 0:
                        raise ValueError
                    self.gunes_isigi_verileri.append(isinim)
                    break
                except ValueError:
                    print("Lütfen geçerli bir pozitif sayı girin.")

    def enerji_uretimini_hesapla(self):
        aylik_uretim = []
        toplam_uretim = 0
        
        for i, isinim in enumerate(self.gunes_isigi_verileri):
            gun_sayisi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][i]
            aylik = (isinim * self.panel_alani * self.panel_verimi * self.performans_orani * gun_sayisi)
            aylik_uretim.append(aylik)
            toplam_uretim += aylik

        return aylik_uretim, toplam_uretim

    def sonuclari_goster(self, aylik_uretim, toplam_uretim):
        print("\n--- Güneş Enerjisi Üretim Tahmini ---")
        print(f"Panel Alanı: {self.panel_alani} m²")
        print(f"Panel Verimi: {self.panel_verimi * 100}%")
        print(f"Sistem Performans Oranı: {self.performans_orani}")
        
        print("\nAylık Enerji Üretimi Tahminleri:")
        aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 
                 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
        for ay, uretim in zip(aylar, aylik_uretim):
            print(f"{ay}: {uretim:.2f} kWh")
        
        print(f"\nToplam Yıllık Enerji Üretimi: {toplam_uretim:.2f} kWh")
        print(f"Ortalama Günlük Enerji Üretimi: {toplam_uretim / 365:.2f} kWh")

    def calistir(self):
        self.kullanici_girisi_al()
        aylik_uretim, toplam_uretim = self.enerji_uretimini_hesapla()
        self.sonuclari_goster(aylik_uretim, toplam_uretim)

if __name__ == "__main__":
    hesaplayici = GunesEnerjisiHesaplayici()
    hesaplayici.calistir()