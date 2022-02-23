s=int(input("Enter number:"))
real=s
rev=0
while(s>0):
    dig=s%10
    rev=rev*10+dig
    s=s//10
if(real==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
