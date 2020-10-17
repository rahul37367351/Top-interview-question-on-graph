Activity 1
   def password(string):
    
    s1=string.split()
    r=""
    for i in range(len(s1)):
        r=r+s1[i][0]+s1[i][-1]
    return r
    
string ="piyush sankhala doing his work"
password_string=password(string)
print(password_string)


Activity 2

def FibonacciRecursion(n):  
   if f <= 1:  
       return f  
   else:  
       return(FibonacciRecursion(f-1) + FibonacciRecursion(f-2))  
f= int(input("Enter the Number of terms? "))  
if f<= 0:   
   print("Please enter Postive integer")  
else:  
   print("Fibonacci sequence will be :",end= " ")  
   for i in range(f):  
       print(FibonacciRecursion(i),end=" ")



Activity 3
P1=input()
if(roll[0]==’1’):
      print(“UG”)
else:
      print(“PG”)
if(roll[1:4]==’051’):
     print(“Department : MCA”)
print(“year:20”+roll[4:6])
print(“ID:”+roll[6:])

