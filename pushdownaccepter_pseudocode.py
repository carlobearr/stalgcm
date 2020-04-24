input_stack = result[][] #from xmlparser [0] = type, [1] = token
write_stack = []
write_stack.push("start") #mark start of document

#------------- main -------------------
while len(input_stack)!=0: #while input stack not empty
    if input_stack.pop(0)[1] == '<': #first char must be '<'
        if tagLeft() == false: 
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
                return true
            else:
                return false

    elif next[1] == "/": #if next is slash
        return closeNest()

    else:
        return false
        

def attribute(): #attribute detected must be followed by ="value"
    if input_stack.pop(0)[1] != "=":
        return false
    if input_stack.pop(0)[0] != "attribute value":
        return false

    next = input_stack.pop(0)

    if next[1] == " ": #space
        next = input_stack.pop(0)
        if next[0] == "attribute"
            return attribute()
        else
            return false

    elif next[1] == ">": #new nest

    elif next[1] == "/": #self closing
        next = input_stack.pop(0)
        if next[1] == ">"
            write_stack.pop() #terminate nest
            return closeTag()
        else
            return false
    else  
        return false



#wala pa tong mga to
def yungMayQuestionMark()

def nest(): #>

def closeTag(): # /




    
    
