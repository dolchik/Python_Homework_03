# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

ScrabbleDic = {1: "AEIOULNSTRАВЕИНОРСТ", 2: "DGДКЛМПУ", 3: "BCMPБГЁЬЯ", 4: "FHVWYЙЫ", 5: "KЖЗХЦЧ", 8: "JXШЭЮ", 10: "QZФЩЪ"}

word = input('Введите слово: ').upper()
score = 0
for i in word:
    for key, val in ScrabbleDic.items():
        if i in val:
            score += key         
print(score)