# 1) x dəyişəni üzrə "müsbət", "mənfi", "sıfır"
x = 5
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2) n rəqəmi cütdürsə "cüt", təkdirsə "tək"
n = 4
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

# 3) a, b, c üçün ən böyük rəqəmi tapmaq
a, b, c = 10, 25, 18
print("Ən böyük:", max(a, b, c))

# 4) day dəyişəni üzrə həftə günü
day = 3
weekdays = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(weekdays.get(day, "Yanlış gün"))

# 5) temp dəyişəni üzrə temperaturun qiymətləndirilməsi
temp = 15
if temp < 0:
    print("soyuq")
elif 0 <= temp <= 20:
    print("normal")
else:
    print("isti")

# 6) password uzunluğu
password = "salam1234"
if len(password) < 8:
    print("qısa")
elif 8 <= len(password) <= 12:
    print("orta")
else:
    print("uzun")

# 7) x rəqəmi 3 və 5 bölünməsi
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8) 0-dan 20-yə qədər cüt rəqəmləri çap et
for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 9) Hər hərfi ayrı çap et
text = "Bağda ərik var idi …"
for ch in text:
    print(ch)

# 10) 1-dən 10-a qədər, 3 istisna olmaqla
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11) İlk 5-ə bölünən rəqəmi while ilə tap
i = 1
while True:
    if i % 5 == 0:
        print("İlk 5-ə bölünən:", i)
        break
    i += 1

# 12) Listdə 5-in indeksini tap
nums = [1, 3, 5, 7, 9]
for idx, val in enumerate(nums):
    if val == 5:
        print("5-in indeksi:", idx)
        break
