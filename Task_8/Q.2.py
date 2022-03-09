
a =[]
b = []

n = int(input("Enter no.of elements of first array"))


for i in range(0, n):
    s = int(input("Enter number in first array :"))
 
    a.append(s) 
     
print(a)

m = int(input("Enter no.of elements in second array"))
for j in range(0, m):
    t = int(input("Enter number in second array :"))
 
    b.append(t) 
     
print(b)

print(" ")

if s==t:
  print("true")
else:
  print("false")



