salary=[
    {
        "name":"Huy" ,
        "Salary per hour": 25 ,
        "hour" : 30 ,
    },
    {
        "name":"Quan" ,
        "Salary per hour": 25 ,
        "hour" : 20 ,
    },
    {
        "name":"Duc" ,
        "Salary per hour": 30 ,
        "hour" : 40 ,
    }
]

total=0
for i in range(len(salary)):
    luong=salary[i]["Salary per hour"]*salary[i]["hour"]
    total+=luong
    print(salary[i]["name"],luong,sep=".")
print("tong luong",total)
