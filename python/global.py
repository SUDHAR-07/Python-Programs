b=1000
def p():
    a=1
    print(a)
    global b
    b=b-100
    print(b)
    return
print(b)
p()
