'''      Replace the Alphabet with their ASCII valus, and print sum of their factors     '''
def fact(a):
    j=0
    for i in range(1,a+1):
        if(a%i==0):
            j+=i
    return j
a=list(input())
b=""
for i in a:
    if i.isalpha():
        b+=str(ord(i))
    else:
        b+=i
print(fact(int(b)))
