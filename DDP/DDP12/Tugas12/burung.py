from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu


    def info_burung(self):
        super().info_animal()
        print("Paruh \t\t\t : ", self.paruh,
              "\warna_bulu \t\t : ", self.warna_bulu)

Burung_beo = Burung("Burung Beo", "Jagung", "Darat", "Bertelur", "melengkung", "Warna_warni")
Burung_beo.info_burung()