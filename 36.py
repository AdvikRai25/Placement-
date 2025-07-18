students = [
    {"Name": "raju", "Dept": "cse", "Marks": [20, 30, 40]},
    {"Name": "vijay", "Dept": "cse", "Marks": [10, 70, 43]},
    {"Name": "pavi", "Dept": "ece", "Marks": [22, 38, 56]},
    {"Name": "rose", "Dept": "ece", "Marks": [26, 36, 89]},
    {"Name": "virat", "Dept": "ece", "Marks": [16, 90, 43]}
]


for i in students:
    sum1 = sum(i["Marks"])
    per = round(sum1/3)
    i["per"] = per
des = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]

b = sorted(students, key= lambda x:x["per"], reverse=True)
index = 1
for i  in b:
    print("{}. {} stands {} : {}%".format(index, i["Name"], des[index-1], i["per"]))
    index += 1