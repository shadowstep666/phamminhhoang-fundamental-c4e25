danh_muc={
    "en":"tieng anh",
    "vn":"tieng viet",
    "cn":"tieng trung",
    "jn":"tieng nhat",
}
while True:
    x = (input("nhap vao du lieu:"))
    print(danh_muc[x])
    need=input("do you want to change information (y/n)")
    if need =="y":
        new_tran=input("new tran :")
        danh_muc[x]=new_tran
        print(danh_muc[x])
        thay_doi=input("do you want to save (y/n)") 
        if thay_doi == "y":
            danh_muc[x]=new_tran
            print(danh_muc)
        elif thay_doi == "n":
            break

# while True :
#     if x == "en":
#         print(danh_muc["en"])
#         break
#     if x == "vn":
#         print(danh_muc["vn"])
#         break
#     if x == "cn":
#         print(danh_muc["cn"])
#         break
#     if x == "jn":
#         print(danh_muc["jn"])
#         break
#     if x == "change":
#         print("do you want to change information (y/n)")
#         a= (input("nhap vao du lieu:"))
#         if a=="y":
#             print("du lieu muon thay doi")
#             x = (input("nhap vao du lieu muon thay doi:"))
#             person[]=
#         elif a == "n"
#             break
#     else :
#         print("wrong,hay nhap lai")
#         x = (input("nhap vao du lieu:"))