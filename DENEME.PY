# kullanıcı ve sifre kontrolü
# kullanıcı ismi admin şifre 123 ise giriş başarılı bir tanesi bile yanlışsa giriş başarısız yazdıran bir fonksiyon .
# isim = input("lütfen isminizi giriniz")
# yas = input("lütfen yaşınızı giriniz ")
#
#
# def isimveyas(isim, yas):
#     print("isim => {}, yas= > {}".format(a, b))
#
#
# isimveyas(isim, yas)


def kontrolet(isim, sifre):
    if isim == "emine" and sifre == "123":
        print("giriş başarılı")
    else:
        print("giriş başarısız")


name = input("isim giriniz")
password = input("şifre giriniz")
kontrolet(name,password)