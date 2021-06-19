def miss(arr):
    n=len(arr)
    total=(n+1)*(n+2)/2
    s=sum(arr)
    return total-s
N=int(input())
arr = list(map(int,input().strip().split()))[:N]
res=miss(arr)
print(res)