# for 반복문 : dictionary
apt = {
    "101호" : "2019.05 입주",
    "102호" : "공실",
    "103호" : "2021.01 입주",
    "104호" : "공실",
    "105호" : "공실"
}

for x in apt:
    print(x, "입실 여부 : ",apt[x])