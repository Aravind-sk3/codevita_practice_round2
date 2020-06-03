for i in range(int(input())):
    n=int(input())
    l=[]
    l1=[]
    for j in range(n):
        a,b=map(int,input().split())
        l.append(a)
        l1.append(b)
    k=abs(max(l1)-min(l1))
    k1=abs(max(l)-min(l))
    print(max(k,k1)**2)
