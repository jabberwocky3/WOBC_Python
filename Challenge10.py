import sys
arg1 = eval(str(sys.argv[1]))

def createPhoneNumber(arg1):
    for i in range(len(arg1)):
        arg1[i] = str(arg1[i])

    areacode = arg1[0:3]
    area = "".join(areacode)
    firstpart = arg1[3:6]
    first = "".join(firstpart)
    lastpart = arg1[6:10]
    last = "".join(lastpart)

    return (f"({area}) {first}-{last}")


if __name__ == "__main__":
    print(createPhoneNumber(arg1))
