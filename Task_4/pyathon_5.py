rows = int(input("Enter no.of  Rows = "))

for i in range(rows - 1, -1, -1):
    for j in range(0, i):
        print(end = ' ')
    for k in range(i, rows):
        print('*', end = ' ')      
    print()
