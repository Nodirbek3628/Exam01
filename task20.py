# **To‘g‘ri javob kiritilmaguncha davom et**

# Dastur foydalanuvchidan “O‘zbekiston poytaxti nima?” deb so‘raydi. “Toshkent” deb to‘g‘ri javob berguncha so‘rashda davom etadi.

def ask_question(question):
    user_answer = input(f"{question} ").strip()
    return user_answer

def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    return result

def main():
    question = "O'zbekiston poytaxti qayer?"
    correct_answer = "Toshkent"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer, correct_answer)

    if is_correct:
        print("to'g'ri topdingiz.")
    else:
        print(f"topolmadingiz, to'g'ri javob \"{correct_answer}\"")

main()
