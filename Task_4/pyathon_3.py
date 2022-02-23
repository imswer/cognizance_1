p=[]
b=int(input("Enter the no.of records:"))

for i in range (b):
     t=input("Enter the record (Roll no, Name, Marks):")
     s=t.split()
     d=list(s)
     p.append(d)
print("Roll no", "Name", "Marks", sep='   ')
for i in p:
    print(i[0], i[1], i[2], sep=' ')
print('ii')
l = p[1]
print(l[0], l[1], l[2], sep='   ')

