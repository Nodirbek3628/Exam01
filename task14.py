# Document type aniqlash**

# Fayl nomi `.pdf`, `.docx`, yoki `.txt` bilan tugashini tekshiring

# | Input          | Output  |
# | -------------- | ------- |
# | `"report.pdf"` | `True`  |
# | `"photo.jpeg"` | `False` |


document = input("Fayllar nomini kiriting: ")

if document.endswith("pdf") or  document.endswith("docx") or document.endswith("txt"):    # har birini oxiri shu fayl bilan tugashini tekshiramz
    print(True)
else:
    print(False)