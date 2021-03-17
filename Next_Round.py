num=0
n, k = map(int, input().split())
scores = list(map(int, input().split()))
new=scores[k-1]
for i in scores:
    if i>0:
        if i>=new:
            num+=1

print(num)
