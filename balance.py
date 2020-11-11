#DEBAYAN MAJUMDER 2020
#Version 2.2
#THIS PROGRAM CHECKS THE BALANCE OF BRACKETS IN A CODE.
#IT CHECKS IF A BRACKET WHICH WAS OPENED, IS CLOSED OR NOT.

stack = []
#METHOD WHICH CHECKES IF A BRACKET BELONGS TO SAME FAMILY OR NOT
def checkBrackets(ch):
    c=0
    if((ch == "(") or (ch == ")")):
        c=1
    elif((ch == "[") or (ch == "]")):
        c=2
    elif((ch == "{") or (ch == "}")):
        c=3
    
    return c

#METHOD TO CHECK IF A CODE EVEN HAS BRACKETS IN IT
def checkForNull(code):
    c=0
    for this in code:
        if(checkBrackets(this) != 0):
            c = c + 1
            
    return c

#ORIGINAL FUNCTION
def checkBalance(brackets):                                                  
    size = len(brackets)
    i=0
    c=0

    while (size!=0):
        ch = brackets[i]                                                      

        if((ch == "(") or (ch == "{") or (ch == "[")):  
            #checking for opening brackets and then adding them to stack
            stack.append(ch)                       
            c=c+1
        elif((ch == ")") or (ch == "}") or (ch == "]")):
            #assigning the last value entered in the stack to "lastElement"
            lastElement = stack[-1]                                       
            if(checkBrackets(lastElement)==checkBrackets(ch)):
                #deleting element from the stack if entered and last value matched
                stack.pop()                                                   
                c=c-1
            else:
                stack.append(ch)
                c=c+1
        
        i=i+1
        size = size-1
    
    #RETURNING BOOLEAN OUTPUT
    if(c==0):
        return True
    else:
        return False                                                          

#MAIN BLOCK
N = int(input("Enter the no of checkings: "))                                  
i=0

while(N!=0):
    print("EXPRESSION NO: %s"%(i+1))
    user_input = input("Enter your expression: ")
    if(checkForNull(user_input)==0):
        print("ENTER A VALID EXPRESSION/CODE!!")
        i = i - 1
        N = N + 1
    elif(checkBalance(user_input)):
        print("BRACKETS ARE BALANCED PROPERLY")
    else:
        print("BRACKETS ARE NOT BALANCED PROPERLY")
    
    i=i+1
    N=N-1
    print()
    
#END OF CODE
