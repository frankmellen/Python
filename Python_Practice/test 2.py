# 公斤和磅的重量转换代码，代码 01

def converter(weight):
    ponds = weight / 0.4535923699688862
    print("ponds(lb) = " + str(ponds))


converter(int(input("please enter weight (kg): ")))






# 公斤和磅的重量转换代码，代码 02

while True:
    weight = int(input("please enter weight(kg): "))
    ponds = weight / 0.45
    print("ponds(lb) = " + str(ponds))
