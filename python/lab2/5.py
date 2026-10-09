list = [12, 36, 31, 42, 63]
cond = input()
for i in range(len(list)):
    op = ""
    num1 = -1
    num2 = -1
    val1 = -1
    val2 = -1

    for j in cond:
        if (j == "="):
            if (num1 == -1 and num2 == -1):

            if (num1 != -1 and num2 != -1):

            if (num1 == -1 and num2 != -1):

            if (num1 != -1 and num2 == -1):

        elif (j == "x"):
            num1 = list[0]
        elif (j == "y"):
            num2 = list[1]
        elif (j == "+"):
            op = "+"
        elif (j == "-"):
            op = "-"
        elif (j == "*"):
            op = "*"
        elif (j == "/"):
            op = "/"
        elif (j == "1" and j == "2" and j == "3" and j == "4" and j == "5" and j == "6" and j == "7" and j == "8" and j == "9" and j == "0"):
            num1 = int(j)


