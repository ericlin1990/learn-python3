def move(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        move(n-1,a,c,b);
        print(a,c)
        move(n-1,b,a,c);

n=int(input("please input hanoi number:"))
print(move(n,'A','B','C'))
