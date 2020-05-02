'''
SUBMITTED BY:
MARK CAI
CARLO SANTOS
BRIAN SO

SUBMITTED TO:
MR. ARVIN REYES

STALGCM S15
'''
from sys import stdin

def error():
    print("NO")
    exit()

xml = ""
result = []

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
    xml = xml + a'''

state = 0
token = 0
temp = ""

'''

LEXICAL ANALYZER PART:
Scans each character in the given xml, which was dissected into one long string, and giving them their 
appropriate token types.

'''
for i in range(len(xml)):
    if state == 0:
        if xml[i] == "<":
            result.append(["Symbol", "<"])
            token = token + 1
            state = 1
    elif state == 1:
        if (xml[i].isalpha()):
            temp = temp + xml[i]
            state = 3
        elif (xml[i] == "?" or xml[i] == "/"):
            temp = temp + xml[i]
            result.append(["Symbol", temp])
            token = token + 1
            temp = ""
            state = 2
    elif state == 2:
        if (xml[i].isalpha()):
            temp = temp + xml[i]
            state = 3
        elif (xml[i] == ">"):
            result.append(["Symbol", xml[i]])
            token = token + 1
            state = 9
    elif state == 3:
        if (xml[i] == ">"):
            result.append(["Tag", temp])
            temp = ""
            token = token + 1
            result.append(["Symbol", ">"])
            token = token + 1
            state = 9
        elif (xml[i].isalpha() or xml[i].isdigit() or xml[i] == "_"):
            temp = temp + xml[i]
        elif (xml[i] == ':' or xml[i] == '-' or xml[i] == '.'):
            error()
        elif (xml[i] == " "):
            result.append(["Tag", temp])
            temp = ""
            token = token + 1
            state = 4
    elif state == 4:
        if (xml[i].isalpha()):
            temp = temp + xml[i]
            state = 5
        elif (xml[i] == "?" or xml[i] == "/"):
            temp = temp + xml[i]
            result.append(["Symbol", temp])
            temp = ""
            token = token + 1
            state = 2
    elif state == 5:
        if (xml[i] == "="):
            result.append(["Attribute", temp])
            token = token + 1
            temp = ""
            state = 6
            result.append(["Operator", xml[i]])
            token = token + 1
        elif (xml[i].isalpha() or xml[i].isdigit() or xml[i] == "_"):
            temp = temp + xml[i]       
    elif state == 6:
        if (xml[i] == '\"'):
            temp = temp + xml[i]
            state = 7
    elif state == 7:
        if (xml[i] != '\"'):
            temp = temp + xml[i]
        else:
            temp = temp + xml[i]
            result.append(["Attribute Value", temp])
            temp = ""
            token = token + 1
            state = 8
    elif state == 8:
        if (xml[i] == "?"):
            result.append(["Symbol", xml[i]])
        elif (xml[i] == ">"):
            result.append(["Symbol", xml[i]])
            token = token + 1
            state = 9
        elif (xml[i] == " "):
            state = 4
    elif state == 9:
        if (xml[i] == " " or xml[i] == "\n"):
            state = 0
        elif (xml[i] == "<"):
            result.append(["Symbol", "<"])
            token = token + 1
            state = 1
        else:
            state = 10
            temp = temp + xml[i]
    elif state == 10:
        if (xml[i] == "<"):
            result.append(["Value", temp])
            token = token + 1
            temp = ""

            result.append(["Symbol", "<"])
            token = token + 1
            state = 1
        else:
            temp = temp + xml[i]

#print(result)
'''for i in range(len(result)):
    print(result[i])'''
state = 0
count = 0
store = []
store.append("#")
'''print("==================")'''

'''

SYNTAX ANALYZER PART:
Scans the result list, which contains a 2D list of the token and its corresponding type inside, until 
count is equal to the number of tokens in the list and identifies if the token is in the right position. 
If it is correct, "YES" will be printed out, and if there is an error then "NO" will 
be printed out by calling the error() function.

'''

while (token != count):
    if state == 0:
        if (result[count][1] == "<"):
            state = 1
            count = count + 1
        else:
            error()
    elif state == 1:
        if (result[count][1] == "?"):
            state = 2
            count = count + 1
        else:
            error()
    elif state == 2:
        if (result[count][1] == "xml"):
            state = 3
            count = count + 1
        else:
            error()
    elif state == 3:
        if (result[count][0] == "Attribute"):
            state = 4
            count = count + 1
        elif (result[count][1] == "?"):
            state = 6
            count = count + 1
        else:
            error()
    elif state == 4:
        if (result[count][1] == "="):
            state = 5
            count = count + 1
        else:
            error()
    elif state == 5:
        if (result[count][0] == "Attribute Value"):
            state = 3
            count = count + 1
        else:
            error()
    elif state == 6:
        if (result[count][1] == ">"):
            state = 7
            count = count + 1
        else:
            error()
    elif state == 7:
        if (result[count][0] == "Value"):
            state = 12
            count = count + 1
        elif (result[count][1] == "<"):
            state = 8
            count = count + 1
        else:
            error()
    elif state == 8:
        if (result[count][1] == "/"):
            state = 10
            count = count + 1
        elif (result[count][0] == "Tag"):
            state = 9
            count = count + 1
            store.append(result[count-1][1])
        else:
            error()
    elif state == 9:
        if (result[count][1] == ">"):
            state = 7
            count = count + 1
        elif (result[count][0] == "Attribute"):
            state = 13
            count = count + 1
        else:
            error()
    elif state == 10:
        if (result[count][0] == "Tag" and (store[len(store)-1] == result[count][1])):
            state = 11
            store.pop()
            count = count +1
        else:
            error()
    elif state == 11:
        if (result[count][1] == ">"):
            state = 7
            count = count + 1
        else:
            error()
    elif state == 12:
        if (store[len(store)-1] != "#"):
            state = 7
        else:
            error()
    elif state == 13:
        if (result[count][1] == "="):
            state = 14
            count = count + 1
        else:
            error()
    elif state == 14:
        if (result[count][0] == "Attribute Value"):
            state = 15
            count = count + 1
        else:
            error()
    elif state == 15:
        if (result[count][1] == "/"):
            state = 11
            count = count + 1
        elif (result[count][1] == ">"):
            state = 7
            count = count + 1
        elif (result[count][0] == "Attribute"):
            state = 13
            count = count + 1
        else:
            error()
    #token = token - 1

print("YES")