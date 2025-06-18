# **Stringdagi unli harflarni sanang**

# Foydalanuvchidan matn oling. `for` yordamida nechta unli harf (`a, e, i, o, u`) borligini aniqlang.

# ➡️ Masalan: `"hello world"` → `3`

# ---

matn = input("Matnni kiriting: ")

unlilar = "aeiou"
sana = 0

for harf in matn.lower():
    if harf in unlilar:
        sana += 1

print("Unli harflar soni:", sana)
