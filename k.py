l = [1,2,4]
print(l)
m=7

lookup = {value:key for (value,key) in enumerate(l)}
print(lookup)
print(f"the index of 4 is {lookup[0]}")