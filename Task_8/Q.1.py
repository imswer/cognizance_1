import numpy as st

a= 20
b=25
arr = []
for i in range(a,b,1):
    
    arr.append(i)

my_input = st.array(arr)  
 
print(my_input)
 
print(f'Current Numbers  {my_input}')
 




ss = [1,1,1,1,1]
D =  st.insert(my_input,ss,0)

tt = [7,7,7,7,7]
J  = st.insert(D,tt,0)


jj = [13,13,13,13,13]

H = st.insert(J,jj,0)


aa = [19,19,19,19,19]
T = st.insert(H,aa,0)

print(f'final numbers {T}')
