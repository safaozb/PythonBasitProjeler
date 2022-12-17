from random import randint
tahmin=randint(1,100)
sayac = 0
while True:
    sayac += 1
    sayi = int(input("Sayı giriniz: "))
    sayi = int(sayi)
    if sayi < tahmin:
        print("Daha büyük bir sayı giriniz.")
        continue
    elif sayi > tahmin:
        print("Daha küçük bir sayı giriniz.")
        continue
    else:
        print(f"Tebrikler, sayıyı {sayac} denemede buldunuz.")
        break
