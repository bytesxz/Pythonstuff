import cmath
import random

#init
class Operations: #has all the possible operations that calc can do
    def __init__(self, n1, n2): #self represents a class inst/obj
        self.n1 = n1
        self.n2 = n2

    def mult(self):
        return self.n1 * self.n2

    def div(self):
        result = 0
        result = self.n1 / self.n2
        return result

    def add(self):
        result = 0
        result = self.n1 + self.n2
        return result

    def subt(self):
        result = 0
        result = self.n1 - self.n2
        return result

    def square(self):
        result = self.n1
        for i in range(1, self.n2):
            result = self.n1 * result
        return result


def runCheck(): #called before loop, set + return run to 0 or 1 based on input.
    run = 0
    while True:
        print("Run again?")
        keyhit = input('y/n: >')  
        if keyhit == 'y':
            run = 0
        elif keyhit == 'n':
            run = 1
        else:
            run = 0
            print("character not recognized.")
        return run
   
    
def MDASCaller():
    result = 0
    n1 = input("first number >")
    n2 = input("second number >")
    op = input("operation | * | / | + | - | s | >")
    Cinst = Operations(int(n1), int(n2))
    
    if op == '*':
        result = Cinst.mult()
    elif op == '/':
        result = Cinst.div()
    elif op == '+':
        result = Cinst.add()
    elif op == '-':
        result = Cinst.subt()
    elif op == 's':
        result = Cinst.square()
    else:
        print("operation not recognized")


    print(result)

class NumberGenerator:

   def randgenerator():
        return random.randrange(0, 101)

   def OP_chooser():
       opt = random.randrange(0,5)
       if opt == 0:
           return "*"
       elif opt == 1:
           return "/"
       elif opt == 2:
           return "+"
       elif opt == 3:
           return "-"
       elif opt == 4:
           return "s"
       else:
           print("randrange greater than available choices, dec by 1")
           return "-"


   def MDASCaller_internal():
    result = 0
    n1 = randgenerator()
    n2 = randgenerator()
    op = OP_chooser()
    Cinst = Operations(int(n1), int(n2))
    
    if op == '*':
        result = Cinst.mult()
    elif op == '/':
        result = Cinst.div()
    elif op == '+':
        result = Cinst.add()
    elif op == '-':
        result = Cinst.subt()
    elif op == 's':
        result = Cinst.square()
    else:
        print("operation not recognized")
    return result

   def randomresult():
        return MDASCaller_internal()

def calc():
    while 0 == runCheck():
        MDASCaller()


#run
generator_instance = NumberGenerator()
result = generator_instance.randomresult
print(result)








