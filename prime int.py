lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for j in range(lower,upper + 1):
   if j> 1:
       for i in range(2,j):
           if (j% i) == 0:
               break
       else:
           print(j)
