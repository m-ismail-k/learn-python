def faktoriyel(Sayi):
    factorial=1
    for x in range(1,sayi+1):
        factorial *= x
    print(factorial)

try:
    faktoriyel(int(input("lütfen bir sayı girin")))
except:
    print("düzgün bi değer gir amk!! ")