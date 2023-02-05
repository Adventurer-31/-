n = int(input())
l1 = [1 for _ in range(n+1)]    #判断是否为质数
l2 = [1] * (n+1)    #存最大质因数
l3 = []    #存质数
for i in range(2, n+1):
    if l1[i]:
        l3.append(i)
        l2[i] = i
    for j in l3:
        if j * i > n:
            break
        l1[j*i] = 0
        l2[j*i] = j
        if i % j == 0:
            break

l4 = list(map(int,input().split()))    #输入内容列表
dp = [float('-inf') for _ in range(n+1)]
dp[1] = l4[0]
dp[2] = l4[0] + l4[1]
dic1 = dict(zip(range(2, n+1),[[] for _ in range(n-1)]))
for i in range(1, n):
    for j in range(1, l2[n-i]+1):
        dic1[i+j].append(i)
for i in range(3, n+1):
    dp[i] = max(dp[j] for j in dic1[i-2])+l4[i-1]
print(dp[n])