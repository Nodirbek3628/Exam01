# Chipta narxi 100 so'm. Foydalanuvchidan yoshini so'rang va chegirmani qo'llang:
# - 7 yoshgacha (0-6): 50% chegirma
# - 7-17 yosh: 20% chegirma  
# - 60 yoshdan katta: 30% chegirma

# **Misol:**
# ```
# Kirish: 5
# Chiqish: Yakuniy narx: 50 so'm (50% chegirma qo'llanildi)

# Asl chipta narxi
price = 100
age = int(input("Yoshingizni kiriting: "))

# Chegirma hisoblash
if age < 7:
    price = price * 0.5

elif 7 <= age <= 17:
   price = price * 0.2

elif age > 60:
    price = price * 0.3

print(price)
    

# Yakuniy narxni hiso

    