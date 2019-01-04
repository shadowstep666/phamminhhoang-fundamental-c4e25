

#person = ["quan",25,"ha noi",3,False,125]

# kho hieu


# person ={}
# print(person)
# print(type(person))


# person={
#     "name":"quan"
# }
# print(person)


# person={
#     "name":"quan",
#     "age":"25",
# }
# print(person)




person={
    "name":"quan",
    "age":25,
    "location":"Hanoi",
    "exes": 3,
    "status": False,
    "friends":125,
}
person["name"]="anhquan"
person["exp"]=2 # key ton tai thi la update , khong ton ton thi la create
print(person)


del person["exes"]
print(person)

# print(person["location"])
# print(person["exes"])
# print(person["status"])
# print(person["friends"])