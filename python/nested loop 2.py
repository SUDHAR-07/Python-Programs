i=1
s=0
while(i>1):
    for j in range(1,9,i):
        s=s+1
        print("!",end="\t")
    print(end="\n")
    i+=1
print(s)
