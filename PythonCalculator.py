import re

print("My Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run 
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
        
    if equation == 'quit':
        run = False
        print ("You have successfully exited the program")
    else:
        equation = re.sub('[a-zA-Z,.()" "]', '', equation)
        if previous == 0:
            previous =eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("The answer is ", previous)


while run:
    performMath()
