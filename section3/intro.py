yob_str= (input("your year of birth?"))

while not yob_str.isdigit():
    print(" not a number , enter again")
    yob_str= (input("your year of birth?"))

yob = int(yob_str)
age = 2018-yob
print(age)
    