# f-string yordamida ism va yoshni birlashtiring**

# | Input                                                                    | Output       |
# | ------------------------------------- | --------------------------------------- |
# | `"Ali"`, `20` | `My name is Ali and I am 20 years old.` |

# ---

name = input("Ismingizni kiritin: ").capitalize()     # Bunda kiritilgan ism kichkina harf bilan kiritiilsa tizim avtomatik katta harfga o'ngarib beradi 
age = int(input("Yoshingizni kiriting: "))

result = f"My name is {name} and I am {age} years old."

print(result)