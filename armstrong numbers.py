n=int(input())
o=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**o
    temp//=10
if n==sum:
    print(n,"is armstrong number")
else:
    print(n,"is not a armstrong")