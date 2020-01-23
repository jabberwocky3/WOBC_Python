import sys
arg1 = str(sys.argv[1])

def createPhoneNumber(arg1):
    number = list(arg1)
    areacode = number[0:3]
    area = "".join(areacode)
    firstpart = number[3:6]
    first = "".join(firstpart)
    lastpart = number[6:10]
    last = "".join(lastpart)

    print(f"({area}){first}-{last}")


if __name__ == "__main__":
    createPhoneNumber(arg1)
