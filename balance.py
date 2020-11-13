#DEBAYAN MAJUMDER 2020
#Version 3
#Version 3 comes with the support of reading multiple files(It takes input all kinds of files)
#If you get a file unsupported, please report me.

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

#ORIGINAL FUNCTION TO CHECK BRACKET BALANCE
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

            #checking if the list/array is empty, if yes, then breaking out of the loop  
            if(len(stack) ==0):
                #updating value of c for false output
                c=c+1
                break
            else:
                #assigning the last value entered in the stack to "lastElement"
                lastElement = stack[-1]

            if(checkBrackets(lastElement)==checkBrackets(ch)):
                #deleting element from the stack if entered and last value matched
                stack.pop()                                                   
                c=c-1
            else:
                stack.append(ch)
                c=c+1
        
        #updating the values
        i=i+1
        size = size-1
    
    #RETURNING BOOLEAN OUTPUT
    if(c==0):
        return True
    else:
        return False                                                          

#MAIN BLOCK
N = int(input("Enter the no of Checkings to be done: "))                                  
i=0

while(N!=0):
    print("EXPRESSION NO: %s"%(i+1))
    
    #taking file input path
    INP = input("Enter your path/File location: ")
    with open(INP) as thisCode:
        user_input = thisCode.read()

    #main fuction calls going here
    #checking even if brackets exists, if yes it checks balance
    if(checkForNull(user_input)==0):
        print("ENTER A VALID EXPRESSION/CODE")
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