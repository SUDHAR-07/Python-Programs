i=1
s=0
while(i<=6):
    for j in range(1,i):
        s=s+1
        print(j,end="\t")
    print(end="\n")
    i+=1
print(s)    
