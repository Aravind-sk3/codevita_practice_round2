n=int(input())
l=list(map(int,input().split()))
l1=[]
p=0
for i in l:
    p=p+i
    l1.append(p)
for _ in range(int(input())):
    a=int(input())
    if l1[n-1]<a:
        print("-1")
    else:
        for i in range(n):
            if l1[i]>=a:
                print(i+1)
                break
