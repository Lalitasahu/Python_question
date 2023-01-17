# 🙂=10
#  😀=11
#  😁=😀+🙂
"""n=int(input("Enter the series : "))
series=1
for i in range(1,n+1):
    series = series+(1/i)
    print(series)"""

"""n=int(input("Enter the series : "))
series=1
for i in range(1,n+1):
    series=series+1/(i**i)
print(series)"""

"""n=int(input("Enter the series : "))
series=1
for i in range(1,n+1):
    if i%2==0:
        series=series+i**3
    else:
        series=series+i**2
print(series)"""


"""n=int(input("enter the number "))
n1=0
n2=1
s=0
sum=0
for i in range(n):
    s=n1+n2
    print(s)
    n1=n2
    n2=s
    sum=sum+s
print(sum)"""


"""n=int(input("enter the number "))
n1=0
n2=1
s=0
even=0
odd=0
for i in range(n):
    s=n1+n2
    print(s)
    n1=n2
    n2=s
    if( s%2 ==0):
        even=even+s
    else:
        odd=odd+s
print("This is even ",even)
print("This is odd ",odd)
# print("This is sum: ",sum)"""


"""n=int(input("enter the number ")) #not complete
n1=0
n2=1
s=0
sum=0
for i in range(n,0,-1):
    s=n1+n2
    print(s)
    n1=n2
    n2=s
#     sum=sum+s
# print(sum)"""


""""n=int(input("enter the first value : "))
n1=int(input('enter the second value: '))
find=int(input('enter the find value: '))
flag=False
for i in range(n,n1):
    if i==find:
        flag=True
        break
if( flag==True):
    print('exist ')
else:
    print('not exist')"""


"""n=int(input("enter the first value : "))
n1=int(input('enter the second value: '))
find=int(input('enter the find value: '))
flag=False
for i in range(n,n1):
    if i==find:
        flag=True
        break
if( flag==True):
    print('exist ')
else:
    print('not exist')"""
