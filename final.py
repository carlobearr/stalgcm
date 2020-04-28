from sys import stdin
def error():
    print("NO")
    exit()

symbol = "symbol"
tag = "tag"
attribute = "attribute"
operator = "operator"
attrvalue = "attribute value"
value = "value"

xml = ""
result = []

'''
while True:
    try:
        a = input()
        xml = xml + a
    except EOFError:
        break

'''
while True:
    a = input()
    if a == "":
        break
    xml = xml + a

status = 0
token = 0
temp = ""


for i in range(len(xml)):
    if status == 0:
        if xml[i] == "<":
            result.append(["symbol", "<"])
            token = token + 1
            status = 1

    elif status == 1:
        if (xml[i] == "?" or xml[i] == "/"):
            result.append(["symbol", xml[i]])
            token = token + 1
            temp = ""
            status = 2
        elif (xml[i].isalpha()):
            temp = temp + xml[i]
            status = 3

    elif status == 2:
        if (xml[i].isalpha()):
            temp = temp + xml[i]
            status = 3
        elif (xml[i] == ">"):
            result.append(["symbol", xml[i]])
            token = token + 1
            status = 9
    
    elif status == 3:
        if (xml[i].isalpha() or xml[i].isdigit() or xml[i] == "_"):
            temp = temp + xml[i]
        elif (xml[i] == ':' or xml[i] == '-' or xml[i] == '.'):
            error()
        elif (xml[i] == " "):
            result.append(["tag", temp])
            temp = ""
            token = token + 1
            status = 4
        elif (xml[i] == ">"):
            result.append(["tag", temp])
            temp = ""
            token = token + 1
            
            result.append(["symbol", ">"])
            token = token + 1
            status = 9

    elif status == 4:
        if (xml[i].isalpha()):
            temp = temp + xml[i]
            status = 5
        elif (xml[i] == "?" or xml[i] == "/"):
            temp = temp + xml[i]
            result.append(["symbol", temp])
            temp = ""
            token = token + 1
            status = 2

    elif status == 5:
        if (xml[i].isalpha() or xml[i].isdigit() or xml[i] == "_"):
            temp = temp + xml[i]
        elif (xml[i] == "="):
            result.append(["attribute", temp])
            token = token + 1
            temp = ""
            status = 6

            result.append(["operator", xml[i]])
            token = token + 1
    elif status == 6:
        if (xml[i] == '\"'):
            temp = temp + xml[i]
            status = 7
    elif status == 7:
        if (xml[i] != '\"'):
            temp = temp + xml[i]
        else:
            temp = temp + xml[i]
            result.append(["attribute value", temp])
            temp = ""
            token = token + 1
            status = 8
    elif status == 8:
        if (xml[i] == ">"):
            result.append(["symbol", xml[i]])
            token = token + 1
            status = 9
        elif (xml[i] == " "):
            status = 4
        elif (xml[i] == "?"):
            result.append(["symbol", xml[i]])
    elif status == 9:
        if (xml[i] == "<"):
            print("A")
            result.append(["symbol", "<"])
            token = token + 1
            status = 1
        elif (xml[i] == " " or xml[i] == "\n"):
            status = 0
        else:
            status = 10
            temp = temp + xml[i]
    elif status == 10:
        if (xml[i] == "<"):
            result.append(["value", "<"])
            token = token + 1
            temp = ""

            result.append(["symbol", "<"])
            token = token + 1
            status = 1
        else:
            temp = temp + xml[i]

#print(result)
for i in range(len(result)):
    print(result[i])
status = 0
count = 0
store = []

while (token != 0):
    if status == 0:
        if (result[count][1] == "<"):
            status = 1
            count = count + 1
        else:
            error()
    elif status == 1:
        if (result[count][1] == "?"):
            status = 2
            count = count + 1
        else:
            error()
    elif status == 2:
        if (result[count][1] == "xml"):
            status = 3
            count = count + 1
        else:
            error()
    elif status == 3:
        if (result[count][0] == "attribute"):
            status = 4
            count = count + 1
        elif (result[count][1] == "?"):
            status = 6
            count = count + 1
        else:
            error()
    elif status == 4:
        if (result[count][1] == "="):
            status = 5
            count = count + 1
        else:
            error()
    elif status == 5:
        if (result[count][0] == "attribute value"):
            status = 3
            count = count + 1
        else:
            error()
    elif status == 6:
        if (result[count][1] == ">"):
            status = 7
            count = count + 1
        else:
            error()
    elif status == 7:
        if (result[count][1] == "<"):
            status = 8
            count = count + 1
        elif (result[count][0] == "value"):
            status = 12
            count = count + 1
        else:
            error()
    elif status == 8:
        if (result[count][0] == "tag"):
            status = 9
            count = count + 1
            store.append(result[count-1][1])
        elif (result[count][1] == "/"):
            status = 10
            count = count + 1
        else:
            error()
    elif status == 9:
        if (result[count][1] == ">"):
            status = 7
            count = count + 1
        elif (result[count][0] == "attribute"):
            status = 13
            count = count + 1
        else:
            error()
    elif status == 10:
        if (result[count][0] == "tag" and store[len(store)-1] == result[count][1]):
            status = 11
            store.pop()
            count = count +1
        else:
            error()
    elif status == 11:
        if (result[count][1] == ">"):
            status = 7
            count = count + 1
        else:
            error()
    elif status == 12:
        if (store[len(store)-1] != "#"):
            status = 7
        else:
            error()
    elif status == 13:
        if (result[count][1] == "="):
            status = 14
            count = count + 1
        else:
            error()
    elif status == 14:
        if (result[count][0] == "attribute value"):
            status = 15
            count = count + 1
        else:
            error()
    elif status == 15:
        if (result[count][1] == "/"):
            status = 11
            count = count + 1
        elif (result[count][0] == "attribute"):
            status = 13
            count = count + 1
        elif (result[count][1] == ">"):
            status = 7
            count = count + 1
        else:
            error()

print("YES")