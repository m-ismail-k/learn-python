kullanıcıbirbakiye, kullanıcıikibakiye = 500, 500
havuz = 0
while kullanıcıbirbakiye > 0 and kullanıcıikibakiye > 0:
    while true
        kullanıcıbirbahis = int(int("birinci oyuncu lütfen bahsinizi giriniz"))
        if kullanıcıbirbahis > kullanıcıbirbakiye:
            print("égirmek istediğiniz tutar bakiyenizi aşamaktadır")
            continue
            kullanıcıikibahis = int(imput("ikinci kullanıcı lütfen bahsinizi girin"))
            if kullanıcıikibahis > kullanıcıikibakiye:
                print("girmek istediğiniz tutar bakiyenizi aşmaktadır")
                continue
                kullanıcıbirbakiye -= kullanıcıbirbahis
                kullanıcıikibakiye -= kullanıcıikibahis
                havuz = kullaıcıbirbahis + kullanıcıikibahis
                