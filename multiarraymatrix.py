mat=[] #MAtrix list 
r=int(input("Enter rows :"))
c=int(input("Enter no of columns :"))
for i in range(r):
    E=[] #Empty list for temporily storing values 
    for j in range(c):
        a=int(input("Enter value to be added :"))
        E.append(a) #adding all elements in the list
    mat.append(E) #adding the list in matrix list 

for i in range(r):
    for j in range(c):
        print(mat[i][j],end='\t')
    print()
print(mat) # Nested list 