ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]

# 1.Soru
ogrenciler.append("Selim Çakır")
print(ogrenciler)

# 2.Soru
ogrenciler.pop(3)
print(ogrenciler)

# 3.Soru
def ogrenciEkle():
    ogrenci1=input("Öğrenci1 adı:")
    ogrenci2=input("Öğrenci2 adı:")

    ogrenciler.extend([ogrenci1],[ogrenci2])
    return ogrenciler
ogrenciEkle()
print(ogrenciler)

# 4.Soru
def ogrencilistele():
    for i in range(len(ogrenciler)):
        print(ogrenciler[i])

ogrencilistele()

# 5.Soru
def ogrenci_index():
    i=0
    while i <len(ogrenciler):
        i+=1
        print(f"{(ogrenciler[i]),ogrenciler.index(ogrenciler[i])}")

ogrenci_index()

# 6 ve 7. Sorular

ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]
i=0
while i<len(ogrenciler):
      i+=1
      print(i)
      print(ogrenciler[i])
      if ogrenciler[i]=="İsmail Keskin":
        ogrenciler.remove("İsmail Keskin")
        print(ogrenciler)
        break

print("******************")



ogrenciler=["Kemal Ünlü","Tarık Sezgin","İsmail Keskin","Yavuz Kılıç","Esat Albayrak"]
for ogrenci in ogrenciler:
    ogrenci=ogrenciler.pop()
    print(ogrenci)


