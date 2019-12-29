class Araba:
    marka = None
    model = None
    yakit = ""
    renk = None

    def Gazabas(self):
        print("yol almaya baslandı")


tofaş = Araba()
tofaş.model = "şahin"
tofaş.marka = "tofaş"
tofaş.renk = "siyah"
tofaş.yakit = 15

tofaş.Gazabas()

# a=Araba()
# print(a.marka)
Araba.marka="bugatti"