num = int(input("Faktoriyelini alacağınız sayıyı giriniz: "))

faktoriyel = 1

if num < 0:
    print("Lütfen pozitif sayı girin.")
elif num == 0:
    print("Cevap: 0")
else:
    for i in range(1,num+1):
        faktoriyel = faktoriyel*i
    print("Cevap:",faktoriyel)
