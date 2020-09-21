
print("###  This program finds maximum number which you enter ###")
print("How many number you want to enter")
say = int(input())
x = []
for i in range(say):
    a = input()
    b = a.isdigit()
    if b == True:
        a = int(a)
        x.append(a)
    else:
        print("Lütfen tam sayı giriniz :")
print ("girdiğiniz sayıların sırası", x)
x = sorted(x, reverse=True)
print("girdiğiniz sayıların büyükten küçüğe sıralaması ", x)
print('en büyük sayı = ', x[0])

max = 0
for i in x:
    if i > max:
        max = i
print("girdiğiniz sayıların büyükten küçüğe sıralması", x)
print("en büyük sayı = ", max)
