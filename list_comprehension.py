# SAMPLE PROGRAM FOR LIST COMPREHENSIONS 
'''
Short hand list operations are faster , code reduction,
memory allocated to list without having list to be resized at run time 
less time faster execution no need to call loop and appen() method to be called  reducung function overheads
'''

l=[i for i in range(1,11)]
print(f"Simple list containing 10 elements : {l}")

l1=[i  for i in range(1,11) if i%2==0] 
#If placing only if conditional it will come after loop
print(f" Placing if conditional after loop {l1}")

l2=[i if i%2==0  else "@" for i in range(13)]
print("If-Else Conditionals :" , l2)
#If_Else conditionals....