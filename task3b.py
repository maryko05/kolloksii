# 1) salam adlı funksiya
def salam():
    print("Salam, Dünya!")

# 2) kub_hesabla adlı funksiya
def kub_hesabla(n):
    return n ** 3

# 3) birlesdir adlı funksiya
def birlesdir(soz1, soz2):
    return soz1 + " " + soz2

# 4) cap_et adlı funksiya
def cap_et(liste):
    for element in liste:
        print(element)

# 5) toplam adlı funksiya
def toplam(*args):
    return sum(args)

# 6) ortalama adlı funksiya
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7) adlar_rəqəmlər adlı funksiya
def adlar_rəqəmlər(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")

# 8) tip_yoxla adlı funksiya
def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

# 9) yas_kateqoriya adlı funksiya
def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

# 10) soz_uzunluq adlı funksiya
def soz_uzunluq():
    soz = input("Bir söz daxil edin: ")
    print("Uzunluq:", len(soz))
