from Animal import Animal

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, status, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.status = status
        self.warna = warna
        

    def info_ikan(self):
        super().info_Animal(),
        print("status \t\t: ",self.status,
              "\nwarna \t\t: ",self.warna)
        

ikan_arwana = ikan("arwana", "ikan kecil", "air tawar", "bertelur", "ikan hias", "merah" )
ikan_arwana.info_ikan()
print("=================================================")

ikan_mujair = ikan("mujair", "pelet", "air tawar", "bertelur", "ikan ternak", "silver mengkilat")
ikan_mujair.info_ikan()
    