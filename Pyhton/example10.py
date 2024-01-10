from collections import Counter
import re

def dosya_oku(dosya_yolu):
    """Belirtilen dosyadan metni okur ve döndürür."""
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        icerik = dosya.read()
    return icerik

def kelimeleri_say(metin):
    """Metindeki kelimeleri sayar ve en sık geçenleri döndürür."""
    # Noktalama işaretlerini ve büyük harfleri kaldır
    temiz_metin = re.sub(r'[^\w\s]', '', metin).lower()
    kelimeler = temiz_metin.split()

    # Kelimeleri say ve en sık geçenleri bul
    kelime_sayisi = Counter(kelimeler)
    en_sik_kelimeler = kelime_sayisi.most_common(10)
    return en_sik_kelimeler

# Metin dosyasını oku
metin_dosyasi = 'ornek_metin.txt'  # Metin dosyasının yolu
metin = dosya_oku(metin_dosyasi)

# En sık geçen kelimeleri bul ve yazdır
sik_kelimeler = kelimeleri_say(metin)
print("En sık geçen kelimeler:")
for kelime, sayi in sik_kelimeler:
    print(f"{kelime}: {sayi}")
