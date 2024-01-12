def faktoriyel_hesapla(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel_hesapla(n-1)

# Kullanıcıdan bir sayı dizisi al
sayilar = input("Faktöriyelini hesaplamak istediğiniz sayıları aralarında boşluk bırakarak girin: ")

# Girişi parçalayarak sayıları elde et
sayi_listesi = [int(sayi) for sayi in sayilar.split()]

# Her bir sayının faktöriyelini hesapla ve ekrana yazdır
for sayi in sayi_listesi:
    sonuc = faktoriyel_hesapla(sayi)
    print(f"{sayi}! = {sonuc}")
