# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))
D = S ** 2 - 4*P     # рассчет дискриминанта

if S < 0 or P <= 0:     # чтобы не получились отрицательные корни
    print('Петя мог загадать только натуральные числа.')
else:
    if D < 0:   # чтобы не получились комплексные корни
        print(f'Не существует ни одной пары натуральных чисел, удовлетворяющих заданным условиям.')
    else:
        X1 = (S - (S ** 2 - 4*P) ** 0.5) / 2
        X2 = (S + (S ** 2 - 4*P) ** 0.5) / 2
        if X1 > 1000 or X2 > 1000:
            print('Петя не мог загадать такие большие числа.')
        else:
            fractionalPart1 = X1 - int(X1)  # дробная часть первого корня
            fractionalPart2 = X2 - int(X2)  # дробная часть второго корня
            if fractionalPart1 == 0 and fractionalPart2 == 0:   # проверка на целостность
                print(f'Петя загадал числа {int(X1), int(X2)}')
            else:
                print(f'Не существует ни одной пары натуральных чисел, удовлетворяющих заданным условиям.')
        

    



