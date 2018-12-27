from random import randint
n=randint(1,100)

m= int(input(" nhap m : "))
print("m =", m)

while m !=n :
    if m < n :
        print("ban phai doan cao hon")
        m= int(input(" nhap m : "))
    elif m > n :
        print("ban phai doan thap hon")
        m= int(input(" nhap m : "))
    
print("bingo")