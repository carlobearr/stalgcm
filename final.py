symbol = "symbol"
tag = "tag"
attribute = "attribute"
operator = "operator"
attrvalue = "attribute value"
value = "value"

xml = ""

while True:
    a = input()
    if a == "":
        break
    xml = xml + a

status = 0
token = 0
num = 0

for i in range(len(xml)):
    if status == 0:
        if xml[i] == '<':
