result = [["symbol", "<"], ["tag", "gem"], ["symbol", ">"]]
input_stack = result #from xmlparser [0] = type, [1] = token #[][]
write_stack = []

write_stack.push("start") #mark start of document

#------------- main -------------------
while len(input_stack)!=0: #while input stack not empty
    if input_stack.pop(0)[1] == '<': #first char must be '<'
        if tagLeft() is False: 
            print("NO")
            break
    else:  #first char is not '<'
        print("NO")
        break

if len(write_stack)!= 0: #if write stack not empty
    print("NO")
else:
    print("YES")

#---------------- functions ----------------------

def tagLeft(): #symbol '<' detected
    next = input_stack.pop(0)

    if write_stack[0] == "start": #if start of document
        write_stack.pop(0) #remove start marker
        if next[1] == "?": #if next is '?'
            return yungMayQuestionMark()    

    if next[0] == "tag": #if next is tag
        write_stack.push(next[1]) #write tagname to write stack
        next = input_stack.pop(0)

        if next[0] == "attribute": # if next next is attr
            return attribute()

        elif next[1] == "/":  # if next next is slash
            next = input_stack.pop(0)
            if next[1] == ">":
                write_stack.pop() #terminate nest
                return True
            else:
                return False

    elif next[1] == "/": #if next is slash
        return closeNest()

    else:
        return False
        

def attribute(): #attribute detected must be followed by ="value"
    if input_stack.pop(0)[1] != "=":
        return False
    if input_stack.pop(0)[0] != "attribute value":
        return False

    next = input_stack.pop(0)

    if next[1] == " ": #space
        next = input_stack.pop(0)
        if next[0] == "attribute":
            return attribute()
        else:
            return False

    elif next[1] == ">": #new nest
        return
    elif next[1] == "/": #self closing
        next = input_stack.pop(0)
        if next[1] == ">":
            write_stack.pop() #terminate nest
            return closeTag()
        else:
            return False
    else  :
        return False


'''
#wala pa tong mga to
def yungMayQuestionMark()

def nest(): #>

def closeTag(): # /'''




    
    
