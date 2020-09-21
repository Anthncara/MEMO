print("Enter a number")
print()
number = int(input())
list = []
for i in range(number):
    a = input()
    b = a.isdigit()
    if b == True:
        a = int(a)
        list.append(a)
    else:
        print("Lütfen tam sayı giriniz :")
max = 0
for i in list:
    if i > max:
        max = i
print("...", max)