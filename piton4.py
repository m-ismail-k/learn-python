kullanıcı = input("lütfen kullanıcı ismi girin: ")
if kullanıcı == "ismail":
    print("tebrikler doğru kullanıcı girildi. ")
elif kullanıcı != ("ismail","ahmet","emine"):
    print("yanlış kullanıcı ismi girdiniz!!! ")

password = int(input("lütfen parolayı giriniz: "))
if password == 1453:
    print("doğru giriş yaptınız..")
elif password != 1453:
    print("kardeş yalnış şifre girdin")
