a = float(input("nhap a ="))
b = float(input("nhap b ="))
c = float(input("nhap c ="))
if a ==0 :
    x = -c // b
    print(x)
else :
    delta = b**2 - 4*a*c
    print(delta)

    if delta < 0 :
        print("phuong trinh vo nghiem ")
    elif delta ==0 :
        print ("phuong trinh co mot nghiem kep")
        x = -b // (2 *a)
        print(x)
    else:
        delta_sqrt = delta**0.5
        print("phuong trinh co hai nghiem phan biet")
        x1 = (-b + delta_sqrt)//(2*a)
        x2 = (-b - delta_sqrt)//(2*a)
        print(x1)
        print(x2)
