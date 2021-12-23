import random

Popitka = 0

print('Привет, меня зовут Programma! А как тебя зовут?')
name = input()
print('Приятно познакомится, ' + name+ '!')

end = 'игра продолжается'

while end != 'n':
    print('Я загадаю целое число от 1 до 20. попробуй отгадай его за 6 попыток.')

    number = random.randint(1, 20)
    print(str(number))

    for popitka in range(6):
        print('Какое число?')
        chislo = input()
        chislo = int(chislo)

        if chislo > number:
            print('Слишком много')

        if chislo < number:
            print('Слишком мало.')

        if chislo == number:
            break

    if chislo == number:
        print('Ура!!!Молодец, ' + name + '! Прямо в точку! Я загадала число '+ str(number) +'.')

    if chislo != number:
        print('Увы,неверно :(')
        
    print('Попробуем еще раз?')
    print('Если, если не хочешь играть, введи"n"/')
    end = input()
    
    
    
    


