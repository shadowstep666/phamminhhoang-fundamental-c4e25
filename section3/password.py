loop = True
while loop :
    password= input("enter your password :")
    loop = False
    if len(password)<8:
        loop = True
        print("enter password more than 8")
    if not password.isalnum():
        print(" password must not contain special character")
        loop=True 
    if  password.isdigit():
        print(" password must contain letter")
        loop = True
    if  password.isalpha():
        print(" password must contain special nomber")
        loop = True   

print("password correct . your  password is :", password)
