print(""""
*****
TEKIN BANK ATM'ye HOSGELDINIZ

1.Bakiye Sorgulama

2.Para Yatirma

3.Para Cekme 

ATM'den ayrilmak icin 'q" ya basiniz

*****""")

bakiye = 1000

while True:
    islem = raw_input("islemi seciniz")
    if (islem=="q"):
        print("Yine bekleriz...")
        break
    elif (islem== "1"):
        print("Hesabinizda bulunan taplam miktar {}'dir:\nDevam etmek istiyorsainiz islem numarasini giriniz yoksa 'q' ya basip cikabilirsiniz".format(bakiye))
    elif(islem=="2"):
        x= int(input("Yatirmak istediginiz tutari giriniz:"))
        bakiye += x
        print("Devam etmek istiyorsainiz islem numarasini giriniz yoksa 'q' ya basip cikabilirsiniz ", bakiye)
    elif(islem == "3"):
        y = int(input("Cekmek istediginiz tutari giriniz:"))
        if (bakiye < y):
            print("Yetersiz Bakiye")
            continue
        bakiye -=y
        print("Kalan bakiyeniz{}".format(bakiye))
        print("Devam etmek istiyorsainiz islem numarasini giriniz yoksa '0' ya basip cikabilirsiniz ",bakiye)

    else:
        print("Gecersiz Bir Islem Girdiniz, Tekrar deneyin")


