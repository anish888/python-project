#stack using python
class stack:
  def __init__(self):
    self.item=[]
  def is_empty(self):
    return self.item==[]
  def push(self,item):
    return self.item.append(item)
  def size(self):
    return len(self.item)
  def peek(self):
    return len(self.item)-1 
  def pop(self) :
    return self.item.pop()  
stack=stack()
print(stack.is_empty())
for i in range(1,10):
  stack.push(i)
print("total items in stack is-->",stack.item)  

print("size of stack is-->",stack.size())  
print(" peek element is-->",stack.peek()) 
print("popped element is-->",stack.pop())
       
