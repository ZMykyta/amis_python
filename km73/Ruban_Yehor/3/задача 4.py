N = int(input("Введите количество студентов - "))
K = int(input("Введите количество яблок - "))
if K >= N:
    B = K//N
    C = K%N
    print("количество яблок у студентов - ", B)
    print("количество яблок в корзине - ", C)
else:
    print("Яблок меньше, чем студентов")
    
input()
