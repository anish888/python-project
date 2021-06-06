#stack using python
#first create class
class stack:
#function for initalize a stack
  def __init__(self):
    self.item=[]
  #defining function if stack is empty or not...if stack is empty return true or else -false  
  def is_empty(self):
    return self.item==[]
  # defining function for add items into stack  
  def push(self,item):
    return self.item.append(item)
  #defining function for size of the stack  
  def size(self):
    return len(self.item)
#defining functio for top of element in stack
  def peek(self):
    return len(self.item)-1 
 #defining function for removig item from stack   
  def pop(self) :
    return self.item.pop()  
 #initialize class stack as stack   
stack=stack()

print(stack.is_empty())
#appending element using for loop
for i in range(1,10):
  stack.push(i)
print("total items in stack is-->",stack.item)  

print("size of stack is-->",stack.size())  
print(" peek element is-->",stack.peek()) 
print("popped element is-->",stack.pop())
       
