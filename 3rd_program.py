S1=set(map(int,input("enter elements of first set:").split()))
print(S1)
S2=set(map(int,input("enter elements of second set:").split()))
print(S2)
common_elements= S1 & S2
if common_elements:
    print("common elements are :",common_elements)
else:
    print("no common elements")
