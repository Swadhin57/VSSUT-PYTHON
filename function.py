def add_numbers(a,b):
    return a+b

def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)

square = lambda X: X*X

n1=int(input("enter first number :"))
n2=int(input("enter second number :"))
sum = add_numbers(n1,n2)
print("sum is :",sum)

print("factorial of first number is :",factorial(n1))

print("square of first number is :",square(n1))



       
       
       
