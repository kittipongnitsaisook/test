class Stacks:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty() == True:
            return "Stack is empty!"
        else:
            pop = self.stack.pop()
            return pop

    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self.stack)

s = Stacks()
print("Is empty?:",s.is_empty())
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)

print("Size after push",s.size())
print("Top element:",s.peek())

print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())
print("Pop:",s.pop())

print("Is empty?:",s.is_empty())
print("Pop from empty:",s.pop())
