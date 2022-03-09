import numpy as np
a =[]
b = []

n = int(input("Enter no.of elements "))

# creating first array (from user)
for i in range(0, n):
    s = int(input("Enter number in first array :"))
 
    a.append(s) 
     
print(a)

# creating second array (from user)


for j in range(0, n):
    t = int(input("Enter number in second array :"))
 
    b.append(t) 
     
print(b)
 
s = np.array(a)
t = np.array(b)


out_num = np.add(s,t) 
print ("output number after addition  : ", out_num)

