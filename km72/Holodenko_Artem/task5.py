import time
print("Ця програма зчитує ціле число, друкує його попереднє і наступне значення.")
a=int(input("Введіть число: "))
print("Наступне значення числа",a,"є",a+1)
print("Попереднє значення числа",a,"є",a-1)
time.sleep(3)
