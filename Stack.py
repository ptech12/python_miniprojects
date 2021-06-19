class Stack:
    def __init__(self):
        self.val=[]
    def add(self,data):
        if data in self.val:
            return False
        self.val.append(data)
        return True
    def remove(self):
        self.val.pop()
    def printstack(self):
        return self.val
    def peek(self):
        return self.val[-1]
if __name__ == '__main__':
    stack=Stack()
    n=int(input("Enter Input Count : "))
    for i in range(n):
        stack.add(int(input(f"Enter Integer Number {i+1}: ")))
    print("***Stack***")
    print(stack.printstack())


    stack.remove()
    print("Stack after pop")
    print(stack.printstack())
    print(stack.peek())