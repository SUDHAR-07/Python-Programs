a=input("enter the string")
b=''
i=-1
for h in a:
    b+=a[i]
    i-=1
print("the given str {} \n rev is {} " .format(a,b))
if(a==b):
    print("palindrome")
else:
    print("not palin drome")
    
