#calculator using python
#defining function for adding/sybtracting/multiplying or divide
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
#user have to select these operations    
print('select operations.')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')
#use while loop for run without conditions until the break statement...
while True:
    #taking user input
    choice=input('enter choice(1,2,3,4)')
    
    if choice in ('1','2','3','4'):
        num1=float(input('enter the first number-->'))
        num2= float(input('enter the second number-->'))

    if choice=='1':
        print(num1,' +' ,num2,'=' ,'the sum is',add(num1,num2))
    
    elif choice=='2':
        print(num1,' -' ,num2,'=','the subtract' ,subtract(num1,num2))
    elif choice=='3':
         print(num1,'*' ,num2,'=','the multiply is' ,multiply(num1,num2))
    elif choice =='4':
        print(num1,'/',num2,'=','the divide is',divide(num1,num2))
        break 
    else:
        print('invalid options')