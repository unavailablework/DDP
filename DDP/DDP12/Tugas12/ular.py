from Animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis
    

    def info_ular(self):
        super().info_Animal(),
        print("warna \t\t: ", self.warna,
              "\njenis \t\t: ", self.jenis)
        

ular_pithon = ular("pithon", "hewan lain", "darat", "bertelur", "item ke ijo-ijoan", "tidak berbisa")
ular_pithon.info_ular()
print("=====================================================")


ular_ijo = ular("ular ijo", "hewan lain", "darat", "bertelur", "ijo", "berbisa")
ular_ijo.info_ular()