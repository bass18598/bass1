num=int(input("enter the number"))
fact=1
if num<0:
  print("please enter the positive  number")
elif num==0:
  print("factorial for 0 is 1")
else:
  for i in  range(1,num+1 ):
    fact*=i
    print("fact of" ,num, "is",fact)
    
  
