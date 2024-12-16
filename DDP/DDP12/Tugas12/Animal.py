# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

# buat minimal 2 objek untuk setiap class childnya. 

class Animal:

    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_Animal(self):
        print("Nama \t\t: ", self.nama,
              "\nMakanan \t: ", self.makanan,
              "\nHidup \t\t: ", self.hidup,
              "\nBerkembang Biak : ", self.berkembang_biak)
    

binatang = Animal("Kucing", "cimol", "udara", "bertelur")
binatang.info_Animal()

# binatang = Animal("kucing", "cimol", "udara", "bertelur")
