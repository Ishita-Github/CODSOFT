#Calculator
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=input("Enter any operation from '+','-','*','/':")
if operation=="+":
    result=num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/":
    result=num1/num2
else:
    print("Enter a valid operation")

#solution
print("The solution is:",result)





    
