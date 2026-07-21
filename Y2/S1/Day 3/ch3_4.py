"""Write a class calculator that operates through the function run(instructions) with the following instructions:

    +: Pop 2 values from the stack, add them, and push the result onto the stack.
    -: Pop 2 values from the stack, subtract the top value from the second value, and push the result onto the stack.
    *: Pop 2 values from the stack, multiply them, and push the result onto the stack.
    /: Pop 2 values from the stack, divide the second value by the top value, and push the result onto the stack.
    DUP: Duplicate (not double) the top value of the stack.
    POP: Pop the top value from the stack and discard it.
    PSH: Push a number onto the stack.

Note: Any other instructions (such as letters) should result in "Invalid instruction: [instruction]".

* Stack Calculator *
Enter arguments : 5 6 +
11
"""

class Stack :
    def __init__(self, items = None):
        if items == None :
            self.items = []
        else:
            self.items = items
        pass
    def push(self, item):
        self.items.append(item)
        return self.items
    def pop(self):
        if(self.isEmpty()==False):
            self.items.pop()
        else :
            self.items = []
        return self.items
    def peek(self) :
        if(self.isEmpty()):
            return 0
        else:
            return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        # s = f"Value in Stack = "
        s=""
        for item in self.items :
            s+= str(item)
        return s
    
class calculator:
    def __init__(self):
        self.result = 0
        self.instructions = ""
        self.stack = Stack()
        self.breakFlag = False
        pass

    def run(self,instructions):

        self.instructions = instructions

        for instruction in self.instructions :
            if self.breakFlag:
                return
            self.ExecuteCommand(instruction)
        if self.breakFlag:
            return
        else:
            print(self.stack.peek())
            return
    
    def ExecuteCommand(self,instruction):
        try :
            instruction = int(instruction)
            self.stack.push(instruction)
            self.result = instruction
            return
        except:
            if(instruction == "+"):
                self.Plus()
            elif(instruction == "-"):
                self.Minus()
            elif(instruction == "*"):
                self.Multiply()
            elif(instruction == "/"):
                self.Divide()
            elif(instruction == "DUP"):
                self.Duplicate()
            elif(instruction == "POP"):
                self.Pop()
            else :
                self.breakFlag = True
                print(f"Invalid instruction: {instruction}")
                
            return
                    

    def Plus(self):
        _val1 = self.stack.peek()
        self.stack.pop()
        _val2 = self.stack.peek()
        self.stack.pop()
        _result = _val1+_val2
        self.ExecuteCommand(_result)
        return
    
    def Minus(self):
        _val1 = self.stack.peek()
        self.stack.pop()
        _val2 = self.stack.peek()
        self.stack.pop()
        _result = _val1-_val2
        self.ExecuteCommand(_result)
        return

    def Multiply(self):
        _val1 = self.stack.peek()
        self.stack.pop()
        _val2 = self.stack.peek()
        self.stack.pop()
        _result = _val1*_val2
        self.ExecuteCommand(_result)
        return

    def Divide(self):
        _val1 = self.stack.peek()
        self.stack.pop()
        _val2 = self.stack.peek()
        self.stack.pop()
        _result = _val1/_val2
        self.ExecuteCommand(_result)
        return

    def Duplicate(self):
        _val1 = self.stack.peek()
        self.ExecuteCommand(_val1)
        return

    def Pop(self):
        self.stack.pop()
        return

print("* Stack Calculator *")
inputList = input("Enter arguments : ").split(" ")
calc = calculator()
calc.run(inputList)