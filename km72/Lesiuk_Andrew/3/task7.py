print('Програма визначає скільки показуватиме годинник')
while True:
    N=int(input('Введіть скільки часу пройшло після півночі\n'))
    if N<0:
        print('Час маэ бути додатнім')
    else:
        break
t = N//1440
print('Кількість днів:', t)
print('Кількість годин:', t//60)
print('Кількість хвилин:', t%60)
