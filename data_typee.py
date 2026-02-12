i=int(input("enter a integer i= :"))
f=float(i)
print("float value of integer i is :",f)
b=bool(i)
print("Boolean value of i is :",b)
s=str(i)
print("String form of i is :",s)

#convertion from list to tuple
lst=[1,2,3,4,5]
tup=tuple(lst)
print("tuple form of lst is : ",tup)

#conversion from list to set
lst=[1,2,3,4,5,5]
s = set(lst)
print("Set form of list is: ", s)

#conversion from ascii_number to ascii_char
ascii_number=66
ascii_ch=chr(ascii_number)
print(ascii_ch)

