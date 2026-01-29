lst = (1,2,3,4,5,6,7)
k = 2

is_found: bool = False
for x in range(len(lst)):
    if k == lst[x]:
        is_found = True
        print(f"{k} has an index of {x}")
        break
    
if is_found == False:
    print(f"{k} was not found in the list")