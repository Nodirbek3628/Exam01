# **BMI hisoblash va tasnif**

# **Vazifa:** Foydalanuvchidan vazn (kg) va bo'y (m) so'rang. BMI ni hisoblang va tasniflang:
# - BMI < 18.5: "Kam vazn"
# - 18.5 ≤ BMI < 25: "Normal vazn"
# - 25 ≤ BMI < 30: "Ortiqcha vazn"  
# - BMI ≥ 30: "Semizlik"

try:
    vazn = float(input("Vazningizni kiriting (kg): "))
    boy = float(input("Bo'yingizni kiriting (metr): "))

    if vazn <= 0 or boy <= 0:
        print("Xatolik: Vazn va bo'y musbat son bo'lishi kerak!")
    elif not (1 <= vazn <= 500):
        print("Xatolik: Vazn 1-500 kg oralig'ida bo'lishi kerak!")
    elif not (0.5 <= boy <= 3.0):
        print("Xatolik: Bo'y 0.5-3.0 metr oralig'ida bo'lishi kerak!")
    else:
        
        bmi = vazn / (boy ** 2)

        if bmi < 18.5:
            tasnif = "Kam vazn"
        elif bmi < 25:
            tasnif = "Normal vazn"
        elif bmi < 30:
            tasnif = "Ortiqcha vazn"
        else:
            tasnif = "Semizlik"

        print(f"BMI: {round(bmi, 2)} - {tasnif}")

except ValueError:
    print("Xatolik: Iltimos, faqat son kiriting!")
