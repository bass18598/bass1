
upper=int(input("upper case"))
lower=int(input("lower case"))
for i in range(lower, upper + 1):
   order = len(str(i))
   sum = 0
   temp = i
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if i == sum:
       print(i)
