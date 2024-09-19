num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

def Addition(num1,num2):
    sum=num1+num2
    print("The Result is : ",sum)


def Subtraction(num1,num2):
    sub=num1-num2
    print("The Result is : ",sub)

            
def Multiplication(num1,num2):
    mul=num1*num2
    print("The Result is : ",mul)


            
def Division(num1,num2):
    div=num1/num2
    print("The Result is : ",div)
            
#Creating Menu
print("1. For Addition")
print("2.For Subtraction")
print("3.For Multiplication")
print("4.For Division")
print("5.For Exit")
select=int(input("enter the  number between 1 to 5:"))         
while True:

  if select ==1:
    Addition(num1,num2)
    break
  elif select ==2:
    Subtraction(num1,num2)
    break
  elif select ==3:
    Multiplication(num1,num2)
    break
  elif select ==4:
    Division(num1,num2)

  elif select ==5:
      break
  else:
      print("invalid input")
    