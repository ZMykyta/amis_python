print('Ведіть координати двох клітин шахової дошки від 1 до 8.\nПрограма визначить чи перейде королева за один хід до заданої клітинки.')
x=int(input('Рядок фігури\n'))
y=int(input('Стовпчик фігури\n'))
x1=int(input('Рядок клітинки\n'))
y1=int(input('Стовпчик клітинки\n'))
if abs(x - x1) == abs(y - y1) or x == x1 or y == y1:
    print('YES')
else:
    print('NO')