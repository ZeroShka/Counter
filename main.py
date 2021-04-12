work = True

def counter(string):
    cA = 0
    cE = 0
    cI = 0
    cO = 0
    cU = 0
    cY = 0
    string = string.lower()

    for i in range(len(string)):

        if (string[i] == "a"):
            cA += 1
        elif (string[i] == "e"):
            cE += 1
        elif (string[i] == "i"):
            cI += 1
        elif (string[i] == "o"):
            cO += 1
        elif (string[i] == "u"):
            cU += 1
        elif (string[i] == "y"):
            cY += 1
        else:
            i = i + 1

    print(f"a {cA}, o {cO}, u {cU}, i {cI}, e {cE}, y {cY}")


while work:
    string = input()
    counter(string)
