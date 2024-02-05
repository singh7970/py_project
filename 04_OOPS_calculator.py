class cali:#cali is my CLASS
    def add(self,a,b):
        print( "add-- ",a+b)

    def subtract(self,a,b):
         print("subtract-- ",a-b)
    
    def multiply(self,a,b):
        print ("multiply",a*b)
    
    def devide (self,a,b):
          print ("devide",a/b)

#calci is my object
calci=cali()

num1=int(input("Enter the first number\t"))
num2=int(input("Enter the second number\t"))

print("1.ADD \n 2.MULTIOLY \n 3.SUBTRACT \n 4.DIV \n")
c=int(input("ENTER THE NUMBER\t"))

if(c==1):
     calci.add(num1,num2)
elif(c==2): 
     calci.multiply(num1,num2)
elif(c==3):     
     calci.subtract(num1,num2)

elif(c==4):
      calci.devide(num1,num2)
else:
     print("Invailed")      













    
 

