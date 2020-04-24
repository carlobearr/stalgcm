source = open('test.xml', 'r')
text = []
tokens = []
while 1:
    char = source.read(1)
    if not char:
        break
    text.append(char)
source.close() 
    #if((65 <= ord(char) and 90 >= ord(char)) or (97 <= ord(char) and 122 >= ord(char))):
        #print(ord(char))  

result = []
i = 0

while text:
    i = i + 1
    char = text.pop(0)
    if char == "<":
        newState = "symbol"
    elif((65 <= ord(char) and 90 >= ord(char)) or (97 <= ord(char) and 122 >= ord(char))): #letters
        word = []
        while True:
            word.append(char)
            char = text[0]
            if ((65 <= ord(char) and 90 >= ord(char)) or (97 <= ord(char) and 122 >= ord(char))):
                char = text.pop(0)
            else:
                char = ''.join(word)
                break
        newState = "tag"
    elif ord(char) == 63: #?
        newState = "symbol"
    elif ord(char) == 32: #space
        newState = "symbol"
    elif ord(char) == 62: #>
        newState = "symbol"
    elif ord(char) == 47: #/
        newState = "slash"
    elif ord(char) == 61: #=
        newState = "operator"
    elif ord(char) == 10: #\n
        newState = "new line"
        char = " "
    elif ord(char) == 34:
        newState = "symbol"
    else:
        newState = "error"
    result.append("(" + str(i) + ") " + char + " - " + newState)
    tokens.append(char)

for a in range(len(result)):
    print(tokens[a])
        
#states: symbol, tag, attribute, value, attribute value

'''
positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "Python":
        newState = "Python_state"
    else:
        newState = "error_state"
    return (newState, txt)

def python_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "is":
        newState = "is_state"
    else:
        newState = "error_state"
    return (newState, txt)

def is_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "not":
        newState = "not_state"
    elif word in positive_adjectives:
        newState = "pos_state"
    elif word in negative_adjectives:
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

def not_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word in positive_adjectives:
        newState = "neg_state"
    elif word in negative_adjectives:
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)

def neg_state(txt):
    print("Hallo")
    return ("neg_state", "")

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Python_state", python_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Start")
    m.run("Python is great")
    m.run("Python is difficult")
    m.run("Perl is ugly")
'''
